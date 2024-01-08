from flask import Flask
from flask import url_for
from flask import render_template


app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    markers=[
   {
   'lat':0,
   'lon':0,
   'popup':'This is the middle of the map.'
    }
   ]
    return render_template('index.html', markers=markers )


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

@app.route('/login')
def login():
    return 'login'

with app.test_request_context():
    print(url_for('home'))
    print(url_for('about'))
    print(url_for('login'))
    print(url_for('profile', username='John Doe'))

if __name__ == '__main__':
    app.run(debug=True)