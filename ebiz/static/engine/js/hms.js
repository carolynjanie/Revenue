function our_layers(map,options){

	        	 var osm = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
					maxZoom: 17,
					attribution: 'Map data: &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
				});
	        	 var grayscale = L.tileLayer('http://{s}.tiles.wmflabs.org/bw-mapnik/{z}/{x}/{y}.png', {
				      maxZoom: 18,
				      attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
				    });
	        	 var osmt = L.tileLayer('https://stamen-tiles-{s}.a.ssl.fastly.net/toner/{z}/{x}/{y}{r}.{ext}', {
					attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
					subdomains: 'abcd',
					minZoom: 0,
					maxZoom: 20,
					ext: 'png'
				});

	        	var counties = new L.GeoJSON.AJAX("{% url 'nairobi' %}",{
	        		style: function colors(feature)
		        	{
		        		switch(feature.properties.district)
		        		{
		        			case 'NAIROBI':
		        			  return{
		        			  	color: 'magenta',
		        			  	fillOpacity: 1
		        			  }; 
		        		break;
						}
					}});
					

		         var subcounties = new L.GeoJSON.AJAX("{% url 'subcounties' %}",
				{
					style: function colors(feature)
		        	{
		        		switch(feature.properties.division)
		        		{
		        			case 'CENTRAL':
		        			  return{
		        			  	color: 'yellow',
		        			  	fillOpacity: 1
		        			  }; 
		        			  break;
		        	    }
		        	    switch(feature.properties.division)
		        		{
		        			case 'KIBERA':
		        			  return{
		        			  	color: 'orange',
		        			  	fillOpacity: 1
		        			  }; 
		        			  break;
		        	    }
		        	    switch(feature.properties.division)
		        		{
		        			case 'PUMWANI':
		        			  return{
		        			  	color: 'red',
		        			  	fillOpacity: 1
		        			  }; 
		        			  break;
		        	    }
		        	    switch(feature.properties.division)
		        		{
		        			case 'MAKADARA':
		        			  return{
		        			  	color: 'green',
		        			  	fillOpacity: 1
		        			  }; 
		        			  break;
		        	    }
		        	    switch(feature.properties.division)
		        		{
		        			case 'DAGORETTI':
		        			  return{
		        			  	color: 'blue',
		        			  	fillOpacity: 1
		        			  }; 
		        			  break;
		        	    }
		        	    switch(feature.properties.division)
		        		{
		        			case 'PARKLANDS/WESTLANDS':
		        			  return{
		        			  	color: 'black',
		        			  	fillOpacity: 1
		        			  }; 
		        			  break;
		        	    }
		        	    switch(feature.properties.division)
		        	    {
		        			case 'KASARANI':
		        			  return{
		        			  	color: 'purple',
		        			  	fillOpacity: 1
		        			  }; 
		        			  break;
		        	    }
						switch(feature.properties.division)
		        	    {
		        			case 'EMBAKASI':
		        			  return{
		        			  	color: 'pink',
		        			  	fillOpacity: 1
		        			  }; 
		        			  break;
		        	    }
		        	}, 
		        	onEachFeature: function(feature,layer)
		    	    {
		    		layer.bindPopup(feature.properties.division.toString());
                    }
                
		        });

		        var counties = L.layerGroup([counties]);
		        var subcounties = L.layerGroup([subcounties]);

				var baseLayers = {
			    	"OSM Topo": osm,
			    	"Grayscale": grayscale,
			    	"OSM Thunder": osmt
			    };


			    var groupedOverlays = {
			    			"MyCounties": counties,
			    			"MySubCounties": subcounties,
			    			}
			 

     L.control.layers(baseLayers, groupedOverlays).addTo(map);

			    L.Routing.control({
				  waypoints: [
				    L.latLng(0, 39),
				    L.latLng(1, 37)
				  ]
				}).addTo(map);


		var searchLayer = L.geoJson().addTo(map);
		//... adding data in searchLayer ...
		L.map('map', { searchControl: {layer: searchLayer} });

		};
{% leaflet_map "gis" callback="window.our_layers" %}