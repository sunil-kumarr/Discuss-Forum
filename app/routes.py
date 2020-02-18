#flask app instance created in __init__.py in app package
from app import app
'''
To render HTML page
The render_template() function invokes the Jinja2 template engine that comes bundled 
with the Flask framework. Jinja2 substitutes {{ ... }} blocks with the corresponding
 values, given by the arguments provided in the render_template() call.
'''
from flask import render_template

#index function return data against this to urls defined as decorater function
@app.route("/")
@app.route("/index")
def index():
    user = {'username':'sunil'}

    return render_template('index.html',title='Home',user = user)