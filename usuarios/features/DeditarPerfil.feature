Feature: Editar Perfil
  Testings de editar perfil
  Aqui van los escenarios

  Scenario: El usuario puede llegar a editarPerfil
    Given voy a la direccion "http://127.0.0.1:8000/editProfile/" URL
    Then deberia ver "Edita tu Perfil"

  Scenario: El usuario deberia ver las opciones
    Given deberia ver en el id "editar_nombre" esto Nombre
    And deberia ver en el id "editar_correo" esto Correo
    And deberia ver en el id "editar_contrasena" esto Password
    Then deberia ver en el id "editar_imagen" esto Imagen de Perfil

  Scenario: El usuario cambia el nombre y apellidos
    Given El presiona "editar_nombre"
    And deberia ver "Cambio del nombre y apellidos"
    And El llena el "id_nombre" con "Pepito"
    And El llena el "id_apellidos" con "Palotes"
    And El presiona "actualizar"
    Then deberia ver en el id "success" esto El nombre y los apellidos se han actualizado correctamente


  Scenario: El usuario cambia de correo
    Given voy a la direccion "http://127.0.0.1:8000/editProfile/" URL
    And El presiona "editar_correo"
    And deberia ver "Cambio de correo"
    And El llena el "id_old_email" con "zeta@zeta.com"
    And El llena el "id_new_email" con "zetas@zetas.com"
    And El presiona "actualizar"
    Then deberia ver en el id "success" esto Su correo se ha actualizado

  Scenario: El usuario cambia la contraseña
    Given voy a la direccion "http://127.0.0.1:8000/editProfile/" URL
    And El presiona "editar_contrasena"
    And deberia ver "Cambio de contraseña"
    And El llena el "id_old_password" con "123456"
    And El llena el "id_new_password1" con "qwerty"
    And El llena el "id_new_password2" con "qwerty"
    And El presiona "actualizar"
    Then deberia ver en el id "success" esto Su contrasena se ha actualizado correctamente

  Scenario: El usuario cambia su imagen#solo funciona en pc joaquin
    Given voy a la direccion "http://127.0.0.1:8000/editProfile/" URL
    And El presiona "editar_imagen"
    And deberia ver "Acrualiza tu foto"
    And selecciona la imagen "C:\Users\quino\Pictures\foto_perfil"
    And El presiona "actualizar"
    Then deberia ver "Acrualiza tu foto"
