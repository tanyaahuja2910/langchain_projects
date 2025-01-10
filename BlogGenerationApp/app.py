import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_ollama import OllamaLLM


## function to get response from llama3.2
def getLlamaResponse(topic,words, blog_style):

    ## Llama model
    llm = OllamaLLM(model="llama3.2")

    ## Prompt Template
    template = "Write a blog for {blog_style} job profile on the topic {topic} in maximum {words} words"

    prompt = PromptTemplate(input_variables=['blog_style', 'topic', 'words'],
                            template = template)


    ## Generate reponse from llm
    response = llm(prompt.format(blog_style=blog_style, topic = topic, words = words))
    return response



st.set_page_config(
    page_title="Generate Blogs",
    layout='centered',
    initial_sidebar_state='collapsed'
)

st.header("Generate Blogs")

text_input = st.text_input("Enter your topic")


## adding 2 columns for additional input fields
col1, col2 = st.columns([5,5]) ## giving width of columns

with col1:
    words = st.text_input("Number of words")

with col2:
    blog_style = st.selectbox("Select blog writing style", ("Researchers", "Data science enthusiasts", "Common people"), index=0)

submit  = st.button("Generate Blog")


## Execute on submit
if submit:
    st.write(getLlamaResponse(text_input,words, blog_style))