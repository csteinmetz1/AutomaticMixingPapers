$(document).ready(function() {
  $("body").tooltip({ selector: '[data-toggle=tooltip]' });
});

$(document).ready(function () {
  // load table data from json file
  $.getJSON("/data/datasets.json", function( data ) {
    
    // column ordering based on HTML table header
    var cols = data.columns;

    // get table from DOM
    var table = document.getElementById("dt");
    var header = table.createTHead();
    var thead = header.insertRow(0);

    // load columns into HTML table header
    for (c=0; c<cols.length; c++) {
      var cell = thead.insertCell(c);
      cell.innerHTML = "<b>" + Object.values(cols[c])[0] + "</b>";
    }

    // get dataset objects to populate table
    var datasets = data.datasets;

    // get table body
    var tbody = table.getElementsByTagName('tbody')[0];

    // iterate over dataset entries and add rows
    for (r=0; r<datasets.length; r++) {
      var row = tbody.insertRow(r);
      for (c=0; c<cols.length; c++) {
        var cell = row.insertCell(c);
        var col = Object.keys(cols[c])[0];
        // conditional formatting
        if (col == "bibtex") {
          // load the proper bibtexr file in here
          var a = document.createElement('a');
          var linkText = document.createTextNode(col);
          a.appendChild(linkText);
          a.setAttribute("class", "btn btn-light btn-sm");
          a.setAttribute("data-toggle", "tooltip");
          a.setAttribute("data-placement", "right");
          a.setAttribute("data-original-title", "Copy")
          a.setAttribute("value", "bibtex")
          cell.appendChild(a);
        }
        else if ((col == "code" || col == "demo") && datasets[r][col] != "")  {
          var a = document.createElement('a');
          var linkText = document.createTextNode(col);
          a.appendChild(linkText);
          a.setAttribute("class", "btn btn-light btn-sm");
          a.title = datasets[r].name + " " + col;
          a.href = datasets[r][col];
          a.target = "_blank";
          cell.appendChild(a);
        }
        else if (col == "title") {
          var a = document.createElement('a');
          var linkText = document.createTextNode(datasets[r][col]);
          a.appendChild(linkText);
          //a.title = datasets[r].name + " " + col;
          a.href = datasets[r]["pdf"];
          a.target = "_blank";
          a.classList.add("font-weight-normal");
          cell.appendChild(a);
        }
        else {
          cell.innerHTML = datasets[r][col];
        }
      }
    } 
    // convert table to interactive table
    $('#dt').DataTable();
    $('.dataTables_length').addClass('bs-select');
  });
  
  $('a.toggle-vis').on( 'click', function (e) {
    e.preventDefault();

    var table = $('#dt').DataTable();

    // Get the column API object
    table.search( $(this).attr('data-term') ).draw();

    // Toggle the visibility
    //column.visible( ! column.visible() );
} );
});



