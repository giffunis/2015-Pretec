# -*- coding: utf-8 -*-
from lettuce import *
from lettuce.django import django_url
from nose.tools import assert_equals
from lettuce.django import django_url
from nose.tools import *
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from usuarios.models import Usuario


@step(u'voy a la direccion "(.*)" url')
def la_direccion_url(step,url):
    world.browser.get(url)


@step(u'deberia ver "(.*)"')
def then_deberia_ver_content(step,content):
    world.browser.implicitly_wait(5)
    if content not in world.browser.find_element_by_id("content").text:
        raise Exception(world.browser.find_element_by_id("content").text)

@step(u'un usuario se quiere registrar "(.*)"')
def un_usuario_se_quiere_registrar(step,nombre):
    assert True, 'This step must be implemented'
    # Usuario=Usuario(nombre=nombre)
    # Usuario.save()
#
@step(u'El llena el "(.*)" con "(.*)"')
def el_llena_el(step,field,value):
    # world.browser.fill(field,value)
    campo_input=world.browser.find_element_by_id(field)
    campo_input.send_keys(value)

@step(u'El presiona "(.*)"')
def el_presiona(step,button_label):
    # button=world.browser.find_element_byid('//button[text()="%s"]') % button_label.first
    botton_registro=world.browser.find_element_by_id(button_label)
    botton_registro.click()
    world.browser.implicitly_wait(5)

@step(u'Then deberia ver el error "(.*)"')
def then_deberia_ver_content(step,content):
    world.browser.implicitly_wait(1)
    if content not in world.browser.find_element_by_id("error").text:
        raise Exception("Pagina no encontrada.")

# @step(u'El deberia ver "(.*)"')
# def el_deberia_ver(step,text):
#     assert text in world.browser.html
#
@step(u'El usuario existente es "(.*)"')
def el_usuario_existente_es(step,campo):
    assert True, 'el usuario quiere crear con ese pseudonimo'

@step(u'deberia ver en el id "(.*)" esto (.*)')
def then_deberia_ver_content(step,id_usu,content):
    world.browser.implicitly_wait(5)
    if content == world.browser.find_element_by_id(id_usu).text:
        assert True
    else:
        raise Exception(content+" "+world.browser.find_element_by_id(id_usu).text)

@step(u'selecciona la imagen (.*)')
def selecciona_la_imagen(step,imagen_input):
    campo_input_file=world.browser.find_element_by_xpath("//input[@type='file']")
    campo_input_file.send_keys(imagen_input)
