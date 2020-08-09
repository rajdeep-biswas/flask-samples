from flask import Flask, render_template, request

sports = Flask(__name__)

sportsmen = []

@sports.route('/')
def home():
	return render_template("home.html")

# using base url for post data, can alternatively use extended url, e.g /send
@sports.route('/', methods=['GET', 'POST'])
def display():

	name = request.form.get("name")
	house = request.form.get("house")

	if not name or not house:
		return render_template("error.html")

	sportsmen.append(f"{name}, {house} House")

	return render_template("display.html", students=sportsmen)

@sports.route('/reg')
def registered():
	return render_template("display.html", students=sportsmen)