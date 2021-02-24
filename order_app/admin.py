from django.contrib import admin
from order_app.models import FoodCategory,FoodItems,FoodAttribute
# Register your models here.

admin.site.register(FoodCategory)
admin.site.register(FoodItems)
admin.site.register(FoodAttribute)