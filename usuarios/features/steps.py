# -*- coding: utf-8 -*-
from lettuce import step,world
from lettuce.django import django_url

@step(u'la direccion "([^"]*)"')
def la_direccion_url(step,url):
    world.browser.get(url)


@step(u'Then deberia ver "([^"]*)"')
def then_deberia_ver_content(step,content):
    if content not in world.browser.find_element_byid("titulo").text:
        raise Exception("Pagina no encontrada.")
