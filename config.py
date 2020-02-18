import os

class Config(object):
    # get the secret-key to be used by flask-wtf to safeguard from CSRF attacks from system veriables or use default
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'user-will-never-guess-it'