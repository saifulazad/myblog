from flask import Flask
from flask import render_template, session,request ,redirect

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html', user='Azad')

    return 'Hello from Flask!'	


app.run(host = '0.0.0.0',debug=True)
