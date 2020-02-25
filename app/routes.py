#flask app instance created in __init__.py in app package
from app import app
'''
To render HTML page
The render_template() function invokes the Jinja2 template engine that comes bundled 
with the Flask framework. Jinja2 substitutes {{ ... }} blocks with the corresponding
 values, given by the arguments provided in the render_template() call.
'''
from flask import render_template,flash,redirect,url_for
from app.forms import LoginForm
from flask_login import current_user,login_user
from app.models import User

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
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user,remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html',title='Sign In',form = form)

