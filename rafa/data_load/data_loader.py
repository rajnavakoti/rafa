import os
from dotenv import load_dotenv

from llama_index.core import SimpleDirectoryReader

# Load environment variables from .env file
load_dotenv()

PERSIST_DB = os.environ.get("PERSIST_DB")
input_dir = os.environ.get("INPUT_DIR")
required_exts = os.environ.get("REQUIRED_EXTS")

def load_documents():
    if not os.path.exists(PERSIST_DB):
        documents = SimpleDirectoryReader(input_dir=input_dir, recursive=True,
                                          required_exts=required_exts).load_data()
        
        return documents
    else:
        return []

documents = load_documents()
