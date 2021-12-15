from django.test import TestCase

from exams_api.models import Product, Customer, Sale

class CustomerModelClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Setting up non-modified data for all class methods.")
        Customer.objects.create(name='João', document='123123123-21')
    
    def test_name(self):
        customer = Customer.objects.get(id=1)
        field_label = customer._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        customer = Customer.objects.get(id=1)
        max_length = customer._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

    def test_document(self):
        customer = Customer.objects.get(id=1)
        field_label = customer._meta.get_field('document').verbose_name
        self.assertEquals(field_label, 'cpf')

    def setUp(self):
        print("setUp: Running to setup clean data.")
        pass