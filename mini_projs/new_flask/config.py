from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
llm = ChatGoogleGenerativeAI(
    model = 'gemini-1.5-flash-latest',
    temperature=0.2,
    max_output_tokens=70,
    max_input_tokens=40
)

