
var ul = "/api/phyto_groupby_route"

// d3.json(ul).then(function(phyto_data) {
//     // console.log(phyto_data)
//     var route = Object.values(phyto_data.Route);
//     var year = Object.values(phyto_data.Year);
//     var taxon_mean = Object.values(phyto_data.taxon_per_m3);
//     // console.log(taxon_mean)
//     var phyto_array = [];
//     Object.keys(year).forEach(function(key) {
//         phyto_array.push([route[key], year[key], taxon_mean[key]]);
//         });
//     console.log(phyto_array)
    
//     // Create a custom filtering function
//     function year20(phyto) {
//         return phyto.year = 2020;
//     }
//   // filter() uses the custom function as its argument
//     var test = phyto_array.filter(year20);
//     console.log(test)
// });


// api url
var urlz = "/api/zooplankton2019"

d3.json(urlz).then(function(zoo_data) {
// console.log(data);

    var route = Object.values(zoo_data.Route);
    var year = Object.values(zoo_data.Year);
    var taxon_value = Object.values(zoo_data.taxon_per_m3);

        var trace1 = {
        x: route,
        y: taxon_value,
        type: "bar",
        text: `<b>/m3 on average`,
        marker: {
            color: 'green',
            size: 0,
          },
        };
    //   ​
    var data = [trace1];
    //   ​
    var layout = {
        title: `Amount of ZooPlankton for Each CPR Route ${year[0]}`,
        xaxis: { title: "Continuous Plankton Tracker Route" },
        yaxis: { title: "Zooplankton" }
    };

        Plotly.newPlot('zoo_route_plot', data, layout);
    });

var urlp = "/api/phytoplankton2019"

d3.json(urlp).then(function(phyto_data) {
// console.log(data);

    var route = Object.values(phyto_data.Route);
    var year = Object.values(phyto_data.Year);
    var taxon_value = Object.values(phyto_data.taxon_per_m3);

        var trace1 = {
        x: route,
        y: taxon_value,
        type: "bar",
        text: `<b>/m3 on average`,
        marker: {
            color: 'orange',
            size: 0,
          },
        };
    //   ​
    var data = [trace1];
    //   ​
    var layout = {
        title: `Amount of PhytoPlankton for Each CPR Route ${year[0]}`,
        xaxis: { title: "Continuous Plankton Tracker Route" },
        yaxis: { title: "Phytoplankton" }
    };

        Plotly.newPlot('phyto_route_plot', data, layout);
    });