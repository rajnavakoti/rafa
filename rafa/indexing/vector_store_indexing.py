import os
import logging
from llama_index.core import VectorStoreIndex, load_index_from_storage, StorageContext
from llama_index.core.callbacks import CallbackManager
from dotenv import load_dotenv

# Initialize logger
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

IS_DOCKER = os.environ.get("IS_DOCKER")
PERSIST_DB = os.environ.get("DOCKER_PERSIST_DB") if IS_DOCKER else os.environ.get("LOCAL_PERSIST_DB")
EMBED_MODEL = os.environ.get("DOCKER_EMBED_MODEL") if IS_DOCKER else os.environ.get("LOCAL_EMBED_MODEL")

CALLBACK_MANAGER = CallbackManager()

def index_vector_store(nodes, storage_context):
    try:
        storage_context = StorageContext.from_defaults()
        storage_context.docstore.add_documents(nodes)
        index = VectorStoreIndex(nodes, embed_model=EMBED_MODEL, storage_context=storage_context,
                                 callback_manager=CALLBACK_MANAGER)
        index.storage_context.persist(persist_dir=PERSIST_DB)
        logger.info("Vector store indexing completed successfully.")
    except Exception as e:
        logger.error("Error occurred during vector store indexing: %s", str(e))

def chroma_index_vector_store(documents, storage_context):
    index = VectorStoreIndex.from_documents(
        documents, storage_context=storage_context, 
        embed_model=EMBED_MODEL)

def index_from_storage():
    try:
        logger.info("PERSIST_DB is: %s", PERSIST_DB)
        root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        logger.info("Root path: %s", root_path)
        vector_db_path = os.path.join(root_path, "vector_db")
        storage_context = StorageContext.from_defaults(persist_dir=vector_db_path)
        index = load_index_from_storage(embed_model=EMBED_MODEL, callback_manager=CALLBACK_MANAGER,
                                        storage_context=storage_context)
        logger.info("Index loaded from storage successfully.")
        return index
    except Exception as e:
        logger.error("Error occurred while loading index from storage: %s", str(e))
        return None
    
def index_from_chroma_storage(vector_store):
    index = VectorStoreIndex.from_vector_store(vector_store, embed_model=EMBED_MODEL)

    return index