import os
import logging
from dotenv import load_dotenv
from llama_index.vector_stores.chroma import ChromaVectorStore
import chromadb
from rafa.data_load import data_loader
from rafa.embedding import embedding_generator
from rafa.storage import context_storage
from rafa.indexing import vector_store_indexing
from llama_index.vector_stores.chroma import ChromaVectorStore

load_dotenv()

IS_DOCKER = os.environ.get("IS_DOCKER")
DATA_COLLECTION_PATH = os.environ.get("DOCKER_DATA_DIR") if IS_DOCKER else os.environ.get("LOCAL_DATA_DIR")
CHROMA_PERSIST_DB = os.environ.get("DOCKER_CHROMA_PERSIST_DB") if IS_DOCKER else os.environ.get("LOCAL_CHROMA_PERSIST_DB")
STORAGE_TYPE = os.environ.get("STORAGE_TYPE")
EMBED_MODEL = os.environ.get("DOCKER_EMBED_MODEL") if IS_DOCKER else os.environ.get("LOCAL_EMBED_MODEL")
CHROMA_DB_HOST = os.environ.get("CHROMA_DB_HOST")
CHROMA_DB_PORT = os.environ.get("CHROMA_DB_PORT")

def document_indexing_flow():
    try:
        documents = data_loader.load_documents()
        nodes = embedding_generator.generate_nodes_from_documents(documents)
        storage_context = context_storage.get_storage_context(nodes)
        index_vector_store = vector_store_indexing.index_vector_store(nodes, storage_context)
    except Exception as e:
        logging.error(f"Error in document indexing flow: {str(e)}")

def chroma_document_indexing_flow():
    logging.info("Chroma document indexing flow")
    try:
        collections = [folder for folder in os.listdir(DATA_COLLECTION_PATH) if os.path.isdir(os.path.join(DATA_COLLECTION_PATH, folder))]
        for collection in collections:
            documents = data_loader.chroma_load_documents(collection)
            if IS_DOCKER:
                db = chromadb.HttpClient(host=CHROMA_DB_HOST, port=CHROMA_DB_PORT)
            else:
                db = chromadb.PersistentClient(path=CHROMA_PERSIST_DB)
            logging.info(f"Creating collection: {collection}")

            vector_store = ChromaVectorStore(chroma_collection=db.get_or_create_collection(collection))
            storage_context = context_storage.get_chroma_storage_context(vector_store)

            index_vector_store = vector_store_indexing.chroma_index_vector_store(
                documents, storage_context
            )
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
