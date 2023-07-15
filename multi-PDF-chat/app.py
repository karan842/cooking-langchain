import streamlit as st 
from dotenv import load_dotenv
from utils import (
    get_pdf_text, get_text_chunks, get_vectorstore, 
    get_conversation_chain, handle_userinput
)
from htmlTemplates import css, bot_template, user_template

def main():
    load_dotenv()
    st.set_page_config(page_title='PrivateGPT', page_icon=":rocket:")
    
    st.write(css, unsafe_allow_html=True)
    
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    
    st.header("Private GPT - Chat with PDFs :books:")
    st.warning("Please upload documents and process first! Then ask questions")
    user_question = st.text_input("Ask a question about your documents:")
    if user_question:
        handle_userinput(user_question)
 
    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader("Upload your PDFs here and click on Process", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing :hourglass:"):
                
                # get the PDF text
                raw_text = get_pdf_text(pdf_docs)
                
                # get the text chunks
                text_chunks = get_text_chunks(raw_text)
                
                # Create vector store 
                vectorstore = get_vectorstore(text_chunks)
                
                # Create conversation chain
                # Using `session_state` streamlit won't reinitialize the variable
                st.session_state.conversation = get_conversation_chain(vectorstore)
    
    
if __name__ == "__main__":
    main()