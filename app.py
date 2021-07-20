import pandas as pd
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template, url_for



#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///planktontestmain4.sqlite")
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
phyto_data = pd.read_sql("SELECT * FROM phytoplankton WHERE Year > 2014"  , conn)
# phyto__color_index_data = pd.read_sql("SELECT * FROM phytoplankton_color_index WHERE year > 2010", conn)
zoo_data = pd.read_sql("SELECT * FROM zooplankton WHERE Year > 2014" , conn)
#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/directories")
def welcome():
    print("Server received request for 'Home' page...")
    return (
        f"Available directories<p>"
        f"/index.html<br/>"
        f"/about.html<br/>"
        f"/map.html<br/>"
        f"/sources.html<br/>"
        f"/visualisations.html<br/>"
        f"/phytoplankton_color_index<b>(DEFUNCT)<br/>"
        f"<span style=font-weight:normal>api/zooplankton<span/><br/>"
        f"/test<br/>"
        f"/test2<br/>"
        f"/api/phytoplankton<br/>"
    )


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/map.html")
def map():
    return render_template("map.html")

@app.route("/sources.html")
def sources():
    return render_template("sources.html")

@app.route("/visualisations.html")
def visualisations():
    return render_template("visualisations.html")

#################################################
# API routes
#################################################
@app.route("/api/phytoplankton")  
def phyto():
    return jsonify((phyto_data.to_dict()))

# @app.route("/phytoplankton_color_index")  
# def phyto_color():
#     return (phyto__color_index_data.to_dict())

@app.route("/test")
def test():
    return (phyto_data["Year"].to_dict())

@app.route("/api/zooplankton")  
def zoo():
    return jsonify((zoo_data.to_dict()))


# #phyto data
# @app.route("/phytoplankton")
# def phytoplankton():
#     return jsonify(Phytoplankton)


# open server
if __name__ == '__main__':
    app.run(debug=True)