import pandas as pd
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template, url_for



#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///planktontestmain1.sqlite")
conn = engine.connect()
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)



# phyto_routes.to_sql("phytoplankton", conn,)
# phyto_taxon_group.to_sql("phytoplankton_taxon_group", conn,)
# phyto_years.to_sql("phytoplankton_years", conn,)
# zoo_routes.to_sql("zooplankton", conn,)
# zoo_taxon_group.to_sql("zooplankton_taxon_group", conn,)
# zoo_years.to_sql("zooplankton_years", conn,)







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
        f"Available directories:<p>"
        
        f"/about.html<br/>"
        f"/map.html<br/>"
        f"/sources.html<br/>"
        f"/visualisations.html<br/><p>"

        f"/api/zooplankton<span/><br/>"
        f"/api/phytoplankton<br/>"
        f"/api/phyto_years<br/>"
        f"/api/phyto_groupby_route (BEWARE taxon_per_m3 is the mean value for year)<br/>"
        f"/api/zoo_groupby_route (BEWARE taxon_per_m3 is the mean value for year)<br/>"
        f"/api/zoo_years<br/>"
        f"/api/phyto_taxon_group<br/>"
        f"/api/zoo_taxon_group<br/>"       
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
# API routes HEATMAP
#################################################

# Query plankton Records in the the Database
phyto_data = pd.read_sql("SELECT * FROM phytoplankton WHERE Year > 2016", conn)
# phyto__color_index_data = pd.read_sql("SELECT * FROM phytoplankton_color_index WHERE year > 2010", conn)
zoo_data = pd.read_sql("SELECT * FROM zooplankton WHERE Year > 2016", conn)


@app.route("/api/phytoplankton")  
def phyto():
    return jsonify((phyto_data.to_dict()))

@app.route("/api/zooplankton")  
def zoo():
    return jsonify((zoo_data.to_dict()))


#################################################
# API routes for Route Barcharts (done yearly as data is too big)
#################################################

# zoo_groupby_route.to_sql("zooplankton_groupby_route", conn,)
# phyto_groupby_route.to_sql("phytoplankton_groupby_route", conn,)


phyto_groupby_route = pd.read_sql("SELECT * FROM phytoplankton_groupby_route", conn)
zoo_groupby_route = pd.read_sql("SELECT * FROM zooplankton_groupby_route", conn)

@app.route("/api/phyto_groupby_route")
def pgroupby_route():
    return jsonify((phyto_groupby_route.to_dict()))

@app.route("/api/zoo_groupby_route")
def zgroupby_route():
    return jsonify((zoo_groupby_route.to_dict()))


# phyto_2020 = pd.read_sql("SELECT * FROM phytoplankton WHERE Year = 2020", conn)
phyto_2019 = pd.read_sql("SELECT * FROM phytoplankton WHERE Year = 2019", conn)
# phyto_2018 = pd.read_sql("SELECT * FROM phytoplankton WHERE Year = 2018", conn)
# phyto_2017 = pd.read_sql("SELECT * FROM phytoplankton WHERE Year = 2017", conn)

# zoo_2020 = pd.read_sql("SELECT * FROM zooplankton WHERE Year = 2020", conn)
zoo_2019 = pd.read_sql("SELECT * FROM zooplankton WHERE Year = 2019", conn)
# zoo_2018 = pd.read_sql("SELECT * FROM zooplankton WHERE Year = 2018", conn)
# zoo_2017 = pd.read_sql("SELECT * FROM zooplankton WHERE Year = 2017", conn)


# @app.route("/api/phytoplankton2020")
# def phyto2020():
#     return jsonify((phyto_2020.to_dict()))

@app.route("/api/phytoplankton2019")
def phyto2019():
    return jsonify((phyto_2019.to_dict()))

# @app.route("/api/phytoplankton2018")
# def phyto2018():
#     return jsonify((phyto_2018.to_dict()))

# @app.route("/api/phytoplankton2017")
# def phyto2017():
#     return jsonify((phyto_2017.to_dict()))



# @app.route("/api/zooplankton2020")
# def zoo2020():
#     return jsonify((zoo_2020.to_dict()))

@app.route("/api/zooplankton2019")
def zoo2019():
    return jsonify((zoo_2019.to_dict()))

# @app.route("/api/zooplankton2018")
# def zoo2018():
#     return jsonify((zoo_2018.to_dict()))

# @app.route("/api/zooplankton2017")
# def zoo2017():
#     return jsonify((zoo_2017.to_dict()))

#################################################
# API routes for Year Barcharts (only 4 main routes to be able to go across year)
#################################################

phyto_years = pd.read_sql("SELECT * FROM phytoplankton_years WHERE Year > 2016", conn)
# Query plankton Records in the the Database
zoo_years = pd.read_sql("SELECT * FROM zooplankton_years WHERE Year > 2016", conn)

@app.route("/api/phyto_years")
def phyto_years_f():
    return jsonify((phyto_years.to_dict()))


@app.route("/api/zoo_years")
def zoo_years_f():
    return jsonify((zoo_years.to_dict()))

#################################################
# API routes for Taxon Groups - For biodiversity reasons
#################################################


phyto_taxon = pd.read_sql("SELECT * FROM phytoplankton_taxon_group WHERE Year > 2016", conn)
# Query plankton Records in the the Database
zoo_taxon = pd.read_sql("SELECT * FROM zooplankton_taxon_group WHERE Year > 2016", conn)


@app.route("/api/phyto_taxon_group")
def phyto_taxon_group():
    return jsonify((phyto_taxon.to_dict()))


@app.route("/api/zoo_taxon_group")
def zoo_taxon_group():
    return jsonify((zoo_taxon.to_dict()))



# open server
if __name__ == '__main__':
    app.run(debug=True)