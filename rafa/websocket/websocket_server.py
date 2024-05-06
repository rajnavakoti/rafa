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
import logging

# Load environment variables from .env file
load_dotenv()
IS_DOCKER = os.environ.get("IS_DOCKER")
LLM_MODEL = os.environ.get("DOCKER_LLM_MODEL") if IS_DOCKER else os.environ.get("LOCAL_LLM_MODEL")
PERSIST_DB = os.environ.get("DOCKER_PERSIST_DB") if IS_DOCKER else os.environ.get("LOCAL_PERSIST_DB")
MEMORY_TOKEN_LIMIT = os.environ.get("DOCKER_CHAT_MEOMRY_TOKEN_LIMIT") if IS_DOCKER else os.environ.get("LOCAL_CHAT_MEOMRY_TOKEN_LIMIT")
OLLAMA_BASE_URL = os.environ.get("DOCKER_OLLAMA_SERVER") if IS_DOCKER else os.environ.get("LOCAL_OLLAMA_SERVER")
OLLAMA_SERVER_CONNECTION_TIMEOUT = os.environ.get("DOCKER_OLLAMA_SERVER_TIMEOUT") if IS_DOCKER else os.environ.get("LOCAL_OLLAMA_SERVER_TIMEOUT")
CHAT_MODE = os.environ.get("DOCKER_CHAT_MODE") if IS_DOCKER else os.environ.get("LOCAL_CHAT_MODE")
STORAGE_TYPE = os.environ.get("STORAGE_TYPE")

SYSTEM_PROMPT = default_prompts.DEFAULT_SYSTEM_PROMPTS
USER_PROMPT = default_prompts.DEFAULT_USER_PROMPT
QA_USER_PROMPT = default_prompts.DEFAULT_QA_USER_PROMPT
MEMORY = ChatMemoryBuffer.from_defaults(token_limit=int(MEMORY_TOKEN_LIMIT))

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

LLM = Ollama(model=LLM_MODEL, base_url=OLLAMA_BASE_URL, 
             request_timeout=OLLAMA_SERVER_CONNECTION_TIMEOUT)

async def websocket_handler(request):
    ws = aiohttp.web.WebSocketResponse()  # Create WebSocketResponse object
    await ws.prepare(request)
    try:
        async for msg in ws:
            if msg.type == aiohttp.web.WSMsgType.TEXT:
                data = json.loads(msg.data)
                text = data['text']
                chat_mode = data['chat_mode']
                collection = data['collection']
                
                if chat_mode == 'qa':
                    response = get_query_response(text, collection)
                else:
                    response = get_chat_response(text, collection)
                
                await ws.send_str(str(response))  # Convert response to string before sending
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
    
    await ws.close()  # Close the WebSocket connection
    return ws

def get_query_response(query: str, collection: str) -> str:
    try:
        if STORAGE_TYPE == "in-memory":
            index = vector_store_indexing.index_from_storage()
        elif STORAGE_TYPE == "chromadb":
            index = vector_store_indexing.index_from_chroma_storage(collection)
        query_engine = index.as_query_engine(text_qa_template=qa_text_qa_msgs, 
                                             llm=LLM)
        logging.info("Query engine created successfully.")
        response = query_engine.query(query)
        logging.info("Query processed successfully.")
        logging.info("response is: {}".format(response))
        return response
    except Exception as e:
        logging.error(f"An error occurred while processing the query at line {e.__traceback__.tb_lineno}: {str(e)}")
        return "An error occurred while processing the query."

def get_chat_response(query: str, collection: str) -> str:
    try:
        if STORAGE_TYPE == "in-memory":
            index = vector_store_indexing.index_from_storage()
        elif STORAGE_TYPE == "chromadb":
            index = vector_store_indexing.index_from_chroma_storage(collection)

        chat_engine = index.as_chat_engine(verbose=True, llm=LLM, 
                                           text_qa_template=text_qa_template, 
                                           chat_mode=CHAT_MODE,
                                           memory=MEMORY)
        response = chat_engine.chat(query)
        logging.info("response is: {}".format(response))
        return response
    except Exception as e:
        logging.error(f"An error occurred while processing the chat: {str(e)}")
        return "An error occurred while processing the chat."

app = web.Application()
app.add_routes([web.get('/', websocket_handler)])

if __name__ == "__main__":
    web.run_app(app)
