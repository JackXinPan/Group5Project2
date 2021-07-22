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
        f"/api/phyto_groupby_route (BEWARE taxon_per_m3 is the median value for year)<br/>"
        f"/api/zoo_groupby_route (BEWARE taxon_per_m3 is the median value for year)<br/>"
        f"/api/zoo_years<br/>"
        f"/api/phyto_taxon_group<br/>"
        f"/api/zoo_taxon_group<br/>"       
    )


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/boxplots.html")
def boxplots():
    return render_template("boxplots.html")

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
# API routes TAXON GRAPH
#################################################
# zoo_groupby_taxon.to_sql("zooplankton_groupby_taxon", conn,)
# phyto_groupby_taxon.to_sql("phytoplankton_groupby_taxon", conn,)

phyto_group_taxon = pd.read_sql("SELECT * FROM phytoplankton_groupby_taxon", conn)
zoo_group_taxon = pd.read_sql("SELECT * FROM zooplankton_groupby_taxon", conn)

@app.route("/api/phyto_group_taxon")  
def phyto_g_tax():
    return jsonify((phyto_group_taxon.to_dict()))

@app.route("/api/zoo_group_taxon")  
def zoo_g_tax():
    return jsonify((zoo_group_taxon.to_dict()))



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

#################################################
# I know
#################################################
phyto_2020 = pd.read_sql("SELECT * FROM phytoplankton_groupby_route WHERE Year = 2020", conn)
phyto_2019 = pd.read_sql("SELECT * FROM phytoplankton_groupby_route WHERE Year = 2019", conn)
phyto_2018 = pd.read_sql("SELECT * FROM phytoplankton_groupby_route WHERE Year = 2018", conn)
phyto_2017 = pd.read_sql("SELECT * FROM phytoplankton_groupby_route WHERE Year = 2017", conn)
phyto_2016 = pd.read_sql("SELECT * FROM phytoplankton_groupby_route WHERE Year = 2016", conn)
phyto_2015 = pd.read_sql("SELECT * FROM phytoplankton_groupby_route WHERE Year = 2015", conn)
phyto_2014 = pd.read_sql("SELECT * FROM phytoplankton_groupby_route WHERE Year = 2014", conn)
phyto_2013 = pd.read_sql("SELECT * FROM phytoplankton_groupby_route WHERE Year = 2013", conn)
phyto_2012 = pd.read_sql("SELECT * FROM phytoplankton_groupby_route WHERE Year = 2012", conn)
phyto_2011 = pd.read_sql("SELECT * FROM phytoplankton_groupby_route WHERE Year = 2011", conn)
phyto_2010 = pd.read_sql("SELECT * FROM phytoplankton_groupby_route WHERE Year = 2010", conn)
phyto_2009 = pd.read_sql("SELECT * FROM phytoplankton_groupby_route WHERE Year = 2009", conn)
phyto_2008 = pd.read_sql("SELECT * FROM phytoplankton_groupby_route WHERE Year = 2008", conn)
phyto_2007 = pd.read_sql("SELECT * FROM phytoplankton_groupby_route WHERE Year = 2007", conn)

zoo_2020 = pd.read_sql("SELECT * FROM zooplankton_groupby_route WHERE Year = 2020", conn)
zoo_2019 = pd.read_sql("SELECT * FROM zooplankton_groupby_route WHERE Year = 2019", conn)
zoo_2018 = pd.read_sql("SELECT * FROM zooplankton_groupby_route WHERE Year = 2018", conn)
zoo_2017 = pd.read_sql("SELECT * FROM zooplankton_groupby_route WHERE Year = 2017", conn)
zoo_2016 = pd.read_sql("SELECT * FROM zooplankton_groupby_route WHERE Year = 2016", conn)
zoo_2015 = pd.read_sql("SELECT * FROM zooplankton_groupby_route WHERE Year = 2015", conn)
zoo_2014 = pd.read_sql("SELECT * FROM zooplankton_groupby_route WHERE Year = 2014", conn)
zoo_2013 = pd.read_sql("SELECT * FROM zooplankton_groupby_route WHERE Year = 2013", conn)
zoo_2012 = pd.read_sql("SELECT * FROM zooplankton_groupby_route WHERE Year = 2012", conn)
zoo_2011 = pd.read_sql("SELECT * FROM zooplankton_groupby_route WHERE Year = 2011", conn)
zoo_2010 = pd.read_sql("SELECT * FROM zooplankton_groupby_route WHERE Year = 2010", conn)
zoo_2009 = pd.read_sql("SELECT * FROM zooplankton_groupby_route WHERE Year = 2009", conn)
zoo_2008 = pd.read_sql("SELECT * FROM zooplankton_groupby_route WHERE Year = 2008", conn)
zoo_2007 = pd.read_sql("SELECT * FROM zooplankton_groupby_route WHERE Year = 2007", conn)


