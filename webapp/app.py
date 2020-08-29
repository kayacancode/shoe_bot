from flask import Flask, redirect, url_for, request, render_template, session
from flask_pymongo import PyMongo
from pymongo import MongoClient
import bcrypt
import re

app = Flask(__name__, template_folder="template")

app.config["MONGO_URI"] = "mongodb+srv://founder:ilovesuppli123@cluster0.5z5et.mongodb.net/suppli?retryWrites=true&w=majority"
mongo = PyMongo(app)


@app.route("/")
def terminal():
    return render_template("index.html", content="Testing")


@app.route('/signupshoeinfo')
def signupshoeinfo():
    return render_template("signupshoeinfo.html")


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        firstname = mongo.db.firstname
        firstname = firstname.insert_one({'name': request.form["firstname"]})
        lastname = mongo.db.lastname
        lastname = lastname.insert_one({'name': request.form["lastname"]})
        birthday = mongo.db.birthday
        birthday = birthday.insert_one({'name': request.form["birthday"]})

        def validateEmail(email):
            regexresult = re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email)
            valid = validateEmail(email)
            if valid:
                print(regexresult)
            # add if user email is already in the database flash error "Email address already exists"
            # direct it to the sign in page
            else:
                print('invalid email format: ', email)

        email = mongo.db.email
        email = email.insert_one({'name': request.form["email"]})
        emails = mongo.db.email
        emailcol = emails["email"]
        x = emailcol.find()
        for data in x:
            print(data)
        users = mongo.db.users
        existing_users = users.find_one({'name': request.form["username"]})

        if existing_users is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert_one({'name': request.form['username'], 'password': hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('signupshoeinfo'))
        return ' That username already exists!'

    return render_template("signup.html")


if __name__ == "__main__":
    app.secret_key = 'longwax57'
    app.run(debug=True)
