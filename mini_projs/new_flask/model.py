from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from config import llm
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field

#setting up template

gemini_template = ChatPromptTemplate.from_messages([
    ("system", "{system_prompt}\n\nYou must respond ONLY in the JSON format specified.\n{format_instructions}"),  # The system message sets the context and instructions for the AI
    ("human", "{user_prompt}"),     # The human message is the user's direct question or prompt
])

#Parsing the output
class AIResponse(BaseModel):
    capital: str = Field(description="The name of the capital city")
    fact: str = Field(description="A cool and interesting fact about the capital")

json_parser = JsonOutputParser(pydantic_object=AIResponse)

#getting responses

def get_ai_response(model, template, system_prompt, user_prompt):
    chain = template | model |json_parser
    return chain.invoke(
        {
        'system_prompt':system_prompt,
        'user_prompt':user_prompt,
        'format_instructions': json_parser.get_format_instructions()
        }
        )

def gemini_response(system_prompt, user_prompt):
    return get_ai_response(llm, gemini_template,system_prompt,user_prompt)

