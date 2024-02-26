import numpy as np

def save_embeddings(embeddings, filename):
    np.save(filename, embeddings)

def load_embeddings(filename):
    return np.load(filename)

def search_embeddings(query_embedding, embeddings):
    distances = np.linalg.norm(embeddings - query_embedding, axis=1)
    closest_index = np.argmin(distances)
    return closest_index