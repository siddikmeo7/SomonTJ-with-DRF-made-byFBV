from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    # Products
    path('products',product_list,name='Product-List'),
    path('postproducts',product_list,name='Post-Product'),
    path('detailproduct/<int:pk>',product_detail,name='Detail-Product'),
    path('editproduct/<int:pk>',product_detail,name='Edit-Product'),
    path('deleteproduct/<int:pk>',product_detail,name='Delete-Product'),
    # Categories
    path('categories',Category_list,name='Category-List'),
    path('postcategory',Category_list,name='Post-Category'),
    path('detailcategory/<int:pk>',category_detail,name='Detail-Category'),
    path('editcategory/<int:pk>',category_detail,name='Edit-Category'),
    path('deletecategory/<int:pk>',category_detail,name='Delete-Category'),
    # Request
    path('requests',request_list,name='Request-List'),
    path('postrequest',request_list,name='Post-Request'),
    path('detailrequest/<int:pk>',request_detail,name='Detail-Request'),
    path('editrequest/<int:pk>',request_detail,name='Edit-Request'),
    path('deleterequest/<int:pk>',request_detail,name='Delete-Request'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
