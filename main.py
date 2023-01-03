from flask import Flask, jsonify, render_template, redirect, url_for, request
import os
import MySQLdb

db = MySQLdb.connect(host="containers-us-west-148.railway.app",
                     user="root",
                     passwd="Qrrpzrh8U0RMTmMnfuQo",
                     db="railway")

cur = db.cursor()

cur.execute("SELECT * FROM YOUR_TABLE_NAME")

for row in cur.fetchall():
    print(row[0])

db.close()

app = Flask(__name__)


@app.route('/')
def form():
    return render_template('form.html')


# from flask_mysqldb import MySQL


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
# app.config['MYSQL_DATABASE_URL'] = 'mysql://root:Qrrpzrh8U0RMTmMnfuQo@containers-us-west-148.railway.app:7721/railway'
# app.config['MYSQL_DATABASE_HOST'] = 'containers-us-west-148.railway.app'
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PORT'] = '7721'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'Qrrpzrh8U0RMTmMnfuQo'
# app.config['MYSQL_DATABASE_DB'] = 'railway'

# mysql = MySQL(app)


# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     cursor = mysql.connection.cursor()

#     mycursor.execute("SELECT * FROM customers")

#     myresult = mycursor.connection.fetchall()
#     cursor.close()

#     return myresult

#     # if request.method == 'GET':
#     #     return "Login via the login Form"

#     # if request.method == 'POST':
#     #     name = request.form['name']
#     #     age = request.form['age']
#     #     cursor = mysql.connection.cursor()
#     #     cursor.execute(
#     #         ''' INSERT INTO info_table VALUES(%s,%s)''', (name, age))
#     #     mysql.connection.commit()
#     #     cursor.close()
#     #     return f"Done!!"


# app.run(host='localhost', port=5000)
