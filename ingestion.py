from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

import os

load_dotenv()

# if __name__ == "__main__":
#     print("loading...")
#     loader = TextLoader(r"C:\Users\bisig\Documents\Udemy\Learn AI Engineering with LangChain and LangGraph\langchain-course\mediumblog.txt", encoding='UTF-8')
#     document = loader.load()

#     print("splitting...")
#     text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
#     texts = text_splitter.split_documents(document)
#     print(f"created {len(texts)} chunks")

#     embeddings = OpenAIEmbeddings(openai_api_key=os.environ["OPENAI_API_KEY"])

#     print("ingesting...")
#     PineconeVectorStore.from_documents(texts, embeddings, index_name=os.environ["INDEX_NAME"])
#     print("finish")