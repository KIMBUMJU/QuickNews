from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_openai import ChatOpenAI
from langchain_core.documents import Document
from app.shared.prompt_templates import prompt_template
from testfiles.article_extract import document

# LangChain 초기화
model = ChatOpenAI(model="gpt-4o")

chain = create_stuff_documents_chain(model, prompt_template)

#Define the function that calls the model
def summarize_article(docs: Document):
    docs = [docs]
    result = chain.invoke({"context": docs})
    return {"result": result}

summary = summarize_article(document)
print(summary)

