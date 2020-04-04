from django.contrib import admin
from .models import Article

# Register your models here.
# 这样就可以在admin目录下有记录
admin.site.register(Article)
