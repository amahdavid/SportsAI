from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from setup import setup_query_engine, setup_tools, setup_agent, setup_backup_tool

app = Flask(__name__)
CORS(app)

query_engine = setup_query_engine("../data")
tools = setup_tools(query_engine)
agent = setup_agent(tools)
backup_tool = setup_backup_tool()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/query', methods=['POST'])
def query():
    try:
        prompt = request.json.get('prompt')
        result = agent.query(prompt)
        response = result.response
        print(response)
        return jsonify({'result': response}), 200
    except Exception as e:
        print("An error occurred:", e)
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=8000)
