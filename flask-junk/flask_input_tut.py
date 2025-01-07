from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    try:
        f = open('sample.txt', 'r')
        s = f.read()
    except: 
        return('Something went wroting, may be the bank declined payments!')
    else: 
        return(s)

if __name__ == '__main__':
    app.run(debug = True)
