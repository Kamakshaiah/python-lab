from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/payment')
def payment():
    try:
        f = open('bank.txt', 'r')
        s = f.read()
        return render_template('payments.html', s=s)
    except:
        return("Don't be panik, you just don't have money")

if __name__ == '__main__':
    app.run(debug=True) 
