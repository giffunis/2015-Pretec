from lettuce import *
from lettuce.django import django_url
from nose.tools import assert_equals
from lettuce.django import django_url
from nose.tools import *
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from microposts.models import Post


@step(u'voy a la direccion "(.*)" url')
def la_direccion_url(step,url):
    world.browser.get(url)


@step(u'Then deberia ver "(.*)"')
def then_deberia_ver_content(step,content):
    world.browser.implicitly_wait(5)
    if content not in world.browser.find_element_by_id("content").text:
        raise Exception("Pagina no encontrada.")

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
