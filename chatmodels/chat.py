
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

model = init_chat_model("groq:openai/gpt-oss-120b", temperature=0.7, max_tokens=512)

print("--------what's on your mind today?--------")
print("Note - Type '0' to quit the chat.")

messages = [
    SystemMessage(content="You are a rude assistant."),
]

while True :

  prompt = input("Priya:")
  
  if prompt == "0":
    break
  messages.append(HumanMessage(content=prompt))
  response = model.invoke(messages)
  messages.append(AIMessage(content=response.content))
  print("bot :" + response.content)
