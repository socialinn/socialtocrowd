

function SelectPlaceMap( args )
{
	// arguments
	args = args || {};
	args.marker_image = args.marker_image || 'NO_MARKER_IMAGE';
	args.default_position = args.default_position || [0, 0];
	args.map_div_id = args.map_div_id || 'default-map-div';

	this.markerImage= args.marker_image;
	this.iconGeometry = new ol.geom.Point(args.default_position);
	this.iconFeature = new ol.Feature({
		geometry: this.iconGeometry
	});
	this.iconStyle = new ol.style.Style({
		image: new ol.style.Icon(/** @type {olx.style.IconOptions} */ ({
			anchor: [0.5, 46],
			anchorXUnits: 'fraction',
			anchorYUnits: 'pixels',
			opacity: 0.75,
			src: this.markerImage
		}))
	});
	this.iconFeature.setStyle(this.iconStyle);
	this.vectorSource = new ol.source.Vector({
		features: [this.iconFeature]
	});
	this.vectorLayer = new ol.layer.Vector({
		source: this.vectorSource
	});
	this.osmLayer = new ol.layer.Tile({
		source: new ol.source.OSM()
	});
	this.mapView = new ol.View({
		center: [0, 0],
		zoom: 8
	});

	this.map = new ol.Map({
		layers: [this.osmLayer, this.vectorLayer],
		target: 'id_pos_map',
		controls: ol.control.defaults({
			attributionOptions: /** @type {olx.control.AttributionOptions} */ ({
				collapsible: false
			})
		}),
		view: this.mapView
	});

	var that = this;
	// that?
	this.setMarkerPlaceLatLon = function( lat, lon ) {
		var normalized_coords = ol.proj.transform([lat, lon], 'EPSG:4326', 'EPSG:3857');
		that.iconGeometry.setCoordinates(normalized_coords);
		that.mapView.setCenter(normalized_coords);
	};

	this.onSelectPlace = function( callback ) {
		that.customSelectPlaceCallback = callback;
	};

	// that?
	this.map.on('singleclick', function(evt) {
		that.iconGeometry.setCoordinates(evt.coordinate);
		if( that.customSelectPlaceCallback ) {
			that.customSelectPlaceCallback( that.map, evt.coordinate );
		}
	});
}

