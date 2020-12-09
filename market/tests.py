from django.test import TestCase
from .models import Shop, Mall, Product, User


class TestImage(TestCase):
    def setUp(self):
        self.Mall = Mall(name='Southfield')
        self.Mall.save_mall()

        self.Shop = Shop(name='kfc')
        self.Shop.save_Shop()

        self.Product = Product(name='wingmancombo')
        self.Product.save_product()

        self.User = Product(name='Game')
        self.User.save_category()

        

