from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=40), nullable=False, unique=True)
    barcode = db.Column(db.String(8), nullable=False, unique=True)
    price = db.Column(db.Numeric(10,2), nullable=False)
    description = db.Column(db.Text)

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
    with app.app_context():
        db.create_all()
    app.run(debug=True)