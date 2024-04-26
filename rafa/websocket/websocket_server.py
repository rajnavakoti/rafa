import os
import aiohttp
from aiohttp import web
from dotenv import load_dotenv
from llama_index.core import load_index_from_storage, ChatPromptTemplate
from llama_index.llms.ollama import Ollama
from llama_index.core.base.llms.types import MessageRole
from rafa.prompts import default_prompts
from rafa.indexing import vector_store_indexing
from llama_index.core.llms import ChatMessage
from llama_index.core.memory import ChatMemoryBuffer

# Load environment variables from .env file
load_dotenv()

LLM_MODEL = os.environ.get("LLM_MODEL")
PERSIST_DB = os.environ.get("PERSIST_DB")
SYSTEM_PROMPT = default_prompts.DEFAULT_SYSTEM_PROMPTS
USER_PROMPT = default_prompts.DEFAULT_USER_PROMPT
MEMORY = ChatMemoryBuffer.from_defaults(token_limit=3900)

chat_text_qa_msgs = [
    ChatMessage(role=MessageRole.SYSTEM, content=SYSTEM_PROMPT),
    ChatMessage(role=MessageRole.USER, content=USER_PROMPT),
]

text_qa_template = ChatPromptTemplate(chat_text_qa_msgs)
LLM = Ollama(model=LLM_MODEL)

async def websocket_handler(request):
    ws = aiohttp.web.WebSocketResponse()  # Create WebSocketResponse object
    await ws.prepare(request)
    async for msg in ws:
        if msg.type == aiohttp.web.WSMsgType.TEXT:
            # response = get_query_answer(msg.data)
            response = get_chat_response(msg.data)
            await ws.send_str(str(response))  # Convert response to string before sending
    await ws.close()  # Close the WebSocket connection
    return ws

def get_query_answer(query: str) -> str:
    index = vector_store_indexing.index_from_storage()
    query_engine = index.as_query_engine(text_qa_template=text_qa_template, llm=LLM, chat_mode='condense_plus_context',
    memory=MEMORY)
    response = query_engine.query(query)
    print("response is: ", response)
    return response

def get_chat_response(query: str) -> str:
    index = vector_store_indexing.index_from_storage()
    print("memory is: ", MEMORY)
    chat_engine = index.as_chat_engine(verbose=True, llm=LLM, text_qa_template=text_qa_template, chat_mode='condense_plus_context',
    memory=MEMORY)
    response = chat_engine.chat(query)
    print("response is: ", response)
    return response

app = web.Application()
app.add_routes([web.get('/', websocket_handler)])

if __name__ == "__main__":
    web.run_app(app)
