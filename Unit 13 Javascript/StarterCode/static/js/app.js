// from data.js
var tableData = data;
// YOUR CODE HERE!

var tbody = d3.select("tbody");

function tables(data){

    tbody.html("");

    data.forEach((dataRow) => {

        var row = tbody.append("tr");
               
        Object.values(dataRow).forEach((value) => {
           var cell = row.append("td");
           cell.text(value);
       });
    })
}

function handleClick(){
    d3.event.preventDefault();

    var date = d3.select("#datetime").property("value");
    var filterData = tableData;

    if(date) {
        filterData = filterData.filter((row) => row.datetime === date);
    }
    tables(filterData);
}

d3.selectAll("#filter-btn").on('click', handleClick);

tables(tableData);