from flask import Flask, render_template,request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker


engine = create_engine("postgres://postgres:b4ah6z1532@localhost/postgres")
db = scoped_session(sessionmaker(bind=engine))

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/DashboardLayout")
def dashboard():
    return render_template("DashboardLayout.html")
