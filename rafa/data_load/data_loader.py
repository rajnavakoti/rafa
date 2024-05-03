import os
import logging
from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader

# Load environment variables from .env file
load_dotenv()

IS_DOCKER = os.environ.get("IS_DOCKER")
PERSIST_DB = os.environ.get("DOCKER_PERSIST_DB") if IS_DOCKER else os.environ.get("LOCAL_PERSIST_DB")
INPUT_DIR = os.environ.get("DOCKER_DATA_DIR") if IS_DOCKER else os.environ.get("LOCAL_DATA_DIR")
REQUIRED_EXTS = os.environ.get("DOCKER_REQUIRED_EXTS") if IS_DOCKER else os.environ.get("LOCAL_REQUIRED_EXTS")
CHROMA_PERSIST_DB = os.environ.get("DOCKER_CHROMA_PERSIST_DB") if IS_DOCKER else os.environ.get("LOCAL_CHROMA_PERSIST_DB")


def load_documents():
    try:
        if not os.path.exists(PERSIST_DB):
            documents = SimpleDirectoryReader(input_dir=INPUT_DIR, recursive=True,
                                              required_exts=REQUIRED_EXTS).load_data()
            return documents
        else:
            return []
    except Exception as e:
        logging.error(f"Error occurred while loading documents: {str(e)}")
        return []
    
def chroma_load_documents(collection_name):
    collection_dir = os.path.join(INPUT_DIR, collection_name)
    
    if not os.path.exists(CHROMA_PERSIST_DB):
        documents = SimpleDirectoryReader(input_dir=collection_dir, recursive=True,
                                          required_exts=REQUIRED_EXTS).load_data()
        
        return documents
    else:
        return []

documents = load_documents()
