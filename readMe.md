# Setup
### installing libraries
- **command**: pip3 install llama-index pypdf python-dotenv pandas
- **pandas**: for reading csv files
- **pypdf**: for pdf files
- **llama**-**index**: for setting up the whole agent
- **python**-**dotenv**: for loading into environment variable files
- Had to install this library to update prompts: pip install llama-index-experimental

### Downloading Data Source
Get your Data set of choice
- NBA Wikipedia: https://en.wikipedia.org/wiki/National_Basketball_Association
- NBA dataset Kaggle: https://www.kaggle.com/datasets/justinas/nba-players-data

### Open API keys
- go to https://platform.openai.com/api-keys
- create your API key and it to your .env file

# Notes
- to create virtual env use "python3 -m venv ai" 
- to activate use "source .venv/bin/activate"
- to deactivate use "deactivate"
- some libraries have had changes use "llama_index.experimental" instead of "llama_index.query_engine"
- you can also just add the unresolved attribute and there may be a note with an update