
from ctypes.wintypes import INT
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<word>')
def hi(word):
    return 'Hi! ' + word

@app.route('/repeat/<int:inti>/<string:word>')
def repeat(inti,word):
    return f"{word} " * inti

@app.route('/ourrepeat/<int:num>/<string:words>')
def words(num,words):
    output = ''
    for i in range(0,num):
        output += f"<p>{words}</p>"
    return output



if __name__=="__main__":  
    app.run(debug=True)