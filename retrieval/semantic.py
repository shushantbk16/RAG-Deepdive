from sentence_transformers import SentenceTransformer
import chromadb

class SemanticRetriever:
    def __init__(self, documents):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        self.client = chromadb.Client()
        self.collection = self.client.create_collection("docs")

        embeddings = self.model.encode(documents).tolist()

        for i, doc in enumerate(documents):
            self.collection.add(
                documents=[doc],
                embeddings=[embeddings[i]],
                ids=[str(i)]
            )

    def search(self, query, k=3):
        query_embedding = self.model.encode(query).tolist()

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=k
        )

        return results["documents"][0]
