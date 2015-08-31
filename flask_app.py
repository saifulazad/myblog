from flask import Flask
from flask import render_template, session,request ,redirect

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('home.html', user='Azad')

    return 'Hello from Flask!'	

@app.route('/python')
def hello():
    return render_template('topic.html', chapters = [("ggg", "as"),("Reference Books", "ref_books")])
@app.route('/ref_books')
def ref_books():

    books = [

        {
            'Author': 'Azad',
            'Name': 'Learning Python',
            'Publication': 'Orelly',
            'Descriptions':'This is very nice and cool book ever I have seen',
             'imgURL': 'learing_py.jpeg',
            'AmazonURL': 'http://www.amazon.com/Learning-Python-Edition-Mark-Lutz/dp/1449355730',
        },
        {
            'Author': 'Azad',
            'Name': 'Dive into Python',
            'Publication': 'Orelly',
            'Descriptions':'This is very bad and cool book ever I have seen',
            'imgURL': 'dive_into_python.jpg',
            'AmazonURL': 'http://www.amazon.com/Dive-Into-Python-Mark-Pilgrim/dp/1590593561',
        }

    ]


    return render_template('ref_books.html', books = books ,chapters = [("ggg", "as"),("Reference Books", "ref_books")])




app.run(debug =True)
