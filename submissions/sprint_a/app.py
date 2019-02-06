# Import the instance of app from the sprint_a package. 
# A package in Python is any directory with an _init_.py file. 
# By defining the configure_app and using it to instantiate an instance of Flask in the _init_.py file,
# we can import app directly from the project's root directory.
from flask import Flask, render_template

from sprint_a import app #??????

app = Flask(__name__)


# 1. In app.py, use the app.route decorator to:
#     bind a view function called generate_epithets to '/'. This route will serve a randomly generated epithet.
#     bind a view function called vocabulary to '/vocabulary'. This route will serve the vocabulary used to generate epithets.
# 2. Have these functions return a JSON representation of {"epithets": []} and {"vocabulary": {}} respectively.
@app.route('/')
@app.route('/home')
def generate_epithets():
    return render_template('insults.html')


@app.route('/vocabulary')
def vocagulary():
    return render_template('vocab.html')

if __name__ == '__main__':
    # app.run(debug=True)  ?????
    app.run()

