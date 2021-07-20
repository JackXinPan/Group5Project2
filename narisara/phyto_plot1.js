// Plot time series
function unpack(rows, index) {
  return rows.map(function(row) {
    return row[index];
  });
}
var url = "final_phytoplankton_clean.js"
d3.json(url).then(function(data) {

// var test = unpack(data,'Year')
// consol.log(test)

// var Centric diatom = [],
// var Centric diatom = [],
// var Centric diatom = [],

var trace1 = {
    type: "scatter",
    mode: "lines",
    name: 'Route1',
    x: unpack(data, 'Year'),
    y: unpack(data, 'taxon_per_m3'),
    line: {color: '#17BECF'}
}

var trace2 = {
    type: "scatter",
    mode: "lines",
    name: 'Route2',
    x: unpack(data, 'Year'),
    y: unpack(data, 'taxon_per_m3'),
    line: {color: '#7F7F7F'}
}

var trace3 = {
    type: "scatter",
    mode: "lines",
    name: 'Route3',
    x: unpack(data, 'Year'),
    y: unpack(data, 'taxon_per_m3'),
    line: {color: '#7F7F7F'}
}

var data = [trace1,trace2,trace3];

var layout = {
    title: 'Time Series with PhytoPlankton',
    xaxis: {
      autorange: true,
      range: ['2007', '2020'],
      rangeselector: {buttons: [
          {
            count: 1,
            label: '1Y',
            step: 'Year',
            stepmode: 'backward'
          },
          {
            count: 5,
            label: '5Y',
            step: 'Year',
            stepmode: 'backward'
          },
          {step: 'all data'}
        ]},
      rangeslider: {range: ['2007', '2020']},
      type: 'year'
    },
    yaxis: {
      autorange: true,
      range: [1, 10],
      type: 'linear'
    }
  };
  
  Plotly.newPlot('myDiv', data, layout);

})



