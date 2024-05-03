import os
from dotenv import load_dotenv
from rafa.data_load import data_loader
from rafa.embedding import embedding_generator
from rafa.storage import context_storage
from rafa.indexing import vector_store_indexing
from llama_index.llms.ollama import Ollama
import logging

# Initialize logger
logger = logging.getLogger(__name__)

# Load and setup environment variables from .env file
load_dotenv()
IS_DOCKER = os.environ.get("IS_DOCKER")
LLM_MODEL = os.environ.get("DOCKER_LLM_MODEL") if IS_DOCKER else os.environ.get("LOCAL_LLM_MODEL")

# Load LLM model
LLM = Ollama(model=LLM_MODEL)

logging.basicConfig(level=logging.INFO)

def document_indexing_flow():
    """
    Main function to load data, generate embeddings, index and store them.
    """
    try:
        # Load documents
        documents = data_loader.load_documents()

        # Generate nodes from documents
        nodes = embedding_generator.generate_nodes_from_documents(documents)

        # Set storage context
        storage_context = context_storage.get_storage_context(nodes)

        # Save vector indexes
        index_vector_store = vector_store_indexing.index_vector_store(nodes, storage_context)

        return index_vector_store
    except Exception as e:
        logging.error("An error occurred during document indexing: %s", str(e))

def query_response(query: str) -> str:
    """
    Main function to query the indexed documents.
    """
    try:
        index = vector_store_indexing.index_from_storage()
        query_engine = index.as_query_engine(llm=LLM)
        chat_engine = index.as_chat_engine(llm=LLM)
        response = chat_engine.chat(query)
        logging.info("Response is: %s", response)
        logging.info("Response of response is: %s", response.response)
        return response
    except Exception as e:
        logging.error("An error occurred during query response: %s", str(e))
        return None

if __name__ == "__main__":
    document_indexing_flow()
    # query_response("can you check again?")
