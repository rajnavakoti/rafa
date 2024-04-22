import os
from llama_index.core import VectorStoreIndex, load_index_from_storage, StorageContext
from llama_index.core.callbacks import CallbackManager
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

PERSIST_DB = os.environ.get("PERSIST_DB")
EMBED_MODEL = os.environ.get("EMBED_MODEL")
CALLBACK_MANAGER = CallbackManager()

def index_vector_store(nodes, storage_context):
    storage_context = StorageContext.from_defaults()
    storage_context.docstore.add_documents(nodes)
    index = VectorStoreIndex(nodes, embed_model=EMBED_MODEL, storage_context=storage_context,
                             callback_manager=CALLBACK_MANAGER)
    index.storage_context.persist(persist_dir=PERSIST_DB)

def index_from_storage():
    print("PERSIST_DB is: ", PERSIST_DB)
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print("Root path:", root_path)
    vector_db_path = os.path.join(root_path, "vector_db")
    storage_context = StorageContext.from_defaults(persist_dir=vector_db_path)
    index = load_index_from_storage(embed_model=EMBED_MODEL, callback_manager=CALLBACK_MANAGER,
                                    storage_context=storage_context)
    return index