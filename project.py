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

#Delete a Mage
#Delete a Magic_Skill
#Create a Mage
#Create a Magic Skill
#Update a Mage
#Update a Magic_Skill
#Show a Mage
#Show a Magic_Skill
#JSON API for all Mage information