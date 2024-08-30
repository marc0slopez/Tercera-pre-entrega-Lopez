from django.test import TestCase
from .models import Categoria, Producto, Cliente

class CategoriaModelTest(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nombre="Electrónica", descripcion="Categoría para productos electrónicos")

    def test_categoria_str(self):
        self.assertEqual(str(self.categoria), "Electrónica")

class ProductoModelTest(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nombre="Electrónica", descripcion="Categoría para productos electrónicos")
        self.producto = Producto.objects.create(nombre="Televisor", descripcion="Televisor LED", precio=500.00, categoria=self.categoria)

    def test_producto_str(self):
        self.assertEqual(str(self.producto), "Televisor")

class ClienteModelTest(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(nombre="Juan Pérez", email="juan.perez@example.com", direccion="Calle Falsa 123")

    def test_cliente_str(self):
        self.assertEqual(str(self.cliente), "Juan Pérez")
