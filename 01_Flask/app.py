from flask import Flask

'''
It crates an instance of the flask class,
which will WSGI(Web Server Gateway Interface) application.
'''
### WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this website"

@app.route("/index")
def index():
    return "This is the Index Page"

if __name__ == "__main__":
    app.run(debug=True)