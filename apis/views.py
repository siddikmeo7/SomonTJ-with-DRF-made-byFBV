from rest_framework.decorators import api_view # For working with functions 
from rest_framework.response import Response  # For Responsing 
from rest_framework import status # For returnig different types of mistakes 
from .serializers import *
from .models import *


# Products
@api_view(['Get','POST'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','PUT','DELETE'])
def product_detail(request,pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializers = ProductSerializer(product)
        return Response(serializers.data)
    
    elif request.method == 'PUT':
        serializer = ProductSerializer(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


# Category
@api_view(['Get','POST'])
def Category_list(request):
    if request.method == 'GET':
        products = Category.objects.all()
        serializer = CategorySerializer(products,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','PUT','DELETE'])
def category_detail(request,pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializers = CategorySerializer(category)
        return Response(serializers.data)
    
    elif request.method == 'PUT':
        serializer = CategorySerializer(category,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# Requests              
@api_view(['GET','POST'])
def request_list(request):
    if request.method == 'GET':
        requests = Request.objects.all()
        serializer = RequestSerializer(requests,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status==status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def request_detail(request,pk):
    try:
        request = Request.objects.get(pk=pk)
    except Request.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializers = RequestSerializer(request)
        return Response(serializers.data)
    
    elif request.method == 'PUT':
        serializer = RequestSerializer(request,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        request.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  
