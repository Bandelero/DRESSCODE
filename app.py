from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app,db)
####################################################

class data_import(db.Model):

	__tablename__ = 'Bookings'

	id = db.Column(db.Integer,primary_key=True)
	email = db.Column(db.Text)
	first_name = db.Column(db.Text)
	last_name = db.Column(db.Text)

	def __init__(self,email,first_name,last_name):
		self.email = email
		self.first_name = first_name
		self.last_name = last_name

	def __repr__(self):
		return f"Email: {self.email} \n First Name: {self.first_name} \n Last Name: {self.last_name}"




@app.route('/')
def index():
	return render_template('index.html')

@app.route('/form')
def form():
	return render_template('form.html')
 
#temporary
@app.route('/thankyou')
def thank_you():
	first = request.args.get('first')
	last = request.args.get('last')
	email = request.args.get('email')

	return render_template('thankyou.html', first=first, last=last, email=email)

@app.route('/services')
def services():
	return render_template('services.html')

@app.route('/gallery')
def gallery():
	return render_template('gallery.html')

@app.route('/events')
def events():
	return render_template('events.html')

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404


if __name__ == '__main__':
	app.run(debug=True)