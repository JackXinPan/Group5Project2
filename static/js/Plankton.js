  var phyto = "static/data/Zoo.geojson";

  d3.json(phyto).then(function(ZooData) {
    console.log(phytoData.features[0].geometry.coordinates)
    var heatArray = [];

     phytoData.features.forEach(function(point) {
      heatArray.push([point.geometry.coordinates[0], point.geometry.coordinates[1]]);
    });
     

    var heatMap = L.heatLayer(heatArray, {
    radius: 20,
    blur: 3
    }).addTo(myMap);
    
    });


// for (var i = 0; i < cities.length; i++) {
//   // loop through the cities array, create a new marker, push it to the cityMarkers array
//   planktonMarkers.push(
//     L.marker(cities[i].location).bindPopup("<h1>" + cities[i].name + "</h1>")
//   );
// }

// Add all the cityMarkers to a new layer group.
// // Now we can handle them as one group instead of referencing each individually
// var plankton = L.layerGroup(planktonMarkers);

// Create baseMaps for layers
  var satellite = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
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
    
      // Create a baseMaps object
  var baseMaps = {
     "Satellite Map": satellite,
     "Street Map": street
};

// Create an overlay object
var overlayMaps = {
  "Zooplankton": Zoo,
  "Phytoplankton": Phyto
};

// define a map object
var myMap = L.map("map", {
  center: [-33.7749, 120.4194],
  zoom: 3
  layers: [streetmap, plankton]
});

// Pass our map layers into our layer control
// Add the layer control to the map
L.control.layers(baseMaps, overlayMaps, {
  collapsed: false
}).addTo(myMap);



////############################# SPARE COPY

// Only one base layer can be shown at a time
var baseMaps = {
  Street: street,
  Satellite: sateillite
};

// Overlays that may be toggled on or off
var overlayMaps = {
  Plankton: cityLayer
};

// Create map object and set default layers
var myMap = L.map("map", {
  center: [46.2276, 2.2137],
  zoom: 6,
  layers: [light, cityLayer]
});

// Pass our map layers into our layer control
// Add the layer control to the map
L.control.layers(baseMaps, overlayMaps).addTo(myMap);