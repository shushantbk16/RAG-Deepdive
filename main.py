from ingestion.loader import load_documents

# Testing Doc Loading

docs=load_documents("data/docs.txt")
# print(docs)



#Testing BM25

from retrieval.lexical import BM25Retriever

BM25=BM25Retriever(docs)
results=BM25.search("what is bm25")



from retrieval.semantic import SemanticRetriever

semantic = SemanticRetriever(docs)

results = semantic.search("how do vector databases work")




from retrieval.hybrid import HybridRetriever

hybrid = HybridRetriever(BM25, semantic)

results = hybrid.search("explain semantic retrieval")


