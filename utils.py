# app holding all holds all functions that required for the application

import openai
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.vectorstores import pinecone
from langchain.llms import OpenAI
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.schema import Document
import pinecone
from pypdf import PdfReader
from langchain.llms.openai import OpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain import HuggingFaceHub

# Extract Information from PDF file

def get_pdf_text(pdf_document):
    text = ""
    pdfreader = PdfReader(pdf_document)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text


# Iterate over files that are supposed to be uploaded

def create_docs(user_pdf_list, unique_id):
    docs=[]
    for filename in user_pdf_list:

        chunks=get_pdf_text(filename)

        # Appending data and adding metadata of the "filename"
        docs.append(Document(
            page_content=chunks,
            metadata={"name": filename.name, "id": filename.id,  "type=":filename.type, "size":filename.size, "unique_id":unique_id },
        ))
    return docs



print("Hello")