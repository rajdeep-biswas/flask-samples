from flask import Flask, render_template, request

sports = Flask(__name__)

@sports.route('/')
def home():
	return render_template("home.html")

@sports.route('/send')
def display():
	name = request.args.get("name")
	house = request.args.get("house")

	if not house:
		house = "not selected"

	if not name:
		name = "not entered"

	return render_template("display.html", name=name, house=house)