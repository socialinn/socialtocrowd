jQuery(document).ready(function ($) { 

  $("[rel^='lightbox']").prettyPhoto({
    social_tools:''
  });

  // height for main map on homepage
  $(window).resize(function(){
    var window_w = $(window).width();
    if(window_w >= 980){
      $('#last_projects #map_canvas').height($('#last_projects').width()/2);
    } else {
      $('#last_projects #map_canvas').height($(window).height()/1.5);
    }
  }).resize();

  // viewoptions
  $('#last_projects .change-view .btn').click(function(){
    $('#last_projects .change-view .btn').removeClass('active');
    $(this).addClass('active');
    $('#last_projects .projects').removeClass('active');
    $('#last_projects .projects.'+ $(this).attr('data-view') ).addClass('active');
    initMap();
  })
    
});

// function for Map on Homepage
function initMap(){
  var image = 'img/marker.png';

  $('#map_canvas').gmap().bind('init', function(ev, map) {
    //Tooltip content
    var contentTooltip =  '<h3>Nombre de proyecto destacado</h3>'+
                          '<div class="progress">'+
                            '<div class="progress-bar progress-bar-primary" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="width: 60%;">60%</div>'+
                          '</div>';
    // Markers
    $('#map_canvas').gmap('addMarker', {'position': '37.8904684, -4.778048', 'bounds': true, 'icon': image }).click(function() {
      $('#map_canvas').gmap('openInfoWindow', { 'content': contentTooltip }, this);
    });
    $('#map_canvas').gmap('addMarker', {'position': '38.8744759, -6.9723008', 'bounds': true, 'icon': image }).click(function() {
      $('#map_canvas').gmap('openInfoWindow', { 'content': contentTooltip }, this);
    });
    $('#map_canvas').gmap('addMarker', {'position': '36.5975718, -6.2363963', 'bounds': true, 'icon': image }).click(function() {
      $('#map_canvas').gmap('openInfoWindow', { 'content': contentTooltip }, this);
    });
  });
}

// function for Success on Donation Form
function formModalSuccess(){
  $(".modal-content.form").removeClass('active');
  $(".modal-content.success").addClass('active');
}
// function for Reset Donation Form
function formModalReset(){
  setTimeout(function(){
    $(".modal-content.form").addClass('active');
    $(".modal-content.success").removeClass('active');
  }, 1000);
}