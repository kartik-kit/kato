from django.contrib import admin
from .models import Blog,Author,Categories,Tags
admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Categories)
admin.site.register(Tags)

# Register your models here.
