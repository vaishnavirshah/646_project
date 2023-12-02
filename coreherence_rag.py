from langchain.chat_models import ChatCohere
from langchain.retrievers import CohereRagRetriever
from langchain.schema.document import Document
from preparing_ds import data

content = []

for i in range(len(data[0]['profile'])):
    content.append(data[0]['profile'][i]['text'])

documents = [Document(page_content=text) for text in content]

rag = CohereRagRetriever(llm=ChatCohere())

query = (data[0]['input'])
index_of_query= (data[0]['input']).find("article:")

query = (data[0]['input'])[index_of_query + len("article:"):].strip()

docs = rag.get_relevant_documents(
    query,
    source_documents=documents
)

def _pretty_print(docs):
    for doc in docs:
        print(doc.metadata)
        print("\n\n" + doc.page_content)
        print("\n\n" + "-" * 30 + "\n\n")

_pretty_print(docs)
