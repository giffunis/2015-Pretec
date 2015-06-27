Feature: Registro
	Testing de registro
	Para saber si un usuario puede registrarse
	Aquí van los escenarios

	Scenario: Usuario puede ir a la pagina de registro
		Given voy a la direccion "/registro/" url
    Then deberia ver "Registro"

	
Scenario: User enters a username that has been taken
    Given a user exists with username "joeb"
    When I go to the "/register/" URL
    And I fill in "username" with "joeb"
    And I move focus away from the username field
    Then I should see "not available"