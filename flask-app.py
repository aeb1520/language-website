from flask import Flask, request, jsonify
from flask_cors import CORS
# change this to be language_model.py instead of the temp one; import real functions from it
from temporary_chatgpt_test import fancy_print  # Import your other file

app = Flask(__name__)
CORS(app) 


@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    text_value = data.get('text', '')
    print(f'Received text: {text_value}') # for debugging

    #calls function from other file I imported
    result_text = fancy_print(text_value) 

    #old line (from when just getting data from website but not sending any back:)
    #return jsonify({'status': 'success', 'received': text_value})

    #new line that returns (what will be) chatgpt stuff to the website
    return jsonify({'status': 'success', 'received': text_value, 'result': result_text})


if __name__ == '__main__':
    app.run(debug=True)


# extra comment so I can commit the changes