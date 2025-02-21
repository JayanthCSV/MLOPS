from flask import Flask, request, render_template

'''
It crates an instance of the flask class,
which will WSGI(Web Server Gateway Interface) application.
'''
### WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to this website</H1></html>"

@app.route("/index")
def index():
    return render_template('index.html') 

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)