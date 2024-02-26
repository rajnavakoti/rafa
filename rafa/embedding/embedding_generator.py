import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from llama_index.core.node_parser import SimpleNodeParser

def generate_nodes_from_documents(documents):
    chunk_size = int(os.getenv("CHUNK_SIZE"))
    chunk_overlap = int(os.getenv("CHUNK_OVERLAP"))

    parser = SimpleNodeParser(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    nodes = parser.get_nodes_from_documents(documents)
    
    return nodes