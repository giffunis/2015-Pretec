Feature: Registro
	Testing de registro
	Para saber si un usuario puede registrarse
	Aquí van los escenarios

	Scenario: Puedo ir a la pagina de registro
		Given la direccion "http://127.0.0.1:8000/registro/"
    Then deberia ver los formularios de inscripcion
