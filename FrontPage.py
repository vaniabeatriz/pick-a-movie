from flask import Flask, render_template

app = Flask(__name__)

#create the pages of site

@app.route('/')
def home():
    return render_template('index.html')
    # return 'Hello! this is the main page <h1>Hello</h1>'

@app.route('/second/')
def second():
    return render_template('secondpage.html')

if __name__== '__main__':
    app.run() #adding #debug=False still get internal server error