from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Devops Community! Here is the ultimate CICD Pipeline🔥🔥'
