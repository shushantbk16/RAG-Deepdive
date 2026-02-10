class HybridRetriever:
    def __init__(self, bm25, semantic):
        self.bm25 = bm25
        self.semantic = semantic

    def search(self, query, k=3):
        bm25_results = self.bm25.search(query, k)
        semantic_results = self.semantic.search(query, k)

        bm25_docs = {doc for doc, _ in bm25_results}
        semantic_docs = set(semantic_results)

        combined = list(bm25_docs.union(semantic_docs))
        print(combined)
        return combined[:k]
