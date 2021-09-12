from flask import Flask, render_template, request, redirect
app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
 	return render_template('index.html')

def write_to_file(data):
	with open('database.txt', mode ='a') as database:
		email = data['email']
		subject = data['subject']
		message = data['message']
		file = database.write(f'\n{email},{subject},{message}')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
    	data = request.form.to_dict()
    	write_to_file(data)
    	return 'Submitted'
    else:
    	return 'something went wrong!'
