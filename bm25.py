from langchain.schema import Document
from preparing_ds import data
from langchain.retrievers import BM25Retriever

content = []

for i in range(len(data[0]['profile'])):
    content.append(data[0]['profile'][i]['text'])

documents = [Document(page_content=text) for text in content]

retriever = BM25Retriever.from_documents(documents)

query = (data[0]['input'])
index_of_query= (data[0]['input']).find("article:")

query = (data[0]['input'])[index_of_query + len("article:"):].strip()

result = retriever.get_relevant_documents(query)

for i in range(len(content)):
    print(content[i])
    print("---------")

print("*************************")

for i in range(len(result)):
    print(result[i])
    print("---------")