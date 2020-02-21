import os

basedir =  os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # get the secret-key to be used by flask-wtf to safeguard from CSRF attacks from system veriables or use default
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'user-will-never-guess-it'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir,'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False