 
    // Map initialization 
    var map = L.map('map').setView([56.8796, 24.6032], 8);
   
    function getColor(d) {
        return d > 2000.0 ? '#800026' :
               d > 1000.0  ? '#BD0026' :
               d > 500.0  ? '#E31A1C' :
               d > 200.0  ? '#FC4E2A' :
               d > 100.0   ? '#FD8D3C' :
               d > 50.0   ? '#FEB24C' :
               d > 20.0   ? '#FED976' :
                          '#FFEDA0';
    }
    var geojson;
    // ... our listeners
    geojson = L.geoJson(brs, {style: style}).addTo(map);
    
    function highlightFeature(e) {
        var layer = e.target;
    
        layer.setStyle({
            weight: 5,
            color: '#666',
            dashArray: '',
            fillOpacity: 0.7
        });
    
        layer.bringToFront();
    }
 
  
    function style(feature) {
        return {
            fillColor: getColor(feature.properties.PLAT_KVKM),
            weight: 2,
            opacity: 1,
            color: 'white',
            dashArray: '3',
            fillOpacity: 0.7
        };
    }
    
    L.geoJson(brs, {style: style}).addTo(map);



    var Stamen_Toner = L.tileLayer('https://stamen-tiles-{s}.a.ssl.fastly.net/toner/{z}/{x}/{y}{r}.{ext}', {
        attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        subdomains: 'abcd',
        minZoom: 0,
        maxZoom: 20,
        ext: 'png'
    });
    Stamen_Toner.addTo(map);


//     map.on('click', function (e) {
//         var info = L.control();

// info.onAdd = function (map) {
//     this._div = L.DomUtil.create('div', 'info'); // create a div with a class "info"
//     this.update();
//     return this._div;
// };

// // method that we will use to update the control based on feature properties passed
// info.update = function (props) {
//     this._div.innerHTML = '<h4>US Population Density</h4>' +  (props ?
//         '<b>' + props.name + '</b><br />' + props.density + ' people / mi<sup>2</sup>'
//         : 'Hover over a state');
// };

// info.addTo(map);
//     });
function highlightFeature(e) {
    var layer = e.target;

    layer.setStyle({
        weight: 5,
        color: '#666',
        dashArray: '',
        fillOpacity: 0.7
    });

    layer.bringToFront();
    info.update(layer.feature);
}

function resetHighlight(e) {
    geojson.resetStyle(e.target);
    info.update();
}



function zoomToFeature(e) {
    map.fitBounds(e.target.getBounds());
}

function onEachFeature(feature, layer) {
    layer.on({
        mouseover: highlightFeature,
        mouseout: resetHighlight,
        dblclick: zoomToFeature
    });
}

geojson = L.geoJson(brs, {
    style: style,
    onEachFeature: onEachFeature
}).addTo(map);

var info = L.control();

info.onAdd = function (map) {
    this._div = L.DomUtil.create('div', 'info'); // create a div with a class "info"
    this.update();
    return this._div;
};
function nosaukums(name)
{
    var saukums = name;
    var output =  " ";
    
     for (let x in loc) {
       
        if (loc[x].Adrese.includes(saukums.slice(0, -3)))
        {
            
            output+=loc[x].ObjektaNosaukums;
            output+= "<br>";
        }
     }
     
     return output;
}
// method that we will use to update the control based on feature properties passed
info.update = function (props) {
    var bonuss;
    if (props)
   { var n = props.properties.NOSAUKUMS;
    var bonuss = nosaukums(n);}
    this._div.innerHTML = '<h4>Informācija</h4>' +  (props ?
        '<b>' + props.properties.PLAT_KVKM + '</b><br />' +'<b>'+ props.properties.NOSAUKUMS + '</b><br />'+ 
        '<b>Šeit atrodas:</b><br>'+ bonuss +'<br />' +
         ''
        : 'Nosaki info');
};

info.addTo(map);


