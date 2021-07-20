// heat map for Zooplankton layer
var zoo = "static/data/zoo.geojson";
  
  d3.json(zoo).then(function(zooData) {
    console.log(zooData.features[0].geometry.coordinates)
    var heatArrayZoo = [];

    zooData.features.forEach(function(point) {
    heatArrayZoo.push([point.geometry.coordinates[0], point.geometry.coordinates[1], point.properties.taxon_per_m3]);
    });
     
    var zooHeatMap = L.heatLayer(heatArrayZoo, {
    radius: 15,
    blur: 3,
    // max: 50
  }) 
  var phyto = "static/data/phyto.geojson";

  d3.json(phyto).then(function(phytoData) {
    console.log(phytoData.features[0].geometry.coordinates)
    var heatArray = [];

    phytoData.features.forEach(function(point) {
    heatArray.push([point.geometry.coordinates[0], point.geometry.coordinates[1], point.properties.taxon_per_m3]);
    });
     
    var phytoHeatMap = L.heatLayer(heatArray, {
    radius: 20,
    blur: 1, 
    max: 5000
    })

    // Create baseMaps for layers
  var satellite = L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    tileSize: 512,
    maxZoom: 18,
    zoomOffset: -1,
    id: "mapbox/satellite-v9",
    accessToken: API_KEY
  });
  
   var street = L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
      attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
      tileSize: 512,
      maxZoom: 18,
      zoomOffset: -1,
      id: "mapbox/streets-v11",
      accessToken: API_KEY
    });

        // Create a baseMaps object
  var baseMaps = {
     "Satellite Map": satellite,
     "Street Map": street
};

// Create an overlay object
var overlayMaps = {
  "Zooplankton": zooHeatMap,
  "Phytoplankton": phytoHeatMap
};

// define a map object
var myMap = L.map("map", {
  center: [-33.7749, 120.4194],
  zoom: 3,
  layers: [street, zooHeatMap]
});

// Pass our map layers into our layer control
// Add the layer control to the map
L.control.layers(baseMaps, overlayMaps, {
  collapsed: false
}).addTo(myMap);
    });  
    });