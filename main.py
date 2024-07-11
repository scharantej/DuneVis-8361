
# main.py

from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

# Routes

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/buy_now')
def buy_now():
    return render_template('buy_now.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Main Driver

if __name__ == '__main__':
    app.run(debug=True)
