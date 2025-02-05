from newspaper import Article
from langchain_core.documents import Document

url = 'https://www.hankyung.com/article/2024121731241'
article = Article(url)
article.download()
article.parse()

# print(article.html)
# print(article.text)

document = Document(
    page_content=article.text,
    metadata={"source": url}
)

# print(document)
