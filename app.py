import streamlit as st
# from langchain_openai.chat_models import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

st.title("🦜🔗 Quickstart App")

# openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")
googleai_api_key = st.sidebar.text_input("Google AI API Key", type="password")

def generate_response(input_text):
    # model = ChatOpenAI(temperature=0.7, api_key=openai_api_key)
    model = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.7, api_key=googleai_api_key)
    st.info(model.invoke(input_text))


with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "What are the three key pieces of advice for learning how to code?",
    )
    submitted = st.form_submit_button("Submit")
    if not googleai_api_key.startswith("AI"):
        st.warning("Please enter your Google AI API key!", icon="⚠")
    if submitted and googleai_api_key.startswith("AI"):
        generate_response(text)


