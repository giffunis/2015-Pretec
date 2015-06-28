Feature: Registro
	Testing de registro
	Para saber si un usuario puede registrarse
	Aquí van los escenarios

	Scenario: Usuario puede ir a la pagina de registro
		Given voy a la direccion "/registro/" url
    Then deberia ver "Registro"

	Scenario: Usuario puede registrarse
		Given un usuario no existe aun
		When El llena el "nombre" con "joaquin"
		And El llena el "apelliodo" con "escobar"
		And El llena el "pseudonimo" con "jota"
		And El llena el "correo" con "jota@jota.com"
		And El llena el "password1" con "123456"
		And El llena el "password2" con "123456"
		And El llena el "date" con "02/17/1991"
		Then El deberia ver "registrado"

		


Scenario: User enters a username that has been taken
    Given a user exists with username "joeb"
    When I go to the "/register/" URL
    And I fill in "username" with "joeb"
    And I move focus away from the username field
    Then I should see "not available"
