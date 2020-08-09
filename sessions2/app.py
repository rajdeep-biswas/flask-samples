from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "ggwprip"

@app.route('/')
def home():
	if "name" in session:
		return render_template("profile.html", name = session["name"])
	else:
		return render_template("home.html")

@app.route('/result')
def result():
	var = request.args.get('name')
	if not var:
		return render_template("home.html")
	session["name"] = var
	print(session)
	return render_template("profile.html", name = session["name"])

@app.route('/logout')
def logout():
	session.pop("name", None)
	return render_template("home.html")

@app.route('/profile')
def profile():
	if "name" in session:
		return render_template("profile.html", name = session["name"])
	return render_template("home.html")

@app.route('/feed')
def feed():
	if "name" in session:
		return render_template("feed.html", name = session["name"])
	return render_template("home.html")