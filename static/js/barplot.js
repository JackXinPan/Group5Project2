
// api url
var urlz = "/api/zooplankton_groupby_2020"
function zoo_plot() {
    d3.json(urlz).then(function(zoo_data) {
    // console.log(data);

        var route = Object.values(zoo_data.Route);
        var year = Object.values(zoo_data.Year);
        var taxon_value = Object.values(zoo_data.taxon_per_m3);

            var trace1 = {
            x: route,
            y: taxon_value,
            type: "bar",
            // text: `<b>/m3 on average`,
            marker: {
                color: 'green',
                size: 0,
            },
            };
        //   ​
        var data = [trace1];
        //   ​
        var layout = {
            title: `Average ZooPlankton/m3 for Each CPR Route ${year[0]}`,
            xaxis: { title: "Continuous Plankton Tracker Route" },
            yaxis: { title: "Average Zooplankton (/m3)" }
        };

            Plotly.newPlot('zoo_route_plot', data, layout);
    });
}
var urlp = "/api/phytoplankton_groupby_2020"
function phyto_plot(){
    d3.json(urlp).then(function(phyto_data) {
    // console.log(data);

        var route = Object.values(phyto_data.Route);
        var year = Object.values(phyto_data.Year);
        var taxon_value = Object.values(phyto_data.taxon_per_m3);

            var trace1 = {
            x: route,
            y: taxon_value,
            type: "bar",
            // text: `<b>/m3 on average`,
            marker: {
                color: 'orange',
                size: 0,
            },
            };
        //   ​
        var data = [trace1];
        //   ​
        var layout = {
            title: `Average PhytoPlankton/m3 for Each CPR Route ${year[0]}`,
            xaxis: { title: "Continuous Plankton Tracker Route" },
            yaxis: { title: "Average Phytoplankton (/m3)" }
        };

            Plotly.newPlot('phyto_route_plot', data, layout);
    });
}

    var ul = "/api/phyto_groupby_route"

d3.json(ul).then(function(phyto_data) {
     console.log(phyto_data)
     console.log(Object.entries(phyto_data))
     var x = Object.values(phyto_data.Year).concat(phyto_data.taxon_per_m3)
     console.log(x)
    // var route = phyto_data.Route;
    var year = Object.values(phyto_data.Year);
    // console.log(year)
    function onlyUnique(value, index, self) {
        return self.indexOf(value) === index;
      }
// ordered list of years
    var year_unique = year.filter(onlyUnique).sort().reverse();
      
    console.log(year_unique);

    // for loop to append on subject ids options onto the select element  
    for (var j = 0; j < year_unique.length; j++) {
        d3.select("#selDataset")
            .append("option")
            .attr("value", year_unique[j])
            .text(year_unique[j]);           
        }    
});

function optionChanged() {
    d3.json(ul).then(function(data) {

    //define variable to draw data from 
    var dropdownMenu = d3.select("#selDataset");

    // Assign the value of the dropdown menu option to a variable
    var menuId = dropdownMenu.property("value");   
    console.log(menuId)
    console.log(Object.values(data.Year))
    var urlp = `/api/phytoplankton_groupby_${menuId}`
    var urlz = `/api/phytoplankton_groupby_${menuId}`
    console.log(urlp)

    d3.json(urlp).then(function(phyto_data) {
        // console.log(data);
        
            var route = Object.values(phyto_data.Route);
            var year = Object.values(phyto_data.Year);
            var taxon_value = Object.values(phyto_data.taxon_per_m3);
        
                var trace1 = {
                x: route,
                y: taxon_value,
                type: "bar",
                // text: `<b>/m3 on average`,
                marker: {
                    color: 'orange',
                    size: 0,
                  },
                };
            //   ​
            var data = [trace1];
            //   ​
            var layout = {
                title: `Average PhytoPlankton/m3 for Each CPR Route ${year[0]}`,
                xaxis: { title: "Continuous Plankton Tracker Route" },
                yaxis: { title: "Average Phytoplankton (/m3)" }
            };
        
                Plotly.newPlot('phyto_route_plot', data, layout);
            });

    d3.json(urlz).then(function(zoo_data) {
    // console.log(data);

    var route = Object.values(zoo_data.Route);
    var year = Object.values(zoo_data.Year);
    var taxon_value = Object.values(zoo_data.taxon_per_m3);

        var trace1 = {
        x: route,
        y: taxon_value,
        type: "bar",
        // text: `<b>/m3 on average`,
        marker: {
            color: 'green',
            size: 0,
            },
        };
    //   ​
    var data = [trace1];
    //   ​
    var layout = {
        title: `Average ZooPlankton/m3 for Each CPR Route ${year[0]}`,
        xaxis: { title: "Continuous Plankton Tracker Route" },
        yaxis: { title: "Average Zooplankton (/m3)" }
    };

        Plotly.newPlot('zoo_route_plot', data, layout);
    });

    

    });
}

zoo_plot();
phyto_plot();