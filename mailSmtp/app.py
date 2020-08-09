from flask import Flask, render_template, request, session
import smtplib

sports = Flask(__name__)
sports.secret_key = "apetnamedsteve"
server = smtplib.SMTP("smtp.gmail.com", 587)

@sports.route('/')
def login():
	return render_template("login.html")

# gmail: had to enable IMAP/POP. had to enable allowance of "less secure apps".
@sports.route('/', methods=['POST'])
def mailscreen():

	email = request.form.get("email")
	pswd = request.form.get("pswd")

	session['email'] = email
	session['pswd'] = pswd

	if not email or not pswd:
		return render_template("error.html", message="you did not enter either the email ID or the password (or both). don't do that, okay?")

	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()

	try:
		server.login(email, pswd)
	except:
		return render_template("error.html", message="you messed up either your email id or password (or both). if you didn't, try enabling IMAP/POP and allowance of \"less secure apps\" in your gmail settings. if not even that, blame gmail. this wasn't supposed to happen.")

	return render_template("mailscreen.html")

@sports.route('/send', methods=['POST'])
def send():

	sendto = request.form.get('sendto')
	mailcontent = request.form.get('mailcontent')

	if not sendto or not mailcontent:
		return render_template("error.html", message="you can't leave either of the fields empty.")

	server.starttls()

	try:
		server.login(session.get('email', None), session.get('pswd', None))
	except:
		return render_template("error.html", message="login failed somehow. blame gmail. this wasn't supposed to happen.")

	try:
		server.sendmail("", sendto, mailcontent)
	except:
		return render_template("error.html", message="your mail could not be sent. gmail screwed up, this wasn't me")

	return render_template("sent.html")