def load_documents(path:str):
    with open(path,"r") as f:
        docs=f.read().split("\n\n")
    return docs
