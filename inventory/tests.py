from django.test import TestCase
from decimal import Decimal

# Create your tests here.
from .models import Supplier, InventoryItem

class SupplierTestCase(TestCase):
    def setUp(self):
        Supplier.objects.create(name="Prioritysoft", contact_info="23 New GRA Main St")
        Supplier.objects.create(name="Supplier2", contact_info="456 Main St")

    def test_supplier_creation(self):
        supplier_a = Supplier.objects.get(name="Prioritysoft")
        supplier_b = Supplier.objects.get(name="Supplier2")
        self.assertEqual(supplier_a.contact_info, "23 New GRA Main St")
        self.assertEqual(supplier_b.contact_info, "456 Main St")

class InventoryItemTestCase(TestCase):
    def setUp(self):
        supplier_a = Supplier.objects.create(name="Prioritysoft", contact_info="23 New GRA Main St")
        item = InventoryItem.objects.create(name="Item1", description="A new item", price=9.99)
        item.suppliers.add(supplier_a)

    def test_inventory_item_creation(self):
        item = InventoryItem.objects.get(name="Item1")
        self.assertEqual(item.description, "A new item")
        self.assertEqual(item.price, Decimal('9.99'))
        self.assertEqual(item.suppliers.count(), 1)
        #self.assertContains('Prioritysoft' in item.suppliers)
