from django.contrib import admin
from .models import Post

admin.site.register(Post)
#为了让模型在admin界面上可用