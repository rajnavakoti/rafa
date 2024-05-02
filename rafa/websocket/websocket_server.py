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
from llama_index.core.bridge.pydantic import Field
import json

# Load environment variables from .env file
load_dotenv()

LLM_MODEL = os.environ.get("LLM_MODEL")
PERSIST_DB = os.environ.get("PERSIST_DB")
SYSTEM_PROMPT = default_prompts.DEFAULT_SYSTEM_PROMPTS
USER_PROMPT = default_prompts.DEFAULT_USER_PROMPT
QA_USER_PROMPT = default_prompts.DEFAULT_QA_USER_PROMPT
MEMORY = ChatMemoryBuffer.from_defaults(token_limit=3900)
BASE_URL = 'http://ollama-container:11434'

qa_text_qa_msgs = [
    ChatMessage(role=MessageRole.SYSTEM, content=SYSTEM_PROMPT),
    ChatMessage(role=MessageRole.USER, content=QA_USER_PROMPT),
]

chat_text_qa_msgs = [
    ChatMessage(role=MessageRole.SYSTEM, content=SYSTEM_PROMPT),
    ChatMessage(role=MessageRole.USER, content=USER_PROMPT),
]

text_qa_template = ChatPromptTemplate(chat_text_qa_msgs)
qa_text_qa_msgs = ChatPromptTemplate(qa_text_qa_msgs)
LLM = Ollama(model=LLM_MODEL, base_url=BASE_URL, request_timeout=90)

async def websocket_handler(request):
    ws = aiohttp.web.WebSocketResponse()  # Create WebSocketResponse object
    await ws.prepare(request)
    async for msg in ws:
        if msg.type == aiohttp.web.WSMsgType.TEXT:
            data = json.loads(msg.data)
            text = data['text']
            chat_mode = data['chat_mode']
            talk_to = data['talk_to']
            # response = get_query_answer(msg.data)
            if chat_mode == 'qa':
                response = get_query_answer(text, talk_to)
            else:
                response = get_chat_response(text, talk_to)
            await ws.send_str(str(response))  # Convert response to string before sending
    await ws.close()  # Close the WebSocket connection
    return ws

def get_query_answer(query: str, talk_to: str) -> str:
    index = vector_store_indexing.index_from_storage()
    if 'ham' in talk_to:
        query_engine = index.as_query_engine(llm=LLM, chat_mode='simple')
    else:
        query_engine = index.as_query_engine(text_qa_template=qa_text_qa_msgs, llm=LLM)
    response = query_engine.query(query)
    print("response is: ", response)
    return response

def get_chat_response(query: str, talk_to: str) -> str:
    index = vector_store_indexing.index_from_storage()
    print("memory is: ", MEMORY)
    if 'ham' in talk_to:
        chat_engine = index.as_chat_engine(verbose=True, llm=LLM, chat_mode='simple')
    else:
        chat_engine = index.as_chat_engine(verbose=True, llm=LLM, text_qa_template=text_qa_template, chat_mode='condense_plus_context',
    memory=MEMORY)
    response = chat_engine.chat(query)
    print("response is: ", response)
    return response

app = web.Application()
app.add_routes([web.get('/', websocket_handler)])

if __name__ == "__main__":
    web.run_app(app)
