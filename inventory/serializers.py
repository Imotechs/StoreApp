from rest_framework import serializers
from .models import Supplier, InventoryItem

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['slug','name','contact_info','date_added']

class InventoryItemSerializer(serializers.ModelSerializer):
    suppliers = SupplierSerializer(many=True,read_only =True)
    supplier_ids = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all(), many=True, write_only=True, required=False)

    class Meta:
        model = InventoryItem
        fields = ['slug','name','description','price','date_added','suppliers','supplier_ids']
    def create(self, validated_data):
        supplier_ids = validated_data.pop('supplier_ids', [])
        item = InventoryItem.objects.create(**validated_data)
        item.suppliers.set(supplier_ids)
        return item

    def update(self, instance, validated_data):
        supplier_ids = validated_data.pop('supplier_ids', [])
        instance = super().update(instance, validated_data)
        instance.suppliers.set(supplier_ids)
        return instance