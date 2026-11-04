
import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

st.set_page_config(page_title="AI Chatbot", page_icon="💬")

# Simple professional CSS
st.markdown("""
<style>
.stApp {
    background-color: #f8fafc;
}

.block-container {
    max-width: 800px;
    padding-top: 40px;
}

.title {
    text-align: center;
    color: #4f46e5;
    font-size: 35px;
    font-weight: 700;
}

.subtitle {
    text-align: center;
    color: #64748b;
    margin-bottom: 30px;
}

[data-testid="stChatMessage"] {
    background-color: black;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 12px;
}

[data-testid="stChatInput"] {
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

# UI Heading
st.markdown('<div class="title">AI Chat Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Your personal AI assistant powered by Groq</div>', unsafe_allow_html=True)

load_dotenv()

model = init_chat_model("groq:openai/gpt-oss-120b", temperature=0.7, max_tokens=512)

if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a helpfull assistant.")
    ]

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display previous messages
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
prompt = st.chat_input("What's on your mind today?")

if prompt:
    if prompt == "0":
        st.stop()

    st.session_state.chat_history.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    messages = st.session_state.messages
    messages.append(HumanMessage(content=prompt))

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = model.invoke(messages)
            st.markdown(response.content)

    messages.append(AIMessage(content=response.content))

    st.session_state.chat_history.append({
        "role": "assistant",
        "content": response.content
    })
