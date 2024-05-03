import os
import logging
from dotenv import load_dotenv
from llama_index.core.node_parser import SimpleNodeParser

# Load environment variables from .env file
load_dotenv()

IS_DOCKER = os.environ.get("IS_DOCKER")
CHUNK_SIZE = os.environ.get("DOCKER_CHUNK_SIZE") if IS_DOCKER else os.environ.get("LOCAL_CHUNK_SIZE")
CHUNK_OVERLAP = os.environ.get("DOCKER_CHUNK_OVERLAP") if IS_DOCKER else os.environ.get("LOCAL_CHUNK_OVERLAP")

def generate_nodes_from_documents(documents):
    try:
        chunk_size = int(CHUNK_SIZE)
        chunk_overlap = int(CHUNK_OVERLAP)

        logging.info(f"Chunk Size: {chunk_size}")
        logging.info(f"Chunk Overlap: {chunk_overlap}")

        nodes = SimpleNodeParser(chunk_size=chunk_size, chunk_overlap=chunk_overlap).get_nodes_from_documents(documents)
        return nodes
    except (ValueError, TypeError) as e:
        logging.error(f"Error while generating nodes from documents: {e}")
        return None