

// MARKER CONFIG
var iconFeature = new ol.Feature({
	geometry: new ol.geom.Point([637125.42195, 8172199.19090669]),
	name: 'Null Island',
	population: 4000,
	rainfall: 500
});

var iconStyle = new ol.style.Style({
  image: new ol.style.Icon(/** @type {olx.style.IconOptions} */ ({
    anchor: [0.5, 46],
    anchorXUnits: 'fraction',
    anchorYUnits: 'pixels',
    opacity: 0.75,
    src: marker_image
  }))
});

iconFeature.setStyle(iconStyle);
// MARKER LAYER
var vectorSource = new ol.source.Vector({
  features: [iconFeature]
});

var vectorLayer = new ol.layer.Vector({
  source: vectorSource
});

// OSM LAYER
var osmLayer = new ol.layer.Tile({
	source: new ol.source.OSM()
});

// MAP POSITION
var mapView = new ol.View({
	center: [0, 0],
	zoom: 2
});

var rasterLayer = new ol.layer.Tile({
  source: new ol.source.TileJSON({
    url: 'http://api.tiles.mapbox.com/v3/mapbox.geography-class.jsonp'
  })
});

var Near = {};
Near.map = new ol.Map({
  layers: [ osmLayer, rasterLayer, vectorLayer ],
  controls: ol.control.defaults({
    attributionOptions: /** @type {olx.control.AttributionOptions} */ ({
      collapsible: false
    })
  }),
  target: 'map-canvas',
  view: mapView
});

Near.map.on('singleclick', function (evt) {
		console.log(evt.coordinate);
        iconGeometry.setCoordinates([10, 10]);
    });
Near.updateSourceLocation = function() {
	Debug.Log("olaqase");
}

