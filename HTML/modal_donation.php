<!-- modal_donation -->
<div class="modal fade" id="modal_donation" tabindex="-1" role="dialog" aria-labelledby="modal_donationLabel" aria-hidden="true">
	<div class="modal-dialog">
		<!-- modal-content form -->
		<div class="modal-content form active">
			<div class="modal-header">
				<button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
				<h3 class="modal-title" id="myModalLabel">Donar un objeto</h3>
			</div>
			<div class="modal-body">
				<!-- form -->
				<form>
					<!-- form-section -->
					<div class="form-section">
						<h4 class="form-section-header"><span class="badge">1</span> ¿Tienes una foto del objeto? Agregala...</h4>
						<div class="well text-center">
							<i class="icon-camera i-64"></i>
							<p><a href="#" class="black">Agregar una imagen</a></p>
						</div>
					</div>
					<!-- END form-section -->
					<!-- form-section -->
					<div class="form-section">
						<h4 class="form-section-header"><span class="badge">2</span> Agrega un nombre y una descripción</h4>
						<div class="form-group">
							<label class="sr-only" for="objectName">Nombre de objeto</label>
							<input type="text" class="form-control" id="objectName" placeholder="Nombre de objeto">
						</div>
						<div class="form-group">
							<label class="sr-only" for="objectDrescription">Descripción del objeto</label>
							<textarea class="form-control" id="objectDrescription" placeholder="Descripción del objeto"></textarea>
						</div>
						<div class="checkbox">
							<label><input id="objectPrivate" type="checkbox"> Hacer privada mi donación.</label>
						</div>
					</div>
					<!-- END form-section -->
					<!-- form-section -->
					<div class="form-section">
						<h4 class="form-section-header"><span class="badge">3</span> Selecciona el método de envío</h4>
						<select class="form-control">
							<option>Método de envío 1</option>
							<option>Método de envío 2</option>
							<option>Método de envío 3</option>
							<option>Método de envío 4</option>
							<option>Método de envío 5</option>
						</select>
					</div>
					<!-- END form-section -->
				</form>
				<!-- END form -->
			</div>
			<div class="modal-footer">
				<button type="button" class="btn btn-link" data-dismiss="modal">Cancelar</button>
				<button type="button" class="btn btn-primary" onclick="formModalSuccess();">Aceptar</button>
			</div>
		</div>
		<!-- END modal-content form -->
		<!-- modal-content success -->
		<div class="modal-content success">
			<div class="modal-header">
				<button type="button" onclick="formModalReset();" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
			</div>
			<div class="modal-body text-center">
				<i class="icon-checkmark i-128"></i>
				<h3>¡Hecho!</h3>
				<h4>Muchas gracias por tu colaboración</h4>
			</div>
		</div>
		<!-- END modal-content success-->
	</div>
</div>
<!-- END modal_donation -->