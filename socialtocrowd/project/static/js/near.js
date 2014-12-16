

// MARKER CONFIG
var iconGeometry = new ol.geom.Point([637125.42195, 8172199.19090669]);
var iconFeature = new ol.Feature({
	geometry: iconGeometry,
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

var iconStyle2 = new ol.style.Style({
  image: new ol.style.Icon(/** @type {olx.style.IconOptions} */ ({
    anchor: [0.5, 46],
    anchorXUnits: 'fraction',
    anchorYUnits: 'pixels',
    opacity: 0.75,
    src: marker_image2
  }))
});


iconFeature.setStyle(iconStyle);

var yourAddrSource = new ol.source.Vector({
	features: []
});

var yourAddrLayer = new ol.layer.Vector({
	source: yourAddrSource
});

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
  layers: [ osmLayer, vectorLayer ],
  target: document.getElementById('map-canvas'),
  controls: ol.control.defaults({
    attributionOptions: /** @type {olx.control.AttributionOptions} */ ({
      collapsible: false
    })
  }),
  view: mapView
});


Near.updateSourceLocation = function() {
	mapView.setCenter(iconGeometry.getCoordinates());
}

var element = document.getElementById('popup');

var popup = new ol.Overlay({
  element: element,
  positioning: 'bottom-center',
  stopEvent: false
});

Near.map.addOverlay(popup);

Near.map.on('click', function(evt) {
  var feature = Near.map.forEachFeatureAtPixel(evt.pixel,
      function(feature, layer) {
        return feature;
      });
  if (feature) {
    var geometry = feature.getGeometry();
    var coord = geometry.getCoordinates();
    popup.setPosition(coord);
    $(element).popover({
      'placement': 'top',
      'html': true,
      'content': feature.get('name')
    });
    $(element).popover('show');
  } else {
    $(element).popover('destroy');
  }
});

$(Near.map.getViewport()).on('mousemove', function(e) {
  var pixel = Near.map.getEventPixel(e.originalEvent);
  var hit = Near.map.forEachFeatureAtPixel(pixel, function(feature, layer) {
    return true;
  });
  if (hit) {
    Near.map.getTarget().style.cursor = 'pointer';
  } else {
    Near.map.getTarget().style.cursor = '';
  }
});

