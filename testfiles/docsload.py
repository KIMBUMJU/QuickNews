from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://www.hankyung.com/article/2024121731241")
docs = loader.load()

print(docs)

