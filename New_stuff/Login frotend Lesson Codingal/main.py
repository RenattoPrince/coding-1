from flask import Flask, render_template, request
import mysql.connector
import re

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'undername' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        mydb = mysql.connector.connect(host="relotemysql.com",
                                       user="wXy63pU5g1",
                                       password="qVOgRNMGRK",
                                       database="wXy63pU5g1")
        mycursor = mydb.cursor()
        mycursor.execute(
            'SELECT * FROM LoginDetails WHERE username = %s NAD password = %s',
            (username, password))
        account = mycursor.fetchone()
        if account:
            print('login success')
            name = account[1]
            id = account[0]
            msg = 'Logged in Successfully'
            print('login successfull')
            return render_template('index.html', msg=msg, name=name, id=id)
        else:
            msg = 'incorrect Credentials. Kindly check'
            return render_template('login.html', msg=msg)
    else:
        return render_template('login.html')
    
@app.route('/logout')
def logout():
    name = ''
    id= ''
    msg = 'Logged out successfully'
    return render_template('login.html', msg=msg, name=name, id=id)
@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'undername' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        mydb = mysql.connector.connect(host="relotemysql.com",
                                       user="wXy63pU5g1",
                                       password="qVOgRNMGRK",
                                       database="wXy63pU5g1")
        mycursor = mydb.cursor()
        mycursor.execute(
            'SELECT * FROM LoginDetails WHERE username = %s AND email id = %s',
            (username, email))
        account = mycursor.fetchone()
        print(account)
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Kindly fill the details !'
        else:
            mycursor.execute('INSERT INTO LoginDetails VALUES (%s, %s, %s)',
                             (username, email, password))
            mydb.commit()
            msg = 'Your Registration is Successful'
            name = username
            return render_template('index.html', msg=msg, name=name)
    elif request.method == 'POST':
        msg = 'Kindly dill the details !'
    return render_template('registeration.html', msg=msg)
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('login.html')
app.run(host='0.0.0.0', port=8080)