@app.route("/api/phytoplankton_groupby_2020")
def phyto2020():
    return jsonify((phyto_2020.to_dict()))

@app.route("/api/phytoplankton_groupby_2019")
def phyto2019():
    return jsonify((phyto_2019.to_dict()))

@app.route("/api/phytoplankton_groupby_2018")
def phyto2018():
    return jsonify((phyto_2018.to_dict()))

@app.route("/api/phytoplankton_groupby_2017")
def phyto2017():
    return jsonify((phyto_2017.to_dict()))

@app.route("/api/phytoplankton_groupby_2016")
def phyto2016():
    return jsonify((phyto_2016.to_dict()))

@app.route("/api/phytoplankton_groupby_2015")
def phyto2015():
    return jsonify((phyto_2015.to_dict()))

@app.route("/api/phytoplankton_groupby_2014")
def phyto2014():
    return jsonify((phyto_2014.to_dict()))

@app.route("/api/phytoplankton_groupby_2013")
def phyto2013():
    return jsonify((phyto_2013.to_dict()))

@app.route("/api/phytoplankton_groupby_2012")
def phyto2012():
    return jsonify((phyto_2012.to_dict()))

@app.route("/api/phytoplankton_groupby_2011")
def phyto2011():
    return jsonify((phyto_2011.to_dict()))

@app.route("/api/phytoplankton_groupby_2010")
def phyto2010():
    return jsonify((phyto_2010.to_dict()))

@app.route("/api/phytoplankton_groupby_2009")
def phyto2009():
    return jsonify((phyto_2009.to_dict()))

@app.route("/api/phytoplankton_groupby_2008")
def phyto2008():
    return jsonify((phyto_2008.to_dict()))

@app.route("/api/phytoplankton_groupby_2007")
def phyto2007():
    return jsonify((phyto_2007.to_dict()))





@app.route("/api/zooplankton_groupby_2020")
def zoo2020():
    return jsonify((zoo_2020.to_dict()))

@app.route("/api/zooplankton_groupby_2019")
def zoo2019():
    return jsonify((zoo_2019.to_dict()))

@app.route("/api/zooplankton_groupby_2018")
def zoo2018():
    return jsonify((zoo_2018.to_dict()))

@app.route("/api/zooplankton_groupby_2017")
def zoo2017():
    return jsonify((zoo_2017.to_dict()))

@app.route("/api/zooplankton_groupby_2016")
def zoo2016():
    return jsonify((zoo_2016.to_dict()))

@app.route("/api/zooplankton_groupby_2015")
def zoo2015():
    return jsonify((zoo_2015.to_dict()))

@app.route("/api/zooplankton_groupby_2014")
def zoo2014():
    return jsonify((zoo_2014.to_dict()))

@app.route("/api/zooplankton_groupby_2013")
def zoo2013():
    return jsonify((zoo_2013.to_dict()))

@app.route("/api/zooplankton_groupby_2012")
def zoo2012():
    return jsonify((zoo_2012.to_dict()))

@app.route("/api/zooplankton_groupby_2011")
def zoo2011():
    return jsonify((zoo_2011.to_dict()))

@app.route("/api/zooplankton_groupby_2010")
def zoo2010():
    return jsonify((zoo_2010.to_dict()))

@app.route("/api/zooplankton_groupby_2009")
def zoo2009():
    return jsonify((zoo_2009.to_dict()))

@app.route("/api/zooplankton_groupby_2008")
def zoo2008():
    return jsonify((zoo_2008.to_dict()))

@app.route("/api/zooplankton_groupby_2007")
def zoo2007():
    return jsonify((zoo_2007.to_dict()))

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