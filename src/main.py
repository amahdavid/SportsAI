from dotenv import load_dotenv
import os
import pandas as pd
from llama_index.experimental import PandasQueryEngine
from prompts import new_prompt, instruction_str, context
from note_engine import note_engine
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI

load_dotenv()

# Load the data
nba_path = os.path.join("..", "data", "nba_data", "all_seasons.csv")
nba_df = pd.read_csv(nba_path)

fifa_path = os.path.join("..", "data", "fifa_data", "wc_matches.csv")
fifa_df = pd.read_csv(fifa_path)

# Create the query engine
nba_query_engine = PandasQueryEngine(df=nba_df, verbose=True, instruction_str=instruction_str)
nba_query_engine.update_prompts({"": new_prompt})

fifa_query_engine = PandasQueryEngine(df=fifa_df, verbose=True, instruction_str=instruction_str)
fifa_query_engine.update_prompts({"": new_prompt})

# specifying diff tools we have access to

tools = [
    note_engine,
    QueryEngineTool(query_engine=nba_query_engine, metadata=ToolMetadata(
        name="nba_data",
        description="This gives information about the NBA"
    )),
    QueryEngineTool(query_engine=nba_query_engine, metadata=ToolMetadata(
        name="fifa_data",
        description="This gives information about the FIFA WC 2022"
    ))
]

llm = OpenAI(model="gpt-3.5-turbo-0613")
agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)

