Feature: Registro
	Testing de registro
	Para saber si un usuario puede registrarse
	Aquí van los escenarios

	Scenario: Usuario puede ir a la pagina de registro
		Given voy a la direccion "http://127.0.0.1:8000/registro/" url
    Then deberia ver "¡Únete a pretec!"

	Scenario: Usuario puede registrarse
		Given un usuario se quiere registrar "jota"
		When El llena el "id_nombre" con "joaquin"
		And El llena el "id_apellidos" con "escobar"
		And El llena el "id_pseudonimo" con "jotajota"
		And El llena el "id_correo" con "jota@jota.com"
		And El llena el "id_password1" con "123456"
		And El llena el "id_password2" con "123456"
		And El llena el "id_date" con "02/17/1991"
		And El presiona "Registrarse"
		Then deberia ver "REGISTRO COMPLETADO"

	Scenario: Usuario no llena los campos de forma correcta
    When El va a la direccion "/registro/" URL
    And El presiona "Registrarse"
    Then El deberia ver "Por favor llene los campos obligatorios"

	Scenario: Usuario ingresa un usuario ya existente
		Given El usuario existente es "jojojo"
		When El va a la direccion "/register/" URL
		And El llena el "pseudonimo" con "jojojo"
		Then El deberia ver "Pseudonimo ya existe"


	Scenario: Usuario ingresa un correo ya existente
		Given El usuario existente es "jota@jota.com"
		When El va a la direccion "/registro/" URL
		And El llena el "correo" con "jota@jota.com"
		Then El deberia ver "Correo ya existe"
