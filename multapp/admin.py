from django.contrib import admin

from .models import MediaUpload

class MediaUploadAdmin(admin.ModelAdmin):
    search_fields = ('author', 'youtube_video_link')
    list_display = ('author', 'image', 'youtube_video_link')
    

admin.site.register(MediaUpload, MediaUploadAdmin)

