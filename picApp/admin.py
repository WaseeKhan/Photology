from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Category)
admin.site.register(Photo)
admin.site.register(Hero)
# Blogs Model
admin.site.register(BlogCat)
admin.site.register(BlogTag)
admin.site.register(Blog)

