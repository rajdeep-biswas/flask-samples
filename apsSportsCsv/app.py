from flask import Flask, render_template, request
from csv import writer, reader

sports = Flask(__name__)

sportsmen = []

@sports.route('/')
def home():
	return render_template("home.html")

# list adds an empty value in my PC version. i tried the exact same code on the cs50 sandbox. it works normally.
@sports.route('/', methods=['GET', 'POST'])
def display():

	if not request.form.get("name") or not request.form.get("house"):
		return render_template("error.html")

	file = open("registered.csv", "a")

	wr = writer(file)
	wr.writerow((request.form.get("name"), request.form.get("house")))
	file.close()

	return "worked"

@sports.route('/reg')
def registered():

	with open("registered.csv", "r") as file:
		rdr = reader(file)
		sportsmen = list(rdr)
	return render_template("display.html", students=sportsmen)