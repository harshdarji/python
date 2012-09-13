// Phase 1: setup


// high-level parameters
var w=960,h=500,margin=20;
var r=5;

var x=d3.scale.linear().range([margin,w-margin]),
	y=d3.scale.linear().range([h-margin,margin]);

// helper functions

// this one creates a line
var line=d3.svg.line()
	.x(function(d) {return x(d.x);})
	.y(function(d) {return y(d.y);})


// this one does too but with all the points set to the y-axis.
// this would be our default position.
var line0=d3.svg.line()
	.x(function(d) {return x(d.x);})
	.y(function(d) {return y(0);}) 

// this one positions the circles. 
var translate=function(d) {return "translate("+d.x+","+d.y+")";} 


var svg=d3.select("#chart")
		.append("svg").attr("width",w).attr("height",h);


// getting data

d3.csv("data.csv", function(csv) {
	// data processing: filtering
	csv=csv.filter(function(d) {return d.country==="USA";});

	x.domain(d3.extent(csv,function(d) {return d.x;})); // this makes the scales adjust to the data.
	y.domain(d3.extent(csv,function(d) {return d.y;}));

	// creating marks to default position

	svg.selectAll("path").data(csv).enter()
		.append("path")
		.attr("d",line0);	// having interpolators makes this part really straightforward

	svg.selectAll("circle").data(csv).enter()
		.attr("r",r) // the circles' radius is determined by the high-level 
					 // parameter we defined at the top of the program
		.attr("transform",translate); // using our helper function

	// handling interaction

	// we'll attribute a class to the markers on mouesover.
	svg.selectAll("circle")
	.on("mouseover",function(){d3.select(this).classed("highlighted",1);}) 
	// we'll remove the class on mouseout, else the circles will always stay "lit"
	.on("mouseout",function(){d3.select(this).classed("highlighted",0);}) 

	// and initiate...

	svg.selectAll("path").transition().attr("d",line);
	
})