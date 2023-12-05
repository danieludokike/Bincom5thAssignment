from django.db import models

from embed_video.fields import EmbedVideoField


#QustionsVideo
class MediaUpload(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50, default="Udokike Daniel")
    image = models.ImageField(upload_to="Uploads/")
    youtube_video_link = EmbedVideoField(max_length=100, unique=True, help_text="Enter the video url here")  # same like models.URLField()
    description = models.TextField()
    
    def __str__(self):
        return f"{self.youtube_video_link}"
