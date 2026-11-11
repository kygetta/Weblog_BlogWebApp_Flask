# View function

from apphost import app

# app.route = decorators *py function to modify the function that follows
# Creates association bet. the URL as an argument and function.
@app.route('/')
@app.route('/index')
def index():
    return "Hello, World"