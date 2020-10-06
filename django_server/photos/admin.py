from django.contrib import admin
from .models import Tag, Photo, PhotoComment, PhotoTag, PhotoGroup, Album, AlbumPhotoRelationship, AlbumTag

# Register your models here.
admin.site.register(Tag)
admin.site.register(Photo)
admin.site.register(PhotoComment)
admin.site.register(PhotoTag)
admin.site.register(PhotoGroup)
admin.site.register(Album)
admin.site.register(AlbumPhotoRelationship)
admin.site.register(AlbumTag)