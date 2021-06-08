
#import pandas as pd
#import numpy as np
#import psycopg2
#import os
#import json
from flask_pymongo import PyMongo
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine

from flask import Flask, render_template, jsonify, request, redirect
from flask_sqlalchemy import SQLAlchemy

from models import create_classes

##########################   Database Setup  #############################


## Create engine to hawaii.sqlite
engine = create_engine('postgresql://TEST:postgres@localhost:5432/Marvel_US_ITTEM')

## reflect an existing database into a new model
Base = automap_base()

## To reflect the returned tables 
Base.prepare(engine, reflect=True)

## View all of the classes that automap found
Base.classes.keys()

## Create session 
session = Session(bind=engine)



###############
# Flask Setup
###############

# create route that renders index.html template, 
# If index in template folder, replace app variable with: app = Flask(__name__, template_folder='templates')
########################################################
app = Flask(__name__)
########################################################



from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://TEST:postgres@localhost:5432/Marvel_US_ITTEM'


# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Set Database instance
db = SQLAlchemy(app)

# Function calling 'models.py' function
Marvel = create_classes(db)


########################################################

@app.route("/")
def welcome():
    """List all available api routes tests."""
    return (
        f"Available Routes:<br/>"
        f"Raw Data: /MarvelUSRaw<br/>"
        f"Data w/Title Keys: /MarvelUS<br/>"
        )
    
# ----------------------------------------- #

    
@app.route("/MarvelUSRaw")
def TEST():
    
    session = Session(engine)
    results = session.query(
        Marvel._id, Marvel.TARGET, Marvel.CODENAME, Marvel.REAL_NAME, Marvel.GENDER, Marvel.RELATIONSHIP_STATUS, 
        Marvel.ALIGNMENT, Marvel.HEIGHT, Marvel.WEIGHT, Marvel.EYECOLOR, Marvel.HAIRCOLOR, Marvel.IDENTIFIES_AS,
        Marvel.BIRTHPLACE, Marvel.CITIZENSHIP, Marvel.EDUCATION, Marvel.EXPERIENCE, Marvel.INTELLIGENCE, Marvel.STRENGTH,
        Marvel.SPEED, Marvel.DURABILITY, Marvel.ENERGY, Marvel.FIGHTING, Marvel.PROFILE_PIC, Marvel.FAVORITE_HANGOUTS,
        Marvel.DETAILED_FILE, Marvel.POWERS_URL, Marvel.City, Marvel.State, Marvel.Zip_Code, Marvel.Latitude, Marvel.Longitude
        ).all()
    session.close()
    return jsonify(results)

# ----------------------------------------- #

@app.route('/MarvelUSDict')
def MarvelDict():
    session = Session(engine)    
    results = session.query(
        Marvel._id, Marvel.TARGET, Marvel.CODENAME, Marvel.REAL_NAME, Marvel.GENDER, Marvel.RELATIONSHIP_STATUS, 
        Marvel.ALIGNMENT, Marvel.HEIGHT, Marvel.WEIGHT, Marvel.EYECOLOR, Marvel.HAIRCOLOR, Marvel.IDENTIFIES_AS,
        Marvel.BIRTHPLACE, Marvel.CITIZENSHIP, Marvel.EDUCATION, Marvel.EXPERIENCE, Marvel.INTELLIGENCE, Marvel.STRENGTH,
        Marvel.SPEED, Marvel.DURABILITY, Marvel.ENERGY, Marvel.FIGHTING, Marvel.PROFILE_PIC, Marvel.FAVORITE_HANGOUTS,
        Marvel.DETAILED_FILE, Marvel.POWERS_URL, Marvel.City, Marvel.State, Marvel.Zip_Code, Marvel.Latitude, Marvel.Longitude
        ).all()
    
    session.close()
    
    # Create a dictionary from the row data and append to a list of Heroes
    all_Heroes = []
    
    for _id, TARGET, CODENAME, REAL_NAME, GENDER, RELATIONSHIP_STATUS, ALIGNMENT, HEIGHT, WEIGHT, EYECOLOR, HAIRCOLOR, IDENTIFIES_AS, BIRTHPLACE, CITIZENSHIP, EDUCATION, EXPERIENCE, INTELLIGENCE, STRENGTH, SPEED, DURABILITY, ENERGY, FIGHTING, PROFILE_PIC, FAVORITE_HANGOUTS, DETAILED_FILE, POWERS_URL, City, State, Zip_Code, Latitude, Longitude in results:

        Marvel_dict = {}        
        Marvel_dict["UNIQUE ID"] = _id
        Marvel_dict["TARGET"] = TARGET
        Marvel_dict["ALIAS"] = CODENAME
        Marvel_dict["REAL NAME"] = REAL_NAME
        Marvel_dict["GENDER"] = GENDER
        Marvel_dict["RELATIONSHIP STATUS"] = RELATIONSHIP_STATUS
        Marvel_dict["ALIGNMENT"] = ALIGNMENT
        Marvel_dict["HEIGHT"] = HEIGHT
        Marvel_dict["WEIGHT"] = WEIGHT
        Marvel_dict["EYE COLOR"] = EYECOLOR
        Marvel_dict["HAIR COLOR"] = HAIRCOLOR
        Marvel_dict["IDENTIFIES AS"] = IDENTIFIES_AS
        Marvel_dict["BIRTHPLACE"] = BIRTHPLACE
        Marvel_dict["CITIZENSHIP"] = CITIZENSHIP
        Marvel_dict["EDUCATION"] = EDUCATION
        Marvel_dict["EXPERIENCE"] = EXPERIENCE
        Marvel_dict["INTELLIGENCE"] = INTELLIGENCE
        Marvel_dict["STRENGTH"] = STRENGTH
        Marvel_dict["SPEED"] = SPEED
        Marvel_dict["DURABILITY"] = DURABILITY
        Marvel_dict["ENERGY"] = ENERGY
        Marvel_dict["FIGHTING"] = FIGHTING
        Marvel_dict["PICTURE"] = PROFILE_PIC
        Marvel_dict["FAVORITE PLACES"] = FAVORITE_HANGOUTS
        Marvel_dict["DETAILED BIOGRAPHY"] = DETAILED_FILE
        Marvel_dict["POWERS & ABILITIES"] = POWERS_URL
        Marvel_dict["CITY OF ORIGIN"] = City
        Marvel_dict["STATE"] = State
        Marvel_dict["ZIP CODE"] = Zip_Code
        Marvel_dict["LATITUDE"] = Latitude
        Marvel_dict["LONGITUDE"] = Longitude
        
        all_Heroes.append(Marvel_dict)

    return jsonify(all_Heroes)
    #session.close()

####################################################
if __name__ == "__main__":
    app.run()
