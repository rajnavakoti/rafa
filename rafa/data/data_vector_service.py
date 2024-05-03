import os
from rafa.data_load import data_loader
from rafa.embedding import embedding_generator
from rafa.storage import context_storage
from rafa.indexing import vector_store_indexing
from llama_index.llms.ollama import Ollama
from llama_index.vector_stores.chroma import ChromaVectorStore
import chromadb
from llama_index.core import StorageContext
from dotenv import load_dotenv

load_dotenv()
IS_DOCKER = os.environ.get("IS_DOCKER")
DATA_COLLECTION_PATH = os.environ.get("DOCKER_DATA_DIR") if IS_DOCKER else os.environ.get("LOCAL_DATA_DIR")
CHROMA_PERSIST_DB = os.environ.get("DOCKER_CHROMA_PERSIST_DB") if IS_DOCKER else os.environ.get("LOCAL_CHROMA_PERSIST_DB")

def test_func():
    collection_names = [folder for folder in os.listdir(DATA_COLLECTION_PATH) if os.path.isdir(os.path.join(DATA_COLLECTION_PATH, folder))]
    print("Folder names under data/collections:")
    for folder_name in collection_names:
        print(folder_name)

def document_indexing_flow():
    documents = data_loader.load_documents()
    nodes = embedding_generator.generate_nodes_from_documents(documents)
    storage_context = context_storage.get_storage_context(nodes)
    index_vector_store = vector_store_indexing.index_vector_store(nodes, storage_context)

def chroma_document_indexing_flow():
    collections = [folder for folder in os.listdir(DATA_COLLECTION_PATH) if os.path.isdir(os.path.join(DATA_COLLECTION_PATH, folder))]
    db = chromadb.PersistentClient(path=CHROMA_PERSIST_DB)

    for collection_name in collections:
        documents = data_loader.chroma_load_documents(collection_name)       
        collection = db.get_or_create_collection(collection_name)
        vector_store = ChromaVectorStore(chroma_collection=collection)
        storage_context = context_storage.get_chroma_storage_context(vector_store)
        vector_store_indexing.chroma_index_vector_store(documents, storage_context)

if __name__ == "__main__":
    test_func()
    document_indexing_flow()
    chroma_document_indexing_flow()
