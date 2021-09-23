from django.contrib import admin
from .models import Movielog, Comment, HashTag

# Register your models here.

admin.site.register(Movielog)
admin.site.register(Comment)
admin.site.register(HashTag)