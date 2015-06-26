from lettuce import step,world

@step(u'la direccion "([^"]*)"')
def estoy_en_registro(step,url):
    world.browser.get(url)


@step(u'deberia ver los formularios de inscripcion "([^"]*)"')
def deberia_ver_el_render_de_registro(step,content):
    if content not in world.browser.find_element_byid("").text:
        raise Exception("Página no encontrada.")
