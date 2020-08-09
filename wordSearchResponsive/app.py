from flask import Flask, render_template, request

wordSearch = Flask(__name__)

WORDS = []
with open("words.txt", "r") as file:
	for line in file.readlines():
		WORDS.append(line.rstrip())

@wordSearch.route('/')
def home():
	return render_template("home.html")

# I completely don't intuitively understand yet how they optimized this
# (and where my implementation wasn't so)

@wordSearch.route('/search')
def results():
	q = request.args.get("q")
	words = [word for word in WORDS if q and word.startswith(q)]
	return render_template("display.html", words=words)