from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

app = Flask(__name__)

# Enable CORS for all routes and specify allowed origins
CORS(app) #resources={r"/*": {"origins": "http://<127.0.0.1>:<3000>"}})

@app.route('/generate_story', methods=['POST'])
def generate_story():
    data = request.json
    vocab_list = data.get('vocab_list')
    language = data.get('language')
    topic = data.get('topic')
    level = data.get('level')
    length = data.get('length')

    story = generate_story(vocab_list, language, topic, level, length)
    return jsonify({"story": story})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

#comment comment
