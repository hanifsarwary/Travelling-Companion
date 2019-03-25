from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Blog)
admin.site.register(BlogPicture)
admin.site.register(BlogLike)
admin.site.register(BlogComment)