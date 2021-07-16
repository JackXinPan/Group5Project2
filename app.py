import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify



#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///planktontest.sqlite")
conn = engine.connect()
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
#Passenger = Base.classes.passenger


# Save references to each table
# Phytoplankton = Base.classes.phytoplankton
# Zooplankton = Base.classes.zooplankton
# PhytoplanktonColor = Base.classes.phytoplankton_color_index



# Query plankton Records in the the Database
phyto_data = pd.read_sql("SELECT * FROM phytoplankton", conn)
phyto__color_index_data = pd.read_sql("SELECT * FROM phytoplankton_color_index", conn)
zoo_data = pd.read_sql("SELECT * FROM zooplankton", conn)
#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    print("Server received request for 'Home' page...")
    return (
        f"Available directories<p>"
        f"/phytoplankton<br/>"
        f"/phytoplankton_color_index<br/>"
        f"/zooplankton"
    )

@app.route("/phytoplankton")  
def phyto():
    return (phyto_data.to_dict())

@app.route("/phytoplankton_color_index")  
def phyto_color():
    return (phyto__color_index_data.to_dict())

@app.route("/zooplankton")  
def zoo():
    return (zoo_data.to_dict())


# #phyto data
# @app.route("/phytoplankton")
# def phytoplankton():
#     return jsonify(Phytoplankton)


# open server
if __name__ == '__main__':
    app.run(debug=True)
