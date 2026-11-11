# View function
from flask import render_template
from apphost import app

# app.route = decorators *py function to modify the function that follows
# Creates association bet. the URL as an argument and function.
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Morgan'}
    posts = [
            {
                'author': {'username': 'John'},
                'body': 'Beautiful day in Portland!'
            },
            {
                  'author': {'username': 'Suzy'},
                  'body': 'The Avengers movie was 10/10!'
            }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)






