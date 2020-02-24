// first we need to load all of the publication data

let pubs_per_year = {};
let years = [];
let npubs = [];

var makePlots = function() {
    pubs_by_year = document.getElementById('pubs-by-year');

    Plotly.newPlot( pubs_by_year, [{
    x: years,
    y: npubs,
    type: 'bar' }], {
    margin: { t: 0 } } );
}


$.getJSON("/data/datasets.json", function( data ) {
    // extract just publication list
    pubs = data.datasets;
    $.each(pubs, function(i, pub){
        if (pubs_per_year.hasOwnProperty(pub.year)) {
            pubs_per_year[pub.year] += 1;
        }
        else {
            pubs_per_year[pub.year] = 1;
        }
    })
    years = Object.keys(pubs_per_year).map(function (x) { return parseInt(x, 10);});
    npubs = Object.values(pubs_per_year);

    makePlots();
})

