from llama_index.core import StorageContext

def get_storage_context(nodes):
    storage_context = StorageContext.from_defaults()
    storage_context.docstore.add_documents(nodes)
    return storage_context