var svgWidth = 960;
var svgHeight = 500;

var margin = {
  top: 20,
  right: 40,
  bottom: 80,
  left: 100
};

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;


var svg = d3
  .select(".chart")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight);


var chartGroup = svg.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);


var chosenXAxis = "age";


function xScale(Healthdata, chosenXAxis) {
 
  var xLinearScale = d3.scaleLinear()
    .domain([d3.min(Healthdata, d => d[chosenXAxis]) * 0.8,
      d3.max(Healthdata, d => d[chosenXAxis]) * 1.2
    ])
    .range([0, width]);

  return xLinearScale;

}


function renderAxes(newXScale, xAxis) {
  var bottomAxis = d3.axisBottom(newXScale);

  xAxis.transition()
    .duration(1000)
    .call(bottomAxis);

  return xAxis;
}


function renderCircles(circlesGroup, newXScale, chosenXAxis) {

  circlesGroup.transition()
    .duration(1000)
    .attr("cx", d => newXScale(d[chosenXAxis]));

  return circlesGroup;
}


function updateToolTip(chosenXAxis, circlesGroup) {

  var label;

  if (chosenXAxis === "age") {
    label = "Age:";
  }
  else {
    label = "Poverty";
  }

  var toolTip = d3.tip()
    .attr("class", "tooltip")
    .offset([80, -60])
    .html(function(d) {
      return (`${d.age}<br>${label} ${d[chosenXAxis]}`);
    });

  circlesGroup.call(toolTip);

  circlesGroup.on("mouseover", function(data) {
    toolTip.show(data);
  })
  
    .on("mouseout", function(data, index) {
      toolTip.hide(data);
    });

  return circlesGroup;
}


d3.csv("assets/data/data.csv").then(function(Healthdata, err) {
  if (err) throw err;

  
    Healthdata.forEach(function(data) {
    data.age = +data.age;
    data.poverty = +data.poverty;
    data.smokes = +data.smokes;
  });

  
  var xLinearScale = xScale(Healthdata, chosenXAxis);

  
  var yLinearScale = d3.scaleLinear()
    .domain([0, d3.max(Healthdata, d => d.smokes)])
    .range([height, 0]);

  
  var bottomAxis = d3.axisBottom(xLinearScale);
  var leftAxis = d3.axisLeft(yLinearScale);

  
  var xAxis = chartGroup.append("g")
    .classed("x-axis", true)
    .attr("transform", `translate(0, ${height})`)
    .call(bottomAxis);

  
  chartGroup.append("g")
    .call(leftAxis);

  
  var circlesGroup = chartGroup.selectAll("circle")
    .data(Healthdata)
    .enter()
    .append("circle")
    .attr("cx", d => xLinearScale(d[chosenXAxis]))
    .attr("cy", d => yLinearScale(d.smokes))
    .attr("r", 20)
    .attr("fill", "blue")
    .attr("opacity", ".5");

  
  var labelsGroup = chartGroup.append("g")
    .attr("transform", `translate(${width / 2}, ${height + 20})`);

  var ageLabel = labelsGroup.append("text")
    .attr("x", 0)
    .attr("y", 20)
    .attr("value", "age") 
    .classed("active", true)
    .text("Age");

  var povertyLabel = labelsGroup.append("text")
    .attr("x", 0)
    .attr("y", 40)
    .attr("value", "poverty") 
    .classed("inactive", true)
    .text("Poverty");


  chartGroup.append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", 0 - margin.left)
    .attr("x", 0 - (height / 2))
    .attr("dy", "1em")
    .classed("axis-text", true)
    .text("Smokes");

  
  var circlesGroup = updateToolTip(chosenXAxis, circlesGroup);

  
  labelsGroup.selectAll("text")
    .on("click", function() {
      
      var value = d3.select(this).attr("value");
      if (value !== chosenXAxis) {

     
        chosenXAxis = value;

        
        xLinearScale = xScale(Healthdata, chosenXAxis);

      
        xAxis = renderAxes(xLinearScale, xAxis);

        
        circlesGroup = renderCircles(circlesGroup, xLinearScale, chosenXAxis);

        
        circlesGroup = updateToolTip(chosenXAxis, circlesGroup);

        
        if (chosenXAxis === "age") {
          povertyLabel
            .classed("active", true)
            .classed("inactive", false);
          ageLabel
            .classed("active", false)
            .classed("inactive", true);
        }
        else {
          povertyLabel
            .classed("active", false)
            .classed("inactive", true);
          ageLabel
            .classed("active", true)
            .classed("inactive", false);
        }
      }
    });
}).catch(function(error) {
  console.log(error);
});
