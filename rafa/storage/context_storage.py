from llama_index.core import StorageContext

def get_storage_context(nodes):
    return StorageContext.from_defaults().docstore.add_documents(nodes)
