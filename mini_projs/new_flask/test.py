from config import llm
from model import gemini_response


response = gemini_response("You are a helpful assistant who provides concise and accurate answers", "What is the capital of India")

print(f"Capital: {response['capital']}")
print(f"Fact: {response['fact']}")