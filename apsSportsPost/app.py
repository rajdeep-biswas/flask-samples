from flask import Flask, render_template, request

sports = Flask(__name__)

@sports.route('/')
def home():
	return render_template("home.html")

# using base url for post data, can alternatively use extended url, e.g /send
@sports.route('/', methods=['POST'])
def display():

	name = request.form.get("name")
	house = request.form.get("house")

	if not name or not house:
		return render_template("error.html")

	return render_template("display.html", name=name, house=house)