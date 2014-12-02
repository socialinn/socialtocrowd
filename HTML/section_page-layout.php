<!-- page-layout -->
<div class="page-layout container">
	<div class="row">
		<!-- #content -->
		<section id="content" class="col-md-9">
			<!-- page-header -->
			<div class="page-header">
				<h2>Titulo de página <small>Subtext for header</small></h2>
			</div>
			<!-- END page-header -->
			<!-- view-options -->
			<div class="row view-options">
				<div class="col-md-4 col-sm-5">
					<div class="input-group">
						<input type="text" class="form-control">
						<span class="input-group-btn">
							<button class="btn btn-default" type="button"><i class="icon-search i-16"></i></button>
						</span>
					</div>
				</div>
				<div class="col-md-6 col-md-offset-2 col-sm-4 col-sm-offset-3 text-right">
					<div class="btn-group change-view" role="group">
						<button type="button" class="btn btn-default active" data-view="list"><i class="icon-list i-16"></i></button>
						<button type="button" class="btn btn-default" data-view="grid"><i class="icon-grid i-16"></i></button>
						<button type="button" class="btn btn-default" data-view="map"><i class="icon-location i-16"></i></button>
					</div>
				</div>
			</div>
			<!-- END view-options -->

			<?php include ('component_projects-list.php');?>
			<?php include ('component_projects-grid.php');?>
			<?php include ('component_objects.php');?>
			<?php include ('component_donations.php');?>
			
			<nav class="text-center">
				<ul class="pagination">
					<li><a href="#"><span aria-hidden="true">&laquo;</span><span class="sr-only">Previous</span></a></li>
					<li class="active"><a href="#">1</a></li>
					<li><a href="#">2</a></li>
					<li><a href="#">3</a></li>
					<li><a href="#">4</a></li>
					<li><a href="#">5</a></li>
					<li><a href="#"><span aria-hidden="true">&raquo;</span><span class="sr-only">Next</span></a></li>
				</ul>
			</nav>
			
		</section>
		<!-- END #content -->
		<!-- #sidebar-right -->
		<div id="sidebar-right" class="col-md-3">
			<?php include ('widget_featured.php');?>
			<?php include ('widget_category.php');?>
			<?php include ('widget_last_donations.php');?>
			<?php include ('widget_needs.php');?>
			<?php include ('widget_collaborators.php');?>
		</div>
		<!-- END #sidebar-right -->
	</div>
</div>
<!-- END page-layout -->