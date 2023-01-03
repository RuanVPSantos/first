from flask import Flask, jsonify
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'containers-us-west-148.railway.app'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Qrrpzrh8U0RMTmMnfuQo'
app.config['MYSQL_DB'] = 'railway'

mysql = MySQL(app)


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"

    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        cursor = mysql.connection.cursor()
        cursor.execute(
            ''' INSERT INTO info_table VALUES(%s,%s)''', (name, age))
        mysql.connection.commit()
        cursor.close()
        return f"Done!!"


app.run(host='localhost', port=5000)


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
