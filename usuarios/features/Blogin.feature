Feature: Login
  Testings del login
  Para saber si es posible loguearse
  Aqui van los escenarios




  Scenario: Usuario se loguea correctamente
    Given El usuario existente es "jotajota"
    And voy a la direccion "http://127.0.0.1:8000/login/" url
    When El llena el "id_pseudonimo" con "jotajota"
    And El llena el "id_password" con "123456"
    And El presiona "Enviar"
    Then deberia ver "Home"

    Scenario: Usuario se puede desloguear
  	Given voy a la direccion "http://127.0.0.1:8000/home/" URL
    And El presiona "btn_cerrarsesion"
  	Then deberia ver "Bienvenido a Pretec"

  Scenario: Usuario intenta loguearse incorrectamente
    Given El usuario existente es "jotajota"
    And voy a la direccion "http://127.0.0.1:8000/login/" url
    When El llena el "id_pseudonimo" con "jotajota"
    And El llena el "id_password" con "654321"
    And El presiona "Enviar"
    Then deberia ver el error "El nombre de usuario o la contrasena no coinciden"

  Scenario: Usuario intenta loguearse con un usuario que no existe
    Given El usuario existente es "jojojo"
    And voy a la direccion "http://127.0.0.1:8000/login/" url
    When El llena el "id_pseudonimo" con "jojojo"
    And El llena el "id_password" con "654321123456"
    And El presiona "Enviar"
    Then deberia ver el error "El usuario no existe"
