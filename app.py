from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Carlos Garcia in 3308!'

@app.route('/caga5719_db')
def caga5719_db():
    conn = psycopg2.connect("caga5719_db")
    conn.close()
    return "Database Connection Successful"
    