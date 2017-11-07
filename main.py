# -*- coding: utf-8 -*-
import json, random
from flask import Flask, request
from flask_cors import CORS, cross_origin
from random import randint
from db import Db

app = Flask(__name__)
app.debug = True
CORS(app)

#*************************  R8 - REINITIALISER UNE PARTIE *************************#
@app.route('/reset',methods=['GET'])
def reset():
    db = Db()
    db.executeFile("db.sql")
    db.close()
    return "Reset done."
#**********************************************************************************#

@app.route('/toto',methods=['GET'])
def reset():
    db = Db()
    db.select("SELECT * FROM Joueur")
    db.close()
    return "SELECT OK."
#**********************************************************************************#

