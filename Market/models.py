from __init__ import db
from __init__ import app

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=40), nullable=False, unique=True)
    barcode = db.Column(db.String(8), nullable=False, unique=True)
    price = db.Column(db.Numeric(10,2), nullable=False)
    description = db.Column(db.Text)

with app.app_context():
    db.create_all()