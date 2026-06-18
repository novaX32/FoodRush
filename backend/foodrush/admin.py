from django.contrib import admin
from .models import User,Food,Category
# Register your models here.

admin.site.register(User)
admin.site.register(Food)
admin.site.register(Category)
