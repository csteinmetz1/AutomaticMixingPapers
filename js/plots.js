// first we need to load all of the publication data

let approachColors = ["#9d3484", "#ec7a8a", "#461a68"];
let categoryColors = ["#151c53", "#1f347e", "#2b609d", "#3993bd", "#65bbca", "#b6dbc5"];

let pubsByYear = {};
let years = [];
let npubs = [];
let cumpubs = [];

let approachCount = {};
let approaches = [];
let approachCounts = [];

let categoryCount = {};
let categories = [];
let categorieCount = [];

var makePlots = function() {

    // top plot - number of pubs per year
    pubsByYearPlot = document.getElementById("pubs-by-year");
    Plotly.newPlot(pubsByYearPlot, [{
    x: years,
    y: npubs,
    marker: {color : "#A9E8DC"},
    type: "bar"}],
    {
    xaxis: {
        autotick : false,
        labels : years.map(String)
        },
    yaxis: {title: "New publications"},
    margin: {
        l: 40,
        r: 40, 
        t: 20, 
        b: 40}},
    {staticPlot: true}
    );

     // top-right plot - cumulative number of pubs per year
     pubsByYearPlot = document.getElementById("cum-pubs-by-year");
     Plotly.newPlot(pubsByYearPlot, [{
     x: years,
     y: cumpubs,
     marker: {color : "#A9E8DC"},
     type: "bar"}],
     {
     xaxis: {
         autotick : false,
         labels : years.map(String)
         },
     yaxis: {title: "Total publications"},
     margin: {
         l: 40,
         r: 40, 
         t: 20, 
         b: 40}},
     {staticPlot: true}
     );

    // pie chart of different approaches
    approachBreakdown = document.getElementById("approach-breakdown");
    Plotly.newPlot(approachBreakdown, [{
    values: approachCounts,
    labels: approaches,
    textinfo: "percent+label",
    textfont: {color : "#FFF"},
    marker: {
        colors : approachColors,
        line: {
            color: '#FFF',
            width: 2
        },
    },
    type: "pie" }], {
    margin: { t: 0 } } 
    );

    // pie chart of different categories
    categoryBreakdown = document.getElementById("category-breakdown");
    Plotly.newPlot(categoryBreakdown, [{
    values: categoryCount,
    labels: categories.sort(),
    textinfo: "percent+label",
    textfont: {color : "#FFF"},
    marker: {
        colors : categoryColors,
        line: {
            color: '#FFF',
            width: 2
        },
    },
    type: "pie" }], {
    margin: { t: 0 } } 
    );

    
}

$.getJSON("data/research.json", function( data ) {
    // extract just publication list
    pubs = data.entries;
    $.each(pubs, function(i, pub){
        if (pubsByYear.hasOwnProperty(pub.year)) {
            pubsByYear[pub.year] += 1;
        }
        else {
            pubsByYear[pub.year] = 1;
        }
        if (approachCount.hasOwnProperty(pub.approach)) {
            approachCount[pub.approach] += 1;
        }
        else {
            approachCount[pub.approach] = 1;
        }
        if (categoryCount.hasOwnProperty(pub.category)) {
            categoryCount[pub.category] += 1;
        }
        else {
            categoryCount[pub.category] = 1;
        }
    })
    years = Object.keys(pubsByYear).map(function (x) { return parseInt(x, 10);});
    npubs = Object.values(pubsByYear);
    npubs.reduce(function(a,b,i) { return cumpubs[i] = a+b; },0);

    approaches = Object.keys(approachCount);
    approachCounts = Object.values(approachCount);

    categories = Object.keys(categoryCount);
    categoryCount = Object.values(categoryCount);

    makePlots();
})

