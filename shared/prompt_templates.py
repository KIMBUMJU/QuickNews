from langchain_core.prompts import ChatPromptTemplate

prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Summarize the following article in Korean Language. Present the key points in 4-5 sentences, numbered as 1, 2, 3, etc.:\\n\\n{context}",
        ),
    ]
)


