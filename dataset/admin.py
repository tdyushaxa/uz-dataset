from django.contrib import admin
from .models import DataSet,CodeComments, Code,Category

# Register your models here.
admin.site.register(DataSet)
admin.site.register(Code)
admin.site.register(CodeComments)
admin.site.register(Category)