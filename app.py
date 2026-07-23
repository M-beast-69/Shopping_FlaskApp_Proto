from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/<username>')
def about(username):
    return f'<h1>Hello {username}</h1>'

if __name__ == "__main__":
    app.run(debug=True)