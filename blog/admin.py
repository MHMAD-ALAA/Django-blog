from multiprocessing.spawn import import_main_path
from django.contrib import admin
from .models import Post

admin.site.register(Post)
