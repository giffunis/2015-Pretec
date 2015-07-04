Feature: seguir y no seguir
  Testing del sistema seguir
  Aqui van los escenarios

  Scenario: Usuario se crea primero
    Given un usuario se quiere registrar "zeta"
    When voy a la direccion "http://127.0.0.1:8000/registro/" URL
    And El llena el "id_nombre" con "joaquin"
    And El llena el "id_apellidos" con "escobar"
    And El llena el "id_pseudonimo" con "zetazeta"
    And El llena el "id_correo" con "zeta@zeta.com"
    And El llena el "id_password1" con "123456"
    And El llena el "id_password2" con "123456"
    And El llena el "id_date" con "02/17/1991"
    And El presiona "Registrarse"
    Then deberia ver "Registro completado"

  Scenario: El usuario zeta se loguea
    Given El usuario existente es "zetazeta"
    And voy a la direccion "http://127.0.0.1:8000/login/" url
    When El llena el "id_pseudonimo" con "zetazeta"
    And El llena el "id_password" con "123456"
    And El presiona "Enviar"
    Then deberia ver "Home"

  Scenario: El usuario zetazeta puede buscar jotajota
    Given voy a la direccion "http://127.0.0.1:8000/home/" URL
    And El presiona "Buscar_Amigos"
    And El llena el "id_busquedaUsu" con "jotajota"
    And El presiona "buscarUsu"
    Then deberia ver "jotajota"

  Scenario: El usuario zetazeta puede ir al perfil de jotajota
    Given El presiona "jotajota"
    Then deberia ver en el id "id_jotajota" esto jotajota

  Scenario: El usuario zeta zeta puede seguir a jotajota
    Given El presiona "btn_seguir"
    Then deberia ver en el id "success" esto Siguiendo!!

  Scenario: El usuario zetazeta deja de seguir a jotajota
    Given El presiona "btn_seguir"
    Then deberia ver en el id "success" esto Ya no sigues a este usuario

  Scenario: El usuario zetazeta vuelve a seguir a jotajota
    Given El presiona "btn_seguir"
    Then deberia ver en el id "success" esto Siguiendo!!

  Scenario: El usuario zetazeta puede ver a quien sigue
    Given voy a la direccion "http://127.0.0.1:8000/mi_perfil/" URL
    And El presiona "siguiendo"
    Then deberia ver en el id "id_jotajota" esto jotajota

  Scenario: El usuario zetazeta puede ver que el jotajota lo tiene como seguidor
    Given El presiona "id_jotajota"
    And El presiona "seguidores"
    Then deberia ver en el id "id_zetazeta" esto zetazeta
