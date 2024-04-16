from dotenv import load_dotenv
import os
import pandas as pd
from llama_index.experimental import PandasQueryEngine
from prompts import new_prompt, instruction_str

load_dotenv()

# Load the data
population_path = os.path.join("..", "data", "nba_data", "all_seasons.csv")
population_df = pd.read_csv(population_path)

# Create the query engine
population_query_engine = PandasQueryEngine(df=population_df, verbose=True, instruction_str=instruction_str)
population_query_engine.update_prompts({"": new_prompt})

