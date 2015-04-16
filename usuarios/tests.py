from django.test import TestCase
from usuarios.models import Usuario

# Create your tests here.

class UsuarioTestCase(TestCase):

    def setUp(self):
        Usuario.objects.create(nombre = "Alejandro", apellidos = "Ravelo", pseudonimo = "J", correo = "alu@ull.edu.es", password = "batman", date = "1976-05-26")
        Usuario.objects.create(nombre = "Joaquin", apellidos = "Escobar", pseudonimo = "Jo", correo = "alu2@ull.edu.es", password = "robin", date = "1976-04-26")

    def test_tiene_nombre(self):
        u1 = Usuario.objects.get(apellidos = 'Ravelo' )
        self.assertEqual(u1.nombre, 'Alejandro')

    def test_tiene_Apellido(self):
        u2 = Usuario.objects.get(nombre = 'Joaquin')
        self.assertEqual(u2.apellidos, 'Escobar')

    def test_Nombre_no_vacio(self):
        u1 = Usuario.objects.get(apellidos = 'Escobar')
        self.assertNotEqual(u1.nombre,"")

    def test_Apellido_no_vacio(self):
        u1 = Usuario.objects.get(nombre = 'Joaquin')
        self.assertNotEqual(u1.apellidos,"")

    def test_Pseudonimo_no_vacio(self):
        u1 = Usuario.objects.get(nombre = 'Joaquin')
        self.assertNotEqual(u1.pseudonimo,"")

    def test_Correo_no_vacio(self):
        u1 = Usuario.objects.get(nombre = 'Joaquin')
        self.assertNotEqual(u1.correo,"")

    def test_Password_no_vacio(self):
        u1 = Usuario.objects.get(nombre = 'Joaquin')
        self.assertNotEqual(u1.password,"")


    def test_Mayor_edad(self):
        u1 = Usuario.objects.get(nombre = 'Joaquin')
        self.assertTrue(u1.restriccion_edad())

    def test_calc_edad(self):
        u1 = Usuario.objects.get(nombre = 'Joaquin')
        self.assertEqual(u1.calc_edad(), 38)



    #def test_disponibilidad_pseudonimo(self)
    #    assertNotEqual()
