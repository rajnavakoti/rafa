from data_load import data_loader
from embedding import embedding_generator
from storage import context_storage
from indexing import vector_store_indexing
from llama_index.llms.ollama import Ollama

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

LLM_MODEL = os.environ.get("LLM_MODEL")
LLM = Ollama(model=LLM_MODEL)

def document_indexing_flow():
    # Load documents
    documents = data_loader.load_documents()

    # Generate nodes from documents
    nodes = embedding_generator.generate_nodes_from_documents(documents)

    # Set storage context
    storage_context = context_storage.get_storage_context(nodes)

    # Save vector indexes
    index_vector_store = vector_store_indexing.index_vector_store(nodes, storage_context)

def query_response(query: str) -> str:
    index = vector_store_indexing.index_from_storage()
    query_engine = index.as_query_engine(llm=LLM)
    chat_engine = index.as_chat_engine(llm=LLM)
    # response = query_engine.query(query)
    response = chat_engine.chat(query)
    print("response is: ", response)
    print("response of response is: ", response.response)
    return response

if __name__ == "__main__":
    document_indexing_flow()
    # query_response("can you check again?")


