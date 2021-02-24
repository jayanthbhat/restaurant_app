from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.
from django.contrib.auth import login,authenticate
from order_app.models import FoodCategory,FoodItems
from rest_framework import status
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView,ListAPIView,ListCreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,CreateAPIView,RetrieveUpdateAPIView
from .serializers import LoginSerializer,ListFoodCategorySerializer,FoodItemsByCategorySerializer,UserSerializer, RegisterSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

# Register API
class RegisterAPI(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        Token.objects.create(user=user)
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        })



class LoginAPI(GenericAPIView):
    permission_classes = (permissions.AllowAny,)

    serializer_class= LoginSerializer
    queryset=User.objects.all()

    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"message": "Login Successfully"})
        else:
            return Response({"message": "Invalid username or password"})
        


class ListFoodCategoryAPIView(ListAPIView):
    serializer_class = ListFoodCategorySerializer
    def get_queryset(self):
        # current_user = self.request.user
        return FoodCategory.objects.all()  


class ListFoodItemsByCategoryAPIView(ListAPIView):
    serializer_class = FoodItemsByCategorySerializer 

    def get_queryset(self):
           
        category_id = self.request.query_params.get('category_id', None)
        attribute_id = self.request.query_params.get('attribute_id', None)
        price_start= self.request.query_params.get('price_start', None)
        price_end= self.request.query_params.get('price_end', None)
        qs= self.request.query_params.get('qs', None)
        if qs:
            return FoodItems.objects.filter(Q(name__icontains=qs)|Q(category__name__icontains=qs))
        else:

            if price_start and price_end:
                return FoodItems.objects.filter(price__range=[price_start,price_end])
            else:
                if attribute_id:
                    if category_id and attribute_id:
                        return FoodItems.objects.filter(category__id=category_id,attributes__id=attribute_id)
                    else:
                        return FoodItems.objects.filter(attributes__id=attribute_id)
                else:
                    if category_id : 
                        return FoodItems.objects.filter(category__id=category_id)
                    else:
                        return FoodItems.objects.all()
