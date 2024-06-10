from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Supplier,InventoryItem
from .serializers import SupplierSerializer,InventoryItemSerializer
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def endpoint(request):
    data = ['/api/suppliers/', '/api/supplier/<str:slug>/',
            '/api/items/',
            '/api/item/<str:slug>/',
            ]
    return Response(data)


class SupplierView(APIView):
    permission_classes =[]# permision class to restrict access
    authentication_classes =[]#auth class to authenticate request.
    serializer_class = SupplierSerializer
    def get(self,request,slug =None,*args,**kwargs):
        message ='successful'
        if slug is not None:
            try:
                supplier_obj = Supplier.objects.get(slug=slug,date_deleted =None)
                supplier_data= SupplierSerializer(supplier_obj,many = False).data

                items = InventoryItemSerializer(InventoryItem.objects.filter(suppliers__id =supplier_obj.id),many = True).data
                supplier_data['itemsList'] = items
                return Response({'message':message,'data':supplier_data}, status= status.HTTP_200_OK) 
            except Supplier.DoesNotExist:
                message ='item does not exist with that slug'
                return Response({'message':message},status=status.HTTP_404_NOT_FOUND)
        supplierslist = SupplierSerializer(Supplier.objects.filter(date_deleted =None),many = True)
        return Response({'message':message,'data':supplierslist.data}, status= status.HTTP_200_OK) 
    
    
    def post(self,request,*args,**kwargs):
        data = request.data.copy()
        serializer = SupplierSerializer(data = data,many =False)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, slug):
        try:
            item = Supplier.objects.get(slug=slug)
        except Supplier.DoesNotExist:
            return Response({'message': 'Item not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = SupplierSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request, slug):
        if slug :
            try:
                obj = Supplier.objects.get(slug=slug)
                obj.soft_delete()
                
                return Response({'message': 'Deleted!','data':SupplierSerializer(obj).data},status=status.HTTP_202_ACCEPTED)
            except Supplier.DoesNotExist:
                return Response({'message': 'Item not found.'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'message': 'Item not found.'}, status=404) 
Supplier_View = SupplierView.as_view()


class InventoryItemsView(APIView):
    permission_classes =[]# if any
    authentication_classes =[]#if any
    serializer_class = InventoryItemSerializer
    def get(self, request, slug=None, *args, **kwargs):
        items = InventoryItem.objects.filter(date_deleted=None)
        message = 'successful!'
        if slug is not None:
            try:
                item = InventoryItem.objects.get(slug=slug, date_deleted=None)
                items = [item]  # Make a list for consistent handling below
            except InventoryItem.DoesNotExist:
                message = 'item does not exist with that slug'
                return Response({'message': message}, status=status.HTTP_404_NOT_FOUND)
        itemserializer = InventoryItemSerializer(items, many=True)
        item_data = itemserializer.data
        # Add suppliers' data
        # for item in item_data:
        #     suppliers = SupplierSerializer(Supplier.objects.filter(items__id=item['id']), many=True).data
        #     item['supplierList'] = suppliers
        return Response({'message': message, 'data': item_data}, status=status.HTTP_200_OK)
    
    def post(self,request,*args,**kwargs):
        data = request.data.copy()
        serializer = InventoryItemSerializer(data =data,many =False)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, slug):
        try:
            item = InventoryItem.objects.get(slug=slug)
        except InventoryItem.DoesNotExist:
            return Response({'message': 'Item not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = InventoryItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, slug):
        if slug :
            try:
                obj = InventoryItem.objects.get(slug=slug)
                obj.soft_delete()
                return Response({'message': 'Deleted!','data':InventoryItemSerializer(obj).data},status=status.HTTP_202_ACCEPTED)
            except InventoryItem.DoesNotExist:
                return Response({'message': 'Item not found.'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'message': 'Item not found.'}, status=404) 
InventoryItems_View = InventoryItemsView.as_view()