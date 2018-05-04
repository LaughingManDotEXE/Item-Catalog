from flask import Flask, render_template, request, redirect,jsonify, url_for, flash
from flask_bootstrap import Bootstrap
app = Flask(__name__)

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Mage, Magic_Skill


#Connect to Database and create database session
engine = create_engine('sqlite:///mages.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#Show all Mages
@app.route('/')
@app.route('/Mages')
def showMage():
	
#Show a Magic_Skill
@app.route('')
def showMagicSkill():
#Delete a Mage
@app.route('', methods = ['GET','POST'])
def deleteMage():
	if	
		return
	else:
		return
#Delete a Magic_Skill
@app.route('', methods = ['GET','POST'])
def deleteMagicSkill():
	if
		return
	return
		return
#Create a Mage
@app.route('', methods = ['GET','POST'])
def createMage():
	if
		return
	else:
		return
#Create a Magic Skill
@app.route('', methods = ['GET','POST'])
def createMagicSkill():
	if
		return
	else:
		return
#Update a Mage
@app.route('', methods = ['GET','POST'])
def updateMage():
	if
		return
	else:
		return
#Update a Magic_Skill
@app.route('', methods = ['GET','POST'])
def updateMagicSkill():
	if
		return
	else:
		return
#JSON API for all Mage information
@app.route('')
def