from flask import Flask
from flask import render_template, session,request ,redirect

app = Flask(__name__)

python_chapter = ['Introduction' , 'Installations', 'Input and Output' ,

                  'Flow Control', 'Loop or Iteration' , 'Basic Data Types',

                  'List and List Comprehantions' , 'Reference Books', "FAQ'S"


                  ]

tepmlates =   ['_'.join(x.lower().split())+'.html' for x in python_chapter ]
print tepmlates
url = range(len(python_chapter))

value_pair = zip(python_chapter,url)

question_6 = [

    {'Descriptions': 'What is the value of this code [ x*x for x in [2, 3, 4]' ,

      'ans':[ '[9, 4 ,14] ' , '[4, 9 , 16]' ,'[9, 4 ,14] ' ,'[9, 4 ,14] ' ],

        'correctans' : 1
     },

    {'Descriptions': 'What is the value of this code [ x*x for x in [2, 3, 4]' ,

      'ans':[ '[9, 4 ,14] ' , '[4, 9 , 16]' ,'[9, 4 ,14] ' ,'[9, 4 ,14] ' ],

        'correctans' : 1
     },
    {'Descriptions': 'What is the value of this code [ x*x for x in [2, 3, 4]' ,

      'ans':[ '[9, 4 ,14] ' , '[4, 9 , 16]' ,'[9, 4 ,14] ' ,'[9, 4 ,14] ' ],

        'correctans' : 1
     },
    {'Descriptions': 'What is the value of this code [ x*x for x in [2, 3, 4]' ,

      'ans':[ '[9, 4 ,14] ' , '[4, 9 , 16]' ,'[9, 4 ,14] ' ,'[9, 4 ,14] ' ],

        'correctans' : 1
     }



]



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
@app.route('/')
def hello_world():
    return render_template('home.html', user='Azad')

    return 'Hello from Flask!'	

@app.route('/python')
def hello():

    id =0
    is_active =[ ' ' ]* len(value_pair);

    is_active[id] = 'active'

    return render_template('topic.html', chapters = zip(python_chapter,url,is_active))
@app.route('/ref_books')
def ref_books():




    return render_template('reference_books.html', books = books ,chapters = value_pair)

@app.route('/<id>')
def render_pages(id):

    id = int(id)

    is_active =[ ' ' ]* len(value_pair);

    is_active[id] = 'active'

    if id ==0:
        print id

        return render_template('introduction.html')

    if id ==6:
        print id
        return render_template('list_and_list_comprehantions.html',chapters = zip(python_chapter,url,is_active))


    if id ==7:
        print id
        return render_template('reference_books.html', books = books ,chapters = zip(python_chapter,url, is_active))


    return render_template('topic.html', chapters = zip(python_chapter,url, is_active))
#app.run(debug =True)
