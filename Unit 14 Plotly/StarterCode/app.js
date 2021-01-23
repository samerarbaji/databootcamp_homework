function retreiveData(sample) {
    d3.json("samples.json").then(data=> {
        console.log(data)
    });
    };
    retreiveData();



    function buildCharts(sample) {

       
        d3.json("samples.json").then((data) => {
          var samples= data.samples;
          var resultsarray= samples.filter(sampleobject => sampleobject.id == sample);
          var result= resultsarray[0]
      
          var ids = result.otu_ids;
          var labels = result.otu_labels;
          var values = result.sample_values;
      
      
        
          var bubblelayout = {
            margin: { t: 0 },
            xaxis: { title: "Id's" },
            hovermode: "closest",
            };
      
            var trace1 = [
            {
              x: ids,
              y: values,
              text: labels,
              mode: "markers",
              marker: {
                color: ids,
                size: values,
                }
            }
          ];
      
          Plotly.plot("bubble", trace1, bubblelayout);
      
        
          
          var trace2 =[
            {
              y:ids.slice(0, 10).map(otuID => `OTU ${otuID}`).reverse(),
              x:values.slice(0,10).reverse(),
              text:labels.slice(0,10).reverse(),
              type:"bar",
              orientation:"h"
      
            }
          ];
      
          var barLayout = {
            title: "Top 10 OTU's",
            margin: { t: 30, l: 150 }
          };
      
          Plotly.newPlot("bar", trace2, barLayout);
        });
      }
       
      function builddata(sample) {
        d3.json("samples.json").then((data) => {
          var metadata= data.metadata;
          var resultsarray= metadata.filter(sampleobject => sampleobject.id == sample);
          var result= resultsarray[0]
          var PANEL = d3.select("#sample-metadata");
          PANEL.html("");
          Object.entries(result).forEach(([key, value]) => {
            PANEL.append("h6").text(`${key}: ${value}`);
          });
    
          
        
        });
      }
       
      function dash() {
        
        var selector = d3.select("#selDataset");
      
        
        d3.json("samples.json").then((data) => {
          var sampleNames = data.names;
          sampleNames.forEach((sample) => {
            selector
              .append("option")
              .text(sample)
              .property("value", sample);
          });
      
          
          const firstSample = sampleNames[0];
          buildCharts(firstSample);
          builddata(firstSample);
        });
      }
      
      function newoption(newSample) {
     
        buildCharts(newSample);
        buildMetadata(newSample);
      }
      
     
      dash();