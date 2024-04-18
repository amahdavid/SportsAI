# Overview
This is a simple AI tool that helps to answer questions about sports such as basketball and soccer. 
By developing this I gained hands-on experience in AI, some machine learning techniques and data analysis
# Feature(s)
- Querying the AI with sports related questions and maybe some car questions
# Demo
![landing page.png](landing%20page.png)
# Setup
- IDE of choice, I used Pycharm and VsCode
- Installing necessary libraries and tools
- Setting up an OpenAI API key
- Setting up GitHub repo for version control
- 
### installing libraries
- **command**: pip3 install llama-index pypdf python-dotenv pandas
- **pandas**: for reading csv files
- **pypdf**: for pdf files
- **llama**-**index**: for setting up the whole agent
- **python**-**dotenv**: for loading into environment variable files
- Had to install this library to update prompts: pip install llama-index-experimental

### Downloading Data Source
Get your Data set of choice, you can download as much as you feel like
- NBA Wikipedia: https://en.wikipedia.org/wiki/National_Basketball_Association
- NBA dataset Kaggle: https://www.kaggle.com/datasets/justinas/nba-players-data

### Open API keys
- go to https://platform.openai.com/api-keys
- You may have to pay for credit if you have an OpenAI your account for over 3 months
- create your API key and it to your .env file

# Notes
- to create virtual env use "python3 -m venv ai" 
- to activate use "source .venv/bin/activate"
- to deactivate use "deactivate"
- some libraries have had changes use "llama_index.experimental" instead of "llama_index.query_engine"
- you can also just add the unresolved attribute and there may be a note with an update
- Llama index docs: https://docs.llamaindex.ai/en/stable/
- Llama index has a nice tool for reading data in one go which is called SimpleDirectoryReader
- If you are testing your application and do not have an endpoint for your landing page do not use live server, it resets
the window anytime there are changes
- Have CORS enabled if you will be making cross region request