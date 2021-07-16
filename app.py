from flask import Flask, render_template, request

app = Flask(__name__)

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