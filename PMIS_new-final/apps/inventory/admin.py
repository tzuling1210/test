from django.contrib import admin

from .models import Product
from .models import Material
from .models import Material_detail

# Register your models here.
admin.site.register(Product)
admin.site.register(Material)
admin.site.register(Material_detail)
