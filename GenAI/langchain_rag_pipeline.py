from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

 

pdf = PyPDFLoader("<pdf>")

pdfpages = pdf.load_and_split()

 

from langchain.text_splitter import CharacterTextSplitter

from langchain_community.vectorstores import FAISS

from langchain_openai.embeddings import OpenAIEmbeddings

import os

from langchain_openai import OpenAI

 

os.environ["OPENAI_API_KEY"]=api_key

 

mybooks = pdf.load()

text_splitter = CharacterTextSplitter(chunk_size=1500,chunk_overlap=0)

split_text = text_splitter.split_documents(mybooks)

 

embeddings = OpenAIEmbeddings()

vectorstore = FAISS.from_documents(split_text,embeddings)

 

vectorstore_retriever = vectorstore.as_retriever()

 

from langchain.agents.agent_toolkits import create_retriever_tool

 

tool = create_retriever_tool(

vectorstore_retriever,

"Atomic_Habits_Chapter_Search",

"Retrieve detailed information on the chapters of the book 'Atomic habits' by James Clear."

)

 

tools = [tool]

 

from langchain.agents.agent_toolkits import create_conversational_retrieval_agent

from langchain_openai.chat_models import ChatOpenAI

 

llm = ChatOpenAI(temperature=0,model_name='gpt-3.5-turbo")

myagent = create_conversational_retrieval_agent(llm,tools,verbose=True)

 

context = "The user is conducting resesarch on book 'Atomic habits' by James Clear for a literature review"

question = "What are the three laws there in this book explain all laws in detail in 250 words"

 

prompt = f""" you need to answer the question in the sentence as same as in the pdf content. Given below is the context and question of the user.

context= {context}

question={question}

 

"""

 

result = myagent.invoke({"input":prompt})
