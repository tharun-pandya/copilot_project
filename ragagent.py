
from langchain import hub
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv("api_key.env")

import google.generativeai as genai
import os

class RAGagent:
    def __init__(self,file_path):
        loader = PyPDFLoader(file_path)
        docs = loader.load_and_split()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=200, add_start_index=True
        )
        all_splits = text_splitter.split_documents(docs)

        vectorstore = Chroma.from_documents(documents=all_splits, embedding=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"))
        self.retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 6})

    def format_docs(self,docs):
        return "\n\n".join(doc.page_content for doc in docs)
    
    def get_answer(self,question):
              
        
        retrieved_docs = self.retriever.invoke(question)

        template = """Use the following pieces of context to answer the question at the end.
        If you don't know the answer, just say that you don't know, don't try to make up an answer.
        Use three sentences maximum and keep the answer as concise as possible.
        Always say "thanks for asking!" at the end of the answer.

        {context}

        Question: {question}

        Helpful Answer:"""
        custom_rag_prompt = PromptTemplate.from_template(template)

        os.environ["GOOGLE_API_KEY"]=os.getenv("GEMINI_API_KEY")
        llm = GoogleGenerativeAI(model="gemini-pro")

        rag_chain = (
            {"context": self.retriever | self.format_docs, "question": RunnablePassthrough()}
            | custom_rag_prompt
            | llm
            | StrOutputParser()
        )

        result=rag_chain.invoke(question)
        return result





