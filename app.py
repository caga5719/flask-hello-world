from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Carlos Garcia in 3308!'

@app.route('/caga5719_db')
def caga5719_db():
    conn = psycopg2.connect("postgres://caga5719_db_user:jgk8px6kecbxYAT0FrhSwflb43dSlugL@dpg-co89c5tjm4es738vrjj0-a/caga5719_db")
    conn.close()
    return "Database Connection Successful"

@app.route('/db_create')
def create_db():
    conn = psycopg2.connect("postgres://caga5719_db_user:jgk8px6kecbxYAT0FrhSwflb43dSlugL@dpg-co89c5tjm4es738vrjj0-a/caga5719_db")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
    ''')
    conn.commit()
    conn.close()
    return "Basketabll Table Successfuly created"

@app.route("/db_insert")
def inserting():
    conn = psycopg2.connect("postgres://caga5719_db_user:jgk8px6kecbxYAT0FrhSwflb43dSlugL@dpg-co89c5tjm4es738vrjj0-a/caga5719_db")
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number) Values
        ('Jayson','Tatum','Boston','Celtics', 0),
        ('Stephen','Curry','San Francisco','Warriors', 30),
        ('Nikola','Jokic','Denver','Nuggets', 15),
        ('Kawhi','Leonard','Los Angeles','Clippers', 0);
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Populated"
