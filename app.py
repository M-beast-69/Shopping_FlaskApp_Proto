from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/market')
def market():
    return render_template('market.html', item_name="Summer Time Saga", price="$20")

if __name__ == "__main__":
    app.run(debug=True)