import os
import logging
from dotenv import load_dotenv
from llama_index.llms.ollama import Ollama
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
import chromadb
from rafa.data_load import data_loader
from rafa.embedding import embedding_generator
from rafa.storage import context_storage
from rafa.indexing import vector_store_indexing

load_dotenv()

IS_DOCKER = os.environ.get("IS_DOCKER")
DATA_COLLECTION_PATH = os.environ.get("DOCKER_DATA_DIR") if IS_DOCKER else os.environ.get("LOCAL_DATA_DIR")
CHROMA_PERSIST_DB = os.environ.get("DOCKER_CHROMA_PERSIST_DB") if IS_DOCKER else os.environ.get("LOCAL_CHROMA_PERSIST_DB")
STORAGE_TYPE = os.environ.get("STORAGE_TYPE")

# Configure logging
logging.basicConfig(filename='app.log', level=logging.ERROR)

def document_indexing_flow():
    try:
        documents = data_loader.load_documents()
        nodes = embedding_generator.generate_nodes_from_documents(documents)
        storage_context = context_storage.get_storage_context(nodes)
        index_vector_store = vector_store_indexing.index_vector_store(nodes, storage_context)
    except Exception as e:
        logging.error(f"Error in document indexing flow: {str(e)}")

def chroma_document_indexing_flow():
    try:
        collections = [folder for folder in os.listdir(DATA_COLLECTION_PATH) if os.path.isdir(os.path.join(DATA_COLLECTION_PATH, folder))]
        with chromadb.PersistentClient(path=CHROMA_PERSIST_DB) as db:
            for collection_name in collections:
                documents = data_loader.chroma_load_documents(collection_name)
                collection = db.get_or_create_collection(collection_name)
                vector_store = ChromaVectorStore(chroma_collection=collection)
                storage_context = context_storage.get_chroma_storage_context(vector_store)
                vector_store_indexing.chroma_index_vector_store(documents, storage_context)

                print(chromadb.PersistentClient(path=CHROMA_PERSIST_DB).list_collections())
    except Exception as e:
        logging.error(f"Error in chroma document indexing flow: {str(e)}")

if __name__ == "__main__":
    logging.info("Starting data vector service...")
    try:
        if STORAGE_TYPE == "in-memory":
            logging.info("In-Memory used for storage")
            document_indexing_flow()
        elif STORAGE_TYPE == "chromadb":
            logging.info("ChromaDB used for storage")
            chroma_document_indexing_flow()
        else:
            logging.error("Invalid storage type specified.")
    except Exception as e:
        logging.error(f"Error in main execution: {str(e)}")
