Feature: Micropost
  Testing de Micropost
  Para ver si es posible hacer post
  Para ver si es posible modificar
  Para ver si es posible eliminar
  Aqui van los escenarios

  Scenario: Usuario se loguea correctamente
    Given El usuario existente es "jotajota"
    And voy a la direccion "http://127.0.0.1:8000/login/" url
    When El llena el "id_pseudonimo" con "jotajota"
    And El llena el "id_password" con "123456"
    And El presiona "Enviar"
    Then deberia ver "Home"

  Scenario: Un usuario logueado puede ir a micropost
    Given voy a la direccion "http://127.0.0.1:8000/microposts" URL
    Then deberia ver "Crea tu micropost"

  Scenario: Un usuario puede crear un post
    Given voy a la direccion "http://127.0.0.1:8000/microposts" URL
    When El llena el "id_titulo" con "Titulo YUJU"
    And El llena el "id_texto" con "Esto es un microposts"
    And El presiona "Enviar"
    Then deberia ver "Post Enviado"

  Scenario: Un usuario puede editar su post
    Given voy a la direccion "http://127.0.0.1:8000/mi_perfil/" URL
    And El presiona "Editar_post"
    And deberia ver "Editar Post"
    And El llena el "titulo" con "Titulo YUJUUUUU"
    And El llena el "texto" con "Se ha editado el micropost"
    And El presiona "publicar"
    Then deberia ver en el id "success" esto Post modificado!

  Scenario: Un usuario puede borrar un post
    Given voy a la direccion "http://127.0.0.1:8000/mi_perfil/" URL
    And El presiona "Eliminar_post"
    Then deberia ver "Post Eliminado"
