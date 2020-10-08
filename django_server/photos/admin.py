from django.contrib import admin
from .models import Tag, Photo, PhotoComment, PhotoTag, PhotoGroup, Album, AlbumPhotoRelationship, AlbumTag

# Register your models here.
admin.site.register(Tag)
# admin.site.register(Photo)
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('baby', 'image_url', 'last_modified')
    list_filter = ['baby'] 
    fields = ('image_url', 'last_modified')


admin.site.register(PhotoComment)
admin.site.register(PhotoTag)
admin.site.register(PhotoGroup)
admin.site.register(Album)
admin.site.register(AlbumPhotoRelationship)
admin.site.register(AlbumTag)