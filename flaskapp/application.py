import mysql.connector
from flask import Flask, request, render_template

application = Flask(__name__, template_folder='template')

mydb = mysql.connector.connect(
    host="endpoint",
    user="username",
    password="password",
    database="databasename"
)

mycursor = mydb.cursor()


@application.route("/")
def home():
    return "<title>Home</title><h1>Home Page</h1>"


@application.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password1"]
        mycursor.execute("INSERT INTO sign_up (email,username,password) VALUES (%s,%s,%s)", [
                         email, username, password])
        mydb.commit()
        return "<h1>User Created</h1>"
    return render_template('sign_up.html')


@application.route("/users")
def users():
    mycursor.execute("SELECT * FROM sign_up")
    fetch = mycursor.fetchall()
    mydb.commit()
    return render_template("page.html", fetch=fetch)


if __name__ == "__main__":
    application.run(debug=True)
