from flask import Flask, jsonify, render_template, redirect, url_for, request
import os
import MySQLdb

db = MySQLdb.connect(host="containers-us-west-148.railway.app",
                     user="root",
                     password="Qrrpzrh8U0RMTmMnfuQo",
                     db="railway")

cur = db.cursor()

cur.execute("SELECT * FROM info_table")
data = cur.fetchall()

db.close()

app = Flask(__name__)


@app.route('/')
def form():
    return render_template('form.html', data=data)


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
