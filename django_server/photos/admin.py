from django.contrib import admin
from .models import Tag, Photo, PhotoComment, Album, PhotoTag

# Register your models here.
admin.site.register(Tag)
admin.site.register(Photo)
admin.site.register(PhotoTag)
admin.site.register(PhotoComment)
admin.site.register(Album)