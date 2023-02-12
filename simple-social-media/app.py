import threading
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import flash
from flask_socketio import SocketIO, send
from flask_sockets import Sockets
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
import socket
import asyncio
from wtforms import SubmitField
import websockets
import os
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, logout_user, login_required, current_user
import json
addfriendbutton = False
PORT = 5050
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy()
userbio = ""
url = "ws://localhost:8080"
viewedanaccount = False


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    posts = db.relationship('Post', backref='user', passive_deletes=True)
    friends = db.relationship('Friends', backref='user')


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=True)
    author = db.Column(db.Integer, db.ForeignKey(
        'user.id', ondelete="CASCADE"), nullable=False)


class Bio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    author = db.Column(db.Integer, db.ForeignKey(
        'user.id', ondelete="CASCADE"), nullable=False)


class Friends(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    requser = db.Column(db.Text, nullable=False)
    authuser = db.Column(db.Integer, db.ForeignKey(
        'user.id', ondelete="CASCADE"), nullable=False)


db.init_app(app)
DB_NAME = "database.db"
loggedin = False
login_manager = LoginManager()
login_manager.login_view = "app.setname"
loggingvar = ""


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

def create_database():
    login_manager.init_app(app)
    app.app_context().push()
    db.create_all()

create_database()

def addFriend(requestinguser, user):
    userfriend = Friends(requser=requestinguser, authuser=user)
    db.session.add(userfriend)
    db.session.commit()

friendslist = []
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = "secret_key_secret_key_secret_key"
login_manager = LoginManager()
login_manager.login_view = "app.setname"
currentuser = ""
postinguser = ""
madeaccount = False


class Website:
    @app.route("/")
    def redir():
        return redirect("/setname")

    @app.route("/logout", methods=['GET', 'POST'])
    def logout():
        global madeaccount
        madeaccount = False
        logout_user()
        return redirect("/setname")

    @app.route("/processinguserinfo/random/<string:userinfo>", methods=["POST"])
    def ProcessingUserInfo(userinfo):
        userinfo = json.loads(userinfo)
        userfriended = userinfo
        print(userfriended)
        return("/")

    @app.route("/signin", methods=["GET", "POST"])
    def signin():
        if request.method == "POST":
            global madeaccount
            global currentuser
            global currentpass
            currentuser = request.form.get("username")
            currentpass = request.form.get("password")
            user = User.query.filter_by(username=currentuser).first()
            if user:
                if check_password_hash(user.password, currentpass):
                    flash("logged in!", category="success")
                    login_user(user, remember=True)
                    madeaccount = True
                    global loggedin
                    loggedin = True
                    return redirect("/home")
                else:
                    flash("Password is incorrect.", category="error")
                    return redirect("/signin")
            else:
                flash("User does not exist.", category="error")
            return redirect("signin")
        if request.method == "GET":
            return render_template("sigin.html", madeaccount=madeaccount)

    @app.route("/home", methods=["GET", "POST"])
    @login_required
    def index():
        if request.method == "GET":
            posts = Post.query.all()
            return render_template("home.html", current_username=currentuser, postinguser=postinguser, madeaccount=madeaccount, posts=posts, addfriendbutton=addfriendbutton)

    @app.route("/creatingpost", methods=["GET", "POST"])
    def creatingpost():
        if request.method == "POST":
            if loggedin == True:
                global postinguser
                global text
                text = request.form.get("text")
                if not text:
                    flash("chat cannot be empty", category='error')
                    return redirect("/home")
                else:
                    post = Post(text=text, author=current_user.id)
                    db.session.add(post)
                    db.session.commit()
                    flash("chat submitted")
                    return redirect("/home")
            else:
                flash("you need an account to post here!", category="error")
                return redirect("/home")
        return render_template("makingpost.html")

    @app.route("/setname", methods=['GET', 'POST'])
    def setname():
        if request.method == 'POST':
            global currentuser
            global currentpass
            global madeaccount
            currentuser = request.form.get("username")
            currentpass = request.form.get("password")
            currentconfirmationpass = request.form.get("confirmationpassword")
            user_exists = User.query.filter_by(username=currentuser).first()
            if user_exists:
                flash("User is already in use.", category="error")
                return render_template("setname.html", madeaccount=madeaccount)
            elif currentconfirmationpass != currentpass:
                flash("Passwords don't match!", category="error")
                return render_template("setname.html", madeaccount=madeaccount)
            elif len(currentpass) < 2:
                flash("Password is too short", category="error")
                return render_template("setname.html", madeaccount=madeaccount)
            else:
                new_user = User(username=currentuser, password=generate_password_hash(
                    currentpass, method="sha256"))
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user, remember=True)
                madeaccount = True
                loggingvar = "Account created"
                return redirect("/home")
        if request.method == "GET":
            return render_template("setname.html", madeaccount=madeaccount)

    @app.route("/users/@<username>", methods=["GET", "POST"])
    @login_required
    def user(username):
        currentbio = Bio.query.filter_by(author=username).first()
        user = User.query.filter_by(username=username).first()
        print(currentbio)
        global currentotherusername
        global viewedanaccount
        currentotherusername = username
        viewedanaccount = True
        try:
            if user.username == currentuser:
                if request.method == "POST":
                    if user.username == currentuser:
                        bio = request.form.get("bio-feild")
                        bio = Bio(text=bio, author=username)
                        db.session.add(bio)
                        db.session.commit()
                if request.method == "GET":
                    return render_template("myaccount.html", currentbio=currentbio, username=username, user=user)
            elif user.username != currentuser:
                return render_template("other_person.html", currentbio=currentbio, username=username, user=user)
        except:
            return render_template("usernotfound.html", currentbio=currentbio, username=username, user=user)

    @app.route("/privatechats", methods=["GET", "POST"])
    def privatechats():
        return render_template("chats.html", madeaccount=madeaccount, friendslist=friendslist)

    @app.route("/private-chat/@<user>")
    def privatechat(user):
        if request.method == "GET":
            friends = Friends.query.filter_by(authuser=currentuser)
            for friend in friends:
                friendtemplist = []
                if friend == user:
                    friendtemplist.append(str(user))
                if friend == friends[-1] and str(user) not in friendtemplist:
                    return f"<p>this person is not on your friends list</p>"
                else:
                    return f"<p>{friend}</p>"
    if viewedanaccount:
        @app.route("/api", methods=["GET", "POST"])
        def api():
            addFriend(currentotherusername, currentuser)
            return redirect(f"/privatechats/@{currentotherusername}", friends=Friends, madeaccount=madeaccount)


if __name__ == "__main__":
    app.run(debug=True)
