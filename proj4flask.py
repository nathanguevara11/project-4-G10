from flask import Flask, render_template, jsonify, request, redirect, url_for
import requests
import psycopg2
import sqlalchemy
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

from IPython.display import display
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKeyConstraint, PrimaryKeyConstraint, ForeignKey, Sequence, Date


app = Flask(__name__)

import os
from dotenv import load_dotenv

load_dotenv() 
database_url = os.getenv("DATABASE_URL")

engine = create_engine(database_url)
base = declarative_base()

class user_info(base): 
    __tablename__ = 'user_info'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    first_name = Column(String(250))
    last_name = Column(String(250))
    birthday = Column(Date)

    # __table_args__ = (
    #     PrimaryKeyConstraint('id'), 
    #     {'extend_existing': True},
    # )    

class order(base): 
    __tablename__ = 'amount_add'
    
    order_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user_info.id'))
    amount = Column(Float)
    team = Column(String(250))
    win_draw_loss = Column(String(250))

    __table_args__ = (
        {'extend_existing':True},
    )
    
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)

session = Session()

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/Soccer')
def Soccer():
    return render_template('Soccer.html')
@app.route('/Basketball')
def Basketball():
    return render_template('Basketball.html')
@app.route('/Football')
def Football():
    return render_template('Football.html')
@app.route('/Hockey')
def Hockey():
    return render_template('Hockey.html')
@app.route('/submissions')
def submissions():
    return render_template('submissions.html')
@app.route('/sub', methods = ["GET", "POST"])
def sub():
    if request.method == 'POST':
        first_name = request.form.get('first name')
        last_name = request.form.get('last name')
        birthday = request.form.get('birthday')
        amount = request.form.get('amount')
        team= request.form.get('team')
        win_draw_loss = request.form.get('wdl')

        new_user = user_info(first_name =first_name, last_name = last_name, birthday = birthday)
       
        session.add(new_user)
        session.commit()

        new_order = order(user_id = new_user.id  ,amount = amount,  team = team , win_draw_loss = win_draw_loss)
        session.add(new_order)
        session.commit()

        return redirect(url_for('confirmation', first_name=first_name, last_name=last_name, birthday=birthday, user_id = new_user.id  ,amount = amount,  team = team , win_draw_loss = win_draw_loss))

    return render_template('submissions.html')

@app.route('/confirmation')
def confirmation():
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    birthday = request.args.get('birthday')
    amount = request.args.get('amount')
    team= request.args.get('team')
    wdl = request.args.get('win_draw_loss')
    return render_template('confirm.html',first_name=first_name, last_name=last_name, birthday=birthday,amount = amount,  team = team , win_draw_loss = wdl)
if __name__ == "__main__":
    app.run(debug = True)