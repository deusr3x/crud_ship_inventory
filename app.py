from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect
from flask_migrate import Migrate
from models import db, InventoryModel
import os
import sqlalchemy as sqla


PASSWORD = os.environ['PGPASSWORD']
USERNAME = os.environ['PGUSER']
DBNAME = os.environ['DBNAME']

app = Flask(__name__)

db_uri = f"postgresql://{USERNAME}:{PASSWORD}@localhost:5432/{DBNAME}"
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

with app.app_context():
    db.create_all()


engine = sqla.create_engine(db_uri)
connection = engine.connect()
metadata = sqla.MetaData()
inventory = sqla.Table('inventory', metadata, autoload=True, autoload_with=engine)


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


@app.route('/data')
def RetrieveList():
    inv = InventoryModel.query.all()
    return render_template('datalist.html', inv=inv)


@app.route('/data/<int:id>')
def RetrieveSingleItem(id):
    item = InventoryModel.query.filter_by(id=id).first()
    if item:
        return render_template('data.html', item=item)
    return f"Item with ID: {id} does not exist"


# @app.route('/data/<int:id>/update', methods=['GET', 'POST'])
# def Update(id):
#     inv = InventoryModel.query.filter_by(id=id).first()
#     if request.method == 'POST':
#         if inv:
#             item_name = request.form['item_name']
#             quantity = request.form['quantity']
#             item_desc = request.form['item_desc']
#             location = request.form['location']
#             location_desc = request.form['location_desc']
#             # t = InventoryModel.query.filter_by(id=1).update(InventoryModel.quantit=20)
#             query = sqla.update(inventory).values({'quantity': quantity, 'item_name': item_name, 'item_description': item_desc, 'location': location, 'location_description': location_desc}).where(inventory.columns.id==id)
#             res = connection.execute(query)
#             return redirect('/data')
#     if request.method == 'GET':
#         return render_template('update.html', inv=inv)


@app.route('/update2', methods=['POST'])
def Update2():
    if request.method == 'POST':
        inv = InventoryModel.query.filter_by(id=request.form['update']).first()
        return render_template('update.html', inv=inv)


@app.route('/make_update', methods=['POST'])
def Make_Update():
    if request.method == 'POST':
        inv = InventoryModel.query.filter_by(id=request.form['id']).first()
        if inv:
            item_name = request.form['item_name']
            quantity = request.form['quantity']
            item_desc = request.form['item_desc']
            location = request.form['location']
            location_desc = request.form['location_desc']
            # t = InventoryModel.query.filter_by(id=1).update(InventoryModel.quantit=20)
            query = sqla.update(inventory).values({'quantity': quantity, 'item_name': item_name, 'item_description': item_desc, 'location': location, 'location_description': location_desc}).where(inventory.columns.id==request.form['id'])
            res = connection.execute(query)
            return redirect('/data')



@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        return render_template('search.html', inv='')
    
    if request.method == 'POST':
        search_str = request.form['item_search']
        res = InventoryModel.query.filter(InventoryModel.item_name.like(search_str+'%'))
    return render_template('search.html', inv=res)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
