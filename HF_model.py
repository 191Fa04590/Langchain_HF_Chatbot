from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import os
load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id= "openai/gpt-oss-20b",
    task= "text-generation"
)
model = ChatHuggingFace(llm = llm)
result = model.invoke("Hello I am abhishek anand this is testing ,plese generate two philosphy's person name  from history")
print(result.content)