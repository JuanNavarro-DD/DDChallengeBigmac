'''
 # @ Author: Juan Navarro
 # @ Create Time: 2022-03-28 23:24:49
 # @ Modified by: Juan Navarro
 # @ Modified time: 2022-03-28 23:24:53
 # @ Description:
 '''
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)



@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)