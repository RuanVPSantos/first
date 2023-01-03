from flask import Flask, render_template, request
from flask_mysqldb import MySQL


app = Flask(__name__)
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'containers-us-west-148.railway.app'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Qrrpzrh8U0RMTmMnfuQo'
app.config['MYSQL_PORT'] = 7721
app.config['MYSQL_DB'] = 'railway'

mysql = MySQL(app)


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})


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
            ''' INSERT INTO info_table(name, age) VALUES(%s,%s)''', (name, age))
        mysql.connection.commit()
        cursor.close()
        return f"Done!!"


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
