from llama_index.core import StorageContext

def get_storage_context(nodes):
    return StorageContext.from_defaults().docstore.add_documents(nodes)

def get_chroma_storage_context(vector_store):
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    return storage_context