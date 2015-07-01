Feature: Micropost
  Testing de Micropost
  Para ver si es posible hacer post
  Para ver si es posible modificar
  Para ver si es posible eliminar
  Aqui van los escenarios

  Scenario: Un usuario logueado puede ir a micropost
    Given voy a la direccion "http://127.0.0.1:8000/microposts" URL
    Then deberia ver "Crea tu micropost"

  Scenario: Un usuario puede crear un post
    Given voy a la direccion "http://127.0.0.1:8000/microposts" URL
    When El llena el "id_titulo" con "Titulo YUJU"
    And El llena el "id_texto" con "Esto es un microposts"
    And El presiona "Enviar"
    Then deberia ver "POST ENVIADO"
