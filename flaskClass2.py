from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import pymysql.cursors
import classifier2


def check_Password(user_input):
    connection = pymysql.connect(user='root', password='admin', host='localhost',
                                 database='login')
    with connection.cursor() as cursor:
        sql = "SELECT Password FROM users WHERE username=%s"
        cursor.execute(sql, (user_input,))
        result = cursor.fetchone()[0]
        print(result)
    return result

app = Flask(__name__)


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('home.html')
    else:
        return "you have logged in"


@app.route('/login', methods=['POST'])
def do_admin_login():
    print(request.form["data"])
    if request.form['password'] == check_Password(request.form['username']) and classifier2.check(request.form["username"], request.form["data"]):
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)
