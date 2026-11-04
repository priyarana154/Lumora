
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

model = init_chat_model("groq:openai/gpt-oss-120b", temperature=0.7, max_tokens=512)
response = model.invoke("give me understanable low level joke with emojies")
print("bot :" + response.content)
