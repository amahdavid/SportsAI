from dotenv import load_dotenv
from llama_index.experimental import PandasQueryEngine
from prompts import new_prompt, instruction_str, context
from ai_actions import note_engine
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from llama_index.core import SimpleDirectoryReader


def setup_query_engine(directory_path):
    try:
        load_dotenv()

        reader = SimpleDirectoryReader(input_dir=directory_path)
        docs = reader.load_data()

        query_engine = PandasQueryEngine(df=None, verbose=True, instruction_str=instruction_str, documents=docs)
        query_engine.update_prompts({"": new_prompt})

        return query_engine
    except Exception as e:
        print(f"An error occurred while setting up the query engine: {e}")
        return None


def setup_tools(query_engine):
    try:
        tools = [
            note_engine,
            QueryEngineTool(query_engine=query_engine, metadata=ToolMetadata(
                name="sports_data",
                description="This gives information about the NBA AND FIFA"
            ))
        ]
        return tools
    except Exception as e:
        print(f"An error occurred while setting up tools: {e}")
        return None


def setup_agent(tools):
    try:
        llm = OpenAI(model="gpt-3.5-turbo-0613")
        agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)
        return agent
    except Exception as e:
        print(f"An error occurred while setting up the agent: {e}")
        return None


def setup_backup_tool():
    def backup_tool():
        return f"Sorry, I couldn't retrieve information for. Please try again later."

    return backup_tool
