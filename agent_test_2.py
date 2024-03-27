from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.agents import Tool
from langchain_google_vertexai import VertexAI  
from dotenv import load_dotenv
from langchain.memory import ConversationBufferMemory
from langchain.agents import Tool, AgentType , tool
from langchain_core.prompts import PromptTemplate
load_dotenv()

# Direct instantiation of llm_chain
memory = ConversationBufferMemory(memory_key="chat_history")
tools = [
    Tool(
        name="getlength",
        func=lambda word: len(word),
        description="Return the length of a word"
    ),
]
    # Updated agent initialization using new constructor methods
llm_chain = LLMChain(
    tools=tools,
    llm=VertexAI(model_name="gemini-pro"),  # Using the updated VertexAI class
    memory=memory,
    verbose=True,
    prompt_template = PromptTemplate(prompt="Hi my name is Melali and I am your travel consultant, how can I help you?")

)

def chat_interaction(prompt):
    # Using the directly instantiated llm_chain to process the prompt
    msg = llm_chain(prompt)
    # Print the assistant's response for verification
    print("Assistant:", msg["output"])

# Example usage to test and print results
chat_interaction("Could you help me find a flight to New York?")
