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

#Show all Mages
@app.route('/')
@app.route('/Mages')
def showMage():
mages = session.query(Mage).order_by(asc(Mage.name))
  return render_template('mages.html', mages = mages)
	
#Show a Magic_Skill
@app.route('')
def showMagicSkill():
@app.route('/mage/<int:mage_id>/')
@app.route('/mage/<int:mage_id>/menu/')
def showMagicSkills(mage_id):
    mage = session.query(Mage).filter_by(id = mage_id).one()
    items = session.query(MagicSkill).filter_by(mage_id = mage_id).all()
    return render_template('menu.html', items = items, mage = mage)
#Delete a Mage
@app.route('/mage/<int:mage_id>/delete/', methods = ['GET','POST'])
def deleteMage(mage_id):
  mageToDelete = session.query(Mage).filter_by(id = mage_id).one()
  if request.method == 'POST':
    session.delete(mageToDelete)
    flash('%s A Mage character has been deleted' % mageToDelete.name)
    session.commit()
    return redirect(url_for('showMages', mage_id = mage_id))
  else:
    return render_template('deleteMage.html',mage = mageToDelete)
#Delete a Magic_Skill
@app.route('', methods = ['GET','POST'])
def deleteMagicSkill():
	if
		return
	return
		return
#Create a Mage
@app.route('', methods = ['GET','POST'])
def createMage(mage_id):
  if request.method == 'POST':
      newMage = Mage(name = request.form['name'])
      session.add(newMage)
      flash('New Mage %s has been added' % newMage.name)
      session.commit()
      return redirect(url_for('showMage'))
  else:
      return render_template('newMage.html')
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
@app.route('/mage/<int:mage_id>/menu/<int:skill_id>/edit', methods=['GET','POST'])
def editMagicSkill(mage_id, skill_id):

    editedSkill = session.query(MagicSkill).filter_by(id = skill_id).one()
    mage = session.query(Mage).filter_by(id = mage_id).one()
    if request.method == 'POST':
        if request.form['skillName']:
            editedSkill.skillName = request.form['skillName']
        if request.form['description']:
            editedSkill.description = request.form['description']
        if request.form['power']:
            editedSkill.power = request.form['power']
        if request.form['course']:
            editedSkill.course = request.form['course']
        session.add(editedSkill)
        session.commit() 
        flash('Magic skill Successfully Edited')
        return redirect(url_for('showMagicSkills', mage_id = mage_id))
    else:
        return render_template('edit_magic_skill.html', mage_id = mage_id, skill_id = skill_id, item = editedSkill)
#JSON API for all Mage information
@app.route('')
def