from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/market')
def market():
    items=[{'id':1, 'name':'Gta V', 'barcode':'78356291','price':'$80'},
    {'id':2, 'name':'RDR 2', 'barcode':'85469209','price':'$89'},
    {'id':3, 'name':'Summer Time Saga', 'barcode':'68915628','price':'$20'},
    {'id':4, 'name':'My Femboy Roommate', 'barcode':'69696969','price':'$15'},
    ]
    return render_template('market.html',items=items)

if __name__ == "__main__":
    app.run(debug=True)