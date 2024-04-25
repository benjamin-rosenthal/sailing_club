from flask import Flask

app = Flask(__name__)

SECRET_KEY = os.environ.get('SECRET_KEY') or 'this is a secret'
print(SECRET_KEY)
app.config['SECRET_KEY'] = SECRET_KEY

from auth import views