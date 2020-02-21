"""
 pip install python-dotenv // for auto setting export FLASK_APP = microblog.py
"""
from app import app,db
from app.models import User,Post

@app.shell_context_processor
def make_shell_context():
    return {'db':db, 'User':User, 'Post':Post}
