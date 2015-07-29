from flask import Flask
from flask import render_template, session,request ,redirect

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('base.html', user='Azad')

    return 'Hello from Flask!'	



app.run(debug =True)
