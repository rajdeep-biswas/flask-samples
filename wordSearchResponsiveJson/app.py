from flask import Flask, jsonify, render_template, request

wordSearch = Flask(__name__)

WORDS = []
with open("words.txt", "r") as file:
	for line in file.readlines():
		WORDS.append(line.rstrip())

@wordSearch.route('/')
def home():
	return render_template("home.html")

# here we use JSON to send all the words to the browser and let's the latter deal with the former
@wordSearch.route('/search')
def results():
	q = request.args.get("q")
	words = [word for word in WORDS if q and word.startswith(q)]
	return jsonify(words)