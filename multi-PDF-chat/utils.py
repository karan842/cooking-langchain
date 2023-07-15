import streamlit as st
from htmlTemplates import css, bot_template, user_template 
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

def get_pdf_text(pdfs):
    """Get text from muliple pdfs"""
    text = ""
    for pdf in pdfs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text
            
            
def get_text_chunks(text):
    """Divide the texts into chunks."""
    text_splitter = CharacterTextSplitter(
        separator="\n",
        # 1000 characters
        chunk_size=1000, 
        # Next chunk starts 200 chunks before to avoid overlapping of in complete text
        chunk_overlap=200,
    )
    chunks = text_splitter.split_text(text)
    return chunks
    
def get_vectorstore(chunks):
    # embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts=chunks, embedding=embeddings)
    return vectorstore


def get_conversation_chain(vectorstore):
    """Generate Conversation chains by taking history and returning new"""
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain


def handle_userinput(user_question):
    response = st.session_state.conversation({'question':user_question})
    st.session_state.chat_history = response['chat_history']
    
    for i, message in enumerate(st.session_state.chat_history):
        if i%2==0:
            st.write(user_template.replace("{{MSG}}",
                                           message.content),
                     unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}",
                                           message.content),
                     unsafe_allow_html=True)
            
    