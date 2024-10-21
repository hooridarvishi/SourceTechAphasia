from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(Post)
admin.site.register(Note)

admin.site.register(Photo)
admin.site.register(Image)
admin.site.register(Image1)
admin.site.register(Text)