from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import os
load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id= "openai/gpt-oss-20b",
    task= "text-generation"
)
model = ChatHuggingFace(llm = llm)
while True:
    user_input = input("Enter your query")
    if user_input.lower() !="exit":        
        result = model.invoke(user_input)
        print(result.content)
    else:
        break
    