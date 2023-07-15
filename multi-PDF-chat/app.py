import streamlit as st 
from dotenv import load_dotenv
from utils import get_pdf_text, get_text_chunks, get_vectorstore, get_conversation_chain
from htmlTemplates import css, bot_template, user_template

def main():
    load_dotenv()
    st.set_page_config(page_title='PrivateChat with Multiple PDFs💭', page_icon=":books:")
    
    st.write(css, unsafe_allow_html=True)
    
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    
    st.header("Chat with multiple PDFs :books:")
    st.text_input("Ask a question about your documents:")
    
    st.write(user_template.replace("{{MSG}}", "Hello, robot"), unsafe_allow_html=True)
    st.write(bot_template.replace("{{MSG}}", "Hello, human"), unsafe_allow_html=True)
    
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
                vectorestore = get_vectorstore(text_chunks)
                
                # Create conversation chain
                # Using `session_state` streamlit won't reinitialize the variable
                st.session_state.conversation = get_conversation_chain(vectorstore)
    
    
if __name__ == "__main__":
    main()