from flask import Flask, jsonify
app = Flask(__name__)
import requests

@app.route('/<word>', methods = ['GET', 'POST'])
def home(word):
	URL = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
	res = requests.get(URL)
	return jsonify(res.json())

@app.route('/', methods = ['GET'])
def disp():

	return jsonify({'data': 'Welcome to dictionary'})


if __name__ == '__main__':
	app.run(debug = True)
