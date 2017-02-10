function draw() {
  createGraphShirts();
}

function getDataShirts(){
  var xhr = new XMLHttpRequest();
  xhr.open('GET', "localhost:5000/shirts", true);
  xhr.send();
  xhr.addEventListener("readystatechange", processRequest, false);

  function processRequest(e){
    if (xhr.readyState == 4 && xhr.status == 200){
      var response = JSON.parse(xhr.responseText);
      return response
    }
  }
}

function createGraphShirts() {
  var shirt_data = getDataShirts();
  var x = d3.scale.linear()
    .domain([0, d3.max(data)])
    .range([0, 420]);

  d3.select(".chart").selectAll("div").data(shirt_data).enter().append("div")
    .style("width", function(d) { return x(d) + "px";})
    .text(function(d) { return d; })

  var chart = d3.select(".chart");
  var bar = chart.selectAll("div");
  var barUpdate = bar.data(data);
  var barEnter = barUpdate.enter().append("div");
  barEnter.style("width", function(d) { return d * 10 + "px"; });
  barEnter.text(function(d) { return d; });
}
draw();
