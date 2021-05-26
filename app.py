from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect
from flask_migrate import Migrate
from models import db, InventoryModel
import os


PASSWORD = os.environ['PGPASSWORD']
USERNAME = os.environ['PGUSER']

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{USERNAME}:{PASSWORD}@localhost:5432/dev"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/data/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')

    if request.method == 'POST':
        item_name = request.form['item_name']
        quantity = request.form['quantity']
        item_desc = request.form['item_desc']
        location = request.form['location']
        location_desc = request.form['location_desc']
        inv = InventoryModel(item_name, quantity, item_desc, location, location_desc)
        db.session.add(inv)
        db.session.commit()
        return redirect('/data')


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
