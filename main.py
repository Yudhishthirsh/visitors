from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get the user's name and email from the form data
    name = request.form['name']
    email = request.form['email']

    # Log the user's name and email to a file
    with open('form_submissions.txt', 'a') as f:
        f.write(f'{name} {email}\n')

    # Return a simple message to the user
    return 'Thanks for submitting your details!'

if __name__ == '__main__':
    app.run()
