# crud_ship_inventory
Simple CRUD application to catalog items

This will use python Flask for the web interface and a postgresql backend.

## Setup
Following the setups in: https://www.askpython.com/python-modules/flask/flask-postgresql and https://www.askpython.com/python-modules/flask/flask-crud-application

### Install PostgreSQL
1. `sudo apt install postgresql libpq-dev postgresql-client postgresql-client-common`
2. Run `sudo su postgres` to change to the postgres user.
3. Now run `psql` and create a user and a database that you wish to use (`CREATE DATABASE <dbname>`)
### Create Virtual Environment
1. Create virtual environment - `sudo apt install python3.7-venv` -> `python3 -m venv env`
2. `source env/bin/activate`
3. Install from requirements.txt `pip install -r requirements.txt`
### Initialise Flask
1. Set environment variables
    - PGUSER -> postgresql username
    - PGPASSWORD -> postgresql username password
    - DBNAME -> database name created in previous step
2. Run:
```
flask db init
flask db migrate
flask db upgrade
```

## Running
To run `python app.py` will start a flask server on `0.0.0.0:5000`.  
### Enter Records
Go to `localhost:5000/data/create`
### View Records
`localhost:5000/data`
### Search Records
`localhost:5000/search`