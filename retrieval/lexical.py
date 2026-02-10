from rank_bm25 import BM25Okapi

class BM25Retriever:
    def __init__(self,documents):
        self.documents=documents
        tokenized_docs=[doc.lower().split() for doc in documents]
        self.bm25=BM25Okapi(tokenized_docs)

    def search(self,query,k=3):
        token_query=query.lower().split()
        scores=self.bm25.get_scores(token_query)
        # ---------------explanation neeeded
        ranked=sorted(zip(self.documents,scores),
        key=lambda x:x[1],
        reverse=True)
    
        return ranked[:k]