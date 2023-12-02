from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/submit_form', methods=['POST'])
def submit_form():
    name = request.form['application']
    email = request.form['format']
    age = request.form['info']
    # Process the data
    return 'Form Submitted'


if __name__ == '__main__':
    app.run(debug=True)
