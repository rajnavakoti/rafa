import os
import logging
from llama_index.core import VectorStoreIndex, load_index_from_storage, StorageContext
from llama_index.core.callbacks import CallbackManager
import chromadb
from llama_index.vector_stores.chroma import ChromaVectorStore
from dotenv import load_dotenv

# Initialize logger
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

IS_DOCKER = os.environ.get("IS_DOCKER")
PERSIST_DB = os.environ.get("DOCKER_PERSIST_DB") if IS_DOCKER else os.environ.get("LOCAL_PERSIST_DB")
CHROMA_PERIST_DB = os.environ.get("DOCKER_CHROMA_PERSIST_DB") if IS_DOCKER else os.environ.get("LOCAL_CHROMA_PERSIST_DB")
EMBED_MODEL = os.environ.get("DOCKER_EMBED_MODEL") if IS_DOCKER else os.environ.get("LOCAL_EMBED_MODEL")

CALLBACK_MANAGER = CallbackManager()

def index_vector_store(nodes, storage_context):
    """
    Indexes a vector store by adding documents to the document store and creating an index.

    Args:
        nodes (list): List of nodes to be added to the vector store.
        storage_context (StorageContext): The storage context for the vector store.

    Returns:
        None

    Raises:
        Exception: If an error occurs during vector store indexing.

    """
    try:
        # Create a default storage context if not provided
        storage_context = StorageContext.from_defaults()

        # Add documents to the document store
        storage_context.docstore.add_documents(nodes)

        # Create a vector store index
        index = VectorStoreIndex(nodes, embed_model=EMBED_MODEL, storage_context=storage_context,
                                 callback_manager=CALLBACK_MANAGER)

        # Persist the storage context
        index.storage_context.persist(persist_dir=PERSIST_DB)

        logger.info("Vector store indexing completed successfully.")
    except Exception as e:
        logger.error("Error occurred during vector store indexing: %s", str(e))

def chroma_index_vector_store(documents, storage_context):
    """
    Indexes the given documents using a vector store.

    Args:
        documents (list): A list of documents to be indexed.
        storage_context: The storage context for the vector store.

    Returns:
        None
    """
    # Create a VectorStoreIndex object from the given documents
    index = VectorStoreIndex.from_documents(
        documents, storage_context=storage_context, 
        embed_model=EMBED_MODEL)

def index_from_storage():
    """
    Loads the index from storage.

    Returns:
        index: The loaded index object.
            Returns None if an error occurs while loading the index.
    """
    try:
        # Log the value of PERSIST_DB
        logger.info("PERSIST_DB is: %s", PERSIST_DB)

        # Get the root path of the project
        root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        logger.info("Root path: %s", root_path)

        # Create the path to the vector_db directory
        vector_db_path = os.path.join(root_path, "vector_db")

        # Create a storage context with the vector_db_path
        storage_context = StorageContext.from_defaults(persist_dir=vector_db_path)

        # Load the index from storage using the specified embed_model, callback_manager, and storage_context
        index = load_index_from_storage(embed_model=EMBED_MODEL, callback_manager=CALLBACK_MANAGER,
                                        storage_context=storage_context)

        # Log a success message
        logger.info("Index loaded from storage successfully.")

        # Return the loaded index
        return index
    except Exception as e:
        # Log an error message if an exception occurs
        logger.error("Error occurred while loading index from storage: %s", str(e))
        return None
    
def index_from_chroma_storage():
    """
    Indexes vectors from a chroma storage.

    Args:
        vector_store: The vector store containing the vectors to be indexed.

    Returns:
        index: The indexed vectors.

    """
    # Create an instance of VectorStoreIndex using the vector_store and EMBED_MODEL
    db = chromadb.PersistentClient(path=CHROMA_PERIST_DB)
    print(db.list_collections())
    chroma_collection = db.get_collection("allen")
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    index = VectorStoreIndex.from_vector_store(vector_store, embed_model=EMBED_MODEL)

    return index