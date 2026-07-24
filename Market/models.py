from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    email_address = db.Column(db.String(40), nullable=False, unique=True)
    password_hash = db.Column(db.String(60), nullable=False)
    budget = db.Column(db.Integer, nullable=False, default=1000)
    items = db.relationship('Item', backref='owned_user', lazy=True)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=40), nullable=False, unique=True)
    barcode = db.Column(db.String(8), nullable=False, unique=True)
    price = db.Column(db.Numeric(10,2), nullable=False)
    description = db.Column(db.Text)
    owner = db.Column(db.Integer, db.ForeignKey('user.id'))