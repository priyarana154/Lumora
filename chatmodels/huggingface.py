import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")

if not token:
    raise ValueError("Hugging Face token .env file se load nahi hua!")

llm = HuggingFaceEndpoint(
repo_id="google/gemma-2-2b-it",
task="text-generation",
    max_new_tokens=128,
    temperature=0.7,
    huggingfacehub_api_token=token,
)

chat = ChatHuggingFace(llm=llm)

response = chat.invoke(
    "Give me an understandable low-level joke with emojis."
)

print(response.content)