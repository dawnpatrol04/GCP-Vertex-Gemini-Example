from langchain.sql_database import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from google.auth import load_credentials_from_file
from google.cloud import aiplatform




from langchain_google_vertexai import VertexAI
from dotenv import load_dotenv , find_dotenv
import os

load_dotenv(find_dotenv())


# prnt env var called  GOOGLE_APPLICATION_CREDENTIALS
print("GOOGLE_APPLICATION_CREDENTIALS: ", os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))

gemini_model = VertexAI(model_name="gemini-pro")

 
# Initialize database connection
db = SQLDatabase.from_uri("sqlite:///Chinook.db")

 
# Create SQL agent using the Langchain AI Platform model integration
agent_executor = create_sql_agent(llm=gemini_model, db=db , verbose=True)

# agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
 


def main():
    query = "List the popular products"
    response = agent_executor.invoke(query)
    print(response)

if __name__ == "__main__":
    main()
