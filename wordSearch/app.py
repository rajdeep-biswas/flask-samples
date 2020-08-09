from flask import Flask, render_template, request

wordSearch = Flask(__name__)
WORDS = []
with open("words.txt", "r") as file:
			for word in file.readlines():
				WORDS.append(word.rstrip())

@wordSearch.route('/')
def home():
	return render_template("home.html")

@wordSearch.route('/search')
def results():
	foundWords = []
	count = 0
	searchedWord = request.args.get("word")

	# foundWords = [word for word in WORDS if word.startswith(request.args.get("word"))]

	for word in WORDS:
		if searchedWord == word[0:len(searchedWord)].lower():
			foundWords.append(word)
			count += 1
	return render_template("display.html", count=count, WORDS=foundWords)