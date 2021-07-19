import pandas as pd
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template, url_for



#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///planktontestmain2.sqlite")
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
phyto_data = pd.read_sql("SELECT * FROM phytoplankton"  , conn)
# phyto__color_index_data = pd.read_sql("SELECT * FROM phytoplankton_color_index WHERE year > 2010", conn)
zoo_data = pd.read_sql("SELECT * FROM zooplankton" , conn)
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
        f"/index.html<br/>"
        f"/about.html<br/>"
        f"/map.html<br/>"
        f"/sources.html<br/>"
        f"/visualisations.html<br/>"
        f"/phytoplankton<br/>"
        f"/phytoplankton_color_index<b>(DEFUNCT)<br/>"
        f"<span style=font-weight:normal>/zooplankton<span/><br/>"
        f"/test<br/>"
        f"/test2<br/>"
        f"/api/phytoplankton<br/>"
    )


@app.route("/index.html")
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
@app.route("/phytoplankton")  
def phyto():
    return jsonify((phyto_data.to_dict()))

# @app.route("/phytoplankton_color_index")  
# def phyto_color():
#     return (phyto__color_index_data.to_dict())

@app.route("/test")
def test():
    return (phyto_data["Year"].to_dict())

@app.route("/zooplankton")  
def zoo():
    return jsonify((zoo_data.to_dict()))


# #phyto data
# @app.route("/phytoplankton")
# def phytoplankton():
#     return jsonify(Phytoplankton)

#################################################
# Database Setup
#################################################


# from flask_sqlalchemy import SQLAlchemy

# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///planktontestmain2.sqlite"

# db = SQLAlchemy(app)

# #################################################
# # Models Setup
# #################################################

# class Phytoplankton(db.Model):
#     __tablename__ = 'phytoplankton'

#     id = db.Column(db.Integer, primary_key=True)
#     year = db.Column(db.Float)
#     lat = db.Column(db.Float)
#     lon = db.Column(db.Float)
#     taxon_name = db.Column(db.String(64))
#     taxon_per_m3 = db.column(db.Float)

#     def __repr__(self):
#         return '<Phytoplankton %r>' % (self.taxon_name)

# #################################################
# # API routes
# #################################################
# @app.route("/test2")
# def test2():
#     results = db.session.query(Phytoplankton, Phytoplankton.lat, Phytoplankton.lon, Phytoplankton.taxon_name, Phytoplankton.taxon_per_m3 ).all()
#     return jsonify([result[3] for result in results])

# @app.route("/api/phytoplankton")
# def pals():
#     results = db.session.query(Phytoplankton, Phytoplankton.lat, Phytoplankton.lon, Phytoplankton.taxon_name, Phytoplankton.taxon_per_m3 ).all()

#     hover_text = [result[0] for result in results]
#     lat = [result[1] for result in results]
#     lon = [result[2] for result in results]
#     taxon_name = [result[3] for result in results]
#     taxon_per_m3 = [result[4] for result in results]

#     phytoplankton_data = [{
#         "type": "scattergeo",
#         "locationmode": "USA-states",
#         "lat": lat,
#         "lon": lon,
#         "taxon_name": taxon_name,
#         "taxon_per_m3": taxon_per_m3,
#         "text": hover_text,
#         "hoverinfo": "text",
#         "marker": {
#             "size": 15,
#             "line": {
#                 "color": "rgb(8,8,8)",
#                 "width": 1
#             },
#         }
#     }]

#     return jsonify(phytoplankton_data)

# open server
if __name__ == '__main__':
    app.run(debug=True)