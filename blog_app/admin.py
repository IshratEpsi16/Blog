from django.contrib import admin
from .models import Blog,Comment,Likes
# Register your models here.
#user: Blog, pass: blog
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Likes)