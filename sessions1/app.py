from flask import Flask, render_template, request

app = Flask(__name__)
session = []

@app.route('/')
def home():
	if session:
		return render_template("profile.html", name = session[0])
	else:
		return render_template("home.html")

@app.route('/result')
def result():
	var = request.args.get('name')
	if not var:
		return render_template("home.html")
	session.append(var)
	print(session)
	return render_template("profile.html", name = session[0])

@app.route('/logout')
def logout():
	if session:
		session.pop()
	return render_template("home.html")

@app.route('/profile')
def profile():
	if session:
		return render_template("profile.html", name = session[0])
	return render_template("home.html")

@app.route('/feed')
def feed():
	if session:
		return render_template("feed.html", name = session[0])
	return render_template("home.html")