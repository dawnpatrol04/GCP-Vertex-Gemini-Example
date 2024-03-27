
from langchain.prompts import PromptTemplate  # Updated import
from langchain.chains import LLMChain  # Updated import
from langchain.memory import ConversationBufferMemory
from langchain.agents import Tool, AgentType , tool
from langchain_google_vertexai import VertexAI  
import os
from dotenv import load_dotenv, find_dotenv
import streamlit as st


load_dotenv(find_dotenv())
os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

def get_word_length(word: str) -> int:
    """Returns the length of a word."""
    return len(word)

@st.cache_resource(show_spinner=False)
def LLM_init():
    # Initialization code here...

    tools = [
        Tool(
            name="getlength",
            func=get_word_length,
            description="Return the length of a word"
        ),
    ]

    memory = ConversationBufferMemory(memory_key="chat_history")
    
    # Updated agent initialization using new constructor methods
    llm_chain = LLMChain(
        tools=tools,
        llm=VertexAI(model_name="gemini-pro"),  # Using the updated VertexAI class from langchain-google-vertexai
        memory=memory,
        # agent_type=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,  # Assuming this is the correct parameter name; adjust if needed
        verbose=True,
        prompt=PromptTemplate(
            prompt="Hi my name is Melali and I am your travel consultant, how can I help you?"
        )
    )
    
    return llm_chain



st.set_page_config(page_title="🦜🔗 Demo App")
st.title('🦜🔗 Demo App')

st.title("💬 Travel Assistant")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hi my name is Melali and I am your travel consultant, how can I help you?"}]

#"st.session_state:", st.session_state.messages

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    # with st.spinner('Preparing'):
    llm_chain = LLM_init()
    msg = llm_chain(prompt)

    #st.write(msg)
    #st.write(len(msg))
    #st.write(type(msg))

    st.session_state.messages.append({"role": "assistant", "content": msg["output"]})
    st.chat_message("assistant").write(msg["output"])




# streamlit run chat-agent.py  --server.port=8085  --server.address=0.0.0.0  --server.enableCORS=false