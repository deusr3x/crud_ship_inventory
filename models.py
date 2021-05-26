from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class InventoryModel(db.Model):
    __tablename__ = 'inventory'

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String())
    quantity = db.Column(db.Integer())
    item_description = db.Column(db.String())
    location = db.Column(db.String())
    location_description = db.Column(db.String())

    def __init__(self, item_name, quantity, item_description, location, location_description):
        self.item_name = item_name
        self.quantity = quantity
        self.item_description = item_description
        self.location = location
        self.location_description = location_description

    def __repr__(self):
        return f"{self.id}: {self.item_name} - {self.location}"

