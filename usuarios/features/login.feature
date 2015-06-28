Feature:Login
  Testings del login
  Para saber si es posible loguearse
  Aqui van los escenarios

  Scenario: Usuario se loguea correctamente
    Given El usuario existe es "jojojo"
    And El va a la direccion "/registro/" URL
    When El llena el "pseudonimo" con "jojojo"
    And El llena el "password1" con "123456"
    And El presiona "Enviar"
    Then El deberia ver "ESTA ES TU PAGINA DE INICIO"

  Scenario:Usuario intenta loguearse incorrectamente
    Given El usuario existe es "jojojo"
    And El va a la direccion "/registro/" URL
    When El llena el "pseudonimo" con "jojojo"
    And El llena el "password1" con "123456"
    And El presiona "Enviar"
    Then El deberia ver "El nombre de usuario o la contrasena no coinciden "
