#flask app instance created in __init__.py in app package
from app import app
'''
To render HTML page
The render_template() function invokes the Jinja2 template engine that comes bundled 
with the Flask framework. Jinja2 substitutes {{ ... }} blocks with the corresponding
 values, given by the arguments provided in the render_template() call.
'''
from flask import render_template,flash,redirect
from app.forms import LoginForm

#index function return data against this to urls defined as decorater function
@app.route("/")
@app.route("/index")
def index():
    user = {'username':'sunil'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',title='Home',user = user, posts=posts)

@app.route("/login" ,methods = ['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            login_form.username.data, login_form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',title='Sign In',form=login_form)
