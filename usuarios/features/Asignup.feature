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
		Then deberia ver "Registro completado"

	Scenario: Usuario ingresa un pseudonimo ya existente
		Given El usuario existente es "jotajota"
		When voy a la direccion "http://127.0.0.1:8000/registro/" URL
		When El llena el "id_nombre" con "jose"
		And El llena el "id_apellidos" con "gomez"
		And El llena el "id_pseudonimo" con "jotajota"
		And El llena el "id_correo" con "jota2@jota2.com"
		And El llena el "id_password1" con "654321"
		And El llena el "id_password2" con "654321"
		And El llena el "id_date" con "05/13/1954"
		And El presiona "Registrarse"
		Then deberia ver el error "El pseudonimo no se encuentra disponible"


	Scenario: Usuario ingresa un correo ya existente
		Given El usuario existente es "jota@jota.com"
		When voy a la direccion "http://127.0.0.1:8000/registro/" URL
		When El llena el "id_nombre" con "joaquin"
		And El llena el "id_apellidos" con "escobar"
		And El llena el "id_pseudonimo" con "jota2jota2"
		And El llena el "id_correo" con "jota@jota.com"
		And El llena el "id_password1" con "654321"
		And El llena el "id_password2" con "654321"
		And El llena el "id_date" con "02/17/1991"
		And El presiona "Registrarse"
		Then deberia ver el error "El correo no se encuentra disponible"
