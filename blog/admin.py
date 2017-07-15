from django.contrib import admin

# Register your models here.
from .models import Post, Tag, Setting, Contact

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Setting)
admin.site.register(Contact)
