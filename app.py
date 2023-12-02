from flask import Flask, render_template,request
import main

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/submit_form', methods=['POST'])
def submit_form():
    app = request.form['application']
    format = request.form['format']
    info = request.form['info']
    # Process the data
    return main.get_test_cases(app,format,info)





if __name__ == '__main__':
    app.run(debug=True)
