from django.contrib import admin
from django.urls import path,include
from .views import ListFoodCategoryAPIView,ListFoodItemsByCategoryAPIView,RegisterAPI,LoginAPI

urlpatterns = [
    # path('', include('order_app.urls')),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/list-fooditems-categories/',ListFoodItemsByCategoryAPIView.as_view(), name="list_subcategory"),
    path('api/list-categories/',ListFoodCategoryAPIView.as_view(), name="list_all_categories"),
]

