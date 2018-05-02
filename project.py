from flask import Flask, render_template, request, redirect,jsonify, url_for, flash
app = Flask(__name__)

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Mage, Magic_Skill


#Connect to Database and create database session
engine = create_engine('sqlite:///mages.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#Show a Mage
@app.route
def showMage
#Show a Magic_Skill
@app.route
def showMagicSkill()
#Delete a Mage
@app.route
def deleteMage()
#Delete a Magic_Skill
@app.route
def deleteMagicSkill()
#Create a Mage
@app.route
def createMage()
#Create a Magic Skill
@app.route
def createMagicSkill()
#Update a Mage
@app.route
def updateMage()
#Update a Magic_Skill
@app.route
def updateMagicSkill()
#JSON API for all Mage information
@app.route
def