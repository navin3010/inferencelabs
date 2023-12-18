from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework import (
    response,
    status,
    serializers as rest_serializers,
    parsers,
)
from ecom import validators, serializers as ecom_serializers, models_api, models
from ecom.forms import ContactForm
from django.db import connection
from rest_framework import permissions, response, status, decorators

class CategoryAPI(APIView):

    def post(self, request):
        user_data = request.user
        title = request.data.get("title", "")
        if not title:
            return response.Response(
                {
                    "status" : False,
                    "msg" : "title is empty"
                },status=status.HTTP_400_BAD_REQUEST
            )
        if not user_data.is_superuser:
            return response.Response(
                {
                    "status" : False,
                    "msg" : "You dont have access to perform this operation (You are not Admin)"
                },status=status.HTTP_400_BAD_REQUEST
            )
        
        validators.IsExists().category_title_is_exists(title=title)
        ecom_serializer =  ecom_serializers.WriteCategorySerializer(data = request.data)
        if not ecom_serializer.is_valid():
            return response.Response(
                {
                    "result": False,
                    "msg": "Validation error",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        ecom_serializer.save(title=title.lower())
        return response.Response(
            {
                "result": True,
                "msg": "success",
                "data": ecom_serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )


@decorators.permission_classes([permissions.AllowAny])
class ProductsAPI(APIView):

    def get(self, request):
        category_id = request.data.get("category_id", "")
        if not category_id:
            return response.Response(
                {
                    "result": False,
                    "msg": "Validation error",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        products_models_data = models_api.ProductsModels().get_product_details_by_category_id(category_id=category_id)
        serialized_data = ecom_serializers.ProductsSerializer(products_models_data, many = True)
        return response.Response(
                {
                    "result": True,
                    "msg": "success",
                    "data": serialized_data.data,
                },
                status=status.HTTP_200_OK,
            )
    
def review(request):
    # if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
        product_id = int(request.POST.get("products"))
        rating = request.POST.get("rating")
        pros = request.POST.get("pros")
        crons = request.POST.get("crons")
        review = request.POST.get("review")
        if not product_id and rating and pros and crons and review:
            return response.Response(
                {
                    "result": False,
                    "msg": "Validation error",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        with connection.cursor() as cursor:
            query = f'''INSERT INTO review(rating, pros, corns, review, products_id)
	                VALUES ({rating},'{pros}','{crons}','{review}',{product_id});'''
            cursor.execute(query)
    return render(request, 'reviews.html', {'form': form})