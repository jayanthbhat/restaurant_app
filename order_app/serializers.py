from rest_framework import serializers

from order_app.models import FoodCategory,FoodItems,FoodAttribute
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('username','password') 

class ListFoodCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodCategory
        fields = ['id',
            'name']

class ListFoodAttributeSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodAttribute
        fields = ['name']


class FoodItemsByCategorySerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    attributes = serializers.SerializerMethodField()
    class Meta:
        model = FoodItems
        fields=[
            'id',
            'category',
            'attributes',
            'name',
            'price',
        ]
    def get_category(self,obj):
        qs = obj.category
        return ListFoodCategorySerializer(qs, many=False, read_only=True).data	
    
    def get_attributes(self,obj):
        qs = obj.attributes
        return ListFoodAttributeSerializer(qs, many=False, read_only=True).data