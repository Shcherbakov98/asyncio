"""Приложение Flask выборки торговых марок"""
from flask import Flask, jsonify
import psycopg2


app = Flask(__name__)
conn_info = "dbname=warehouse user=artem password=123 host=127.0.0.1"
db = psycopg2.connect(conn_info)


@app.route('/brands')
def brands():
    cur = db.cursor()
    cur.execute('SELECT brand_id, brand_name FROM products.brand')
    rows = cur.fetchall()
    cur.close()
    return jsonify([{'brand_id': row[0], 'brand_name': row[1]} for row in rows])
