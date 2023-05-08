from django.db import models
from django.conf import settings
import os
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class Info(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    content = models.TextField()
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Image(models.Model):
    info = models.ForeignKey(Info, on_delete=models.CASCADE)
    def info_image_path(instance, filename):
        return f'infobases/{instance.info.pk}/{filename}'

    image = ProcessedImageField(upload_to=info_image_path, blank=True, null=True, processors=[ResizeToFill(200, 200)], options={'quality':90})
    # image = ProcessedImageField(upload_to='', blank=True, null=True, processors=[ResizeToFill(200, 200)], options={'quality':90})

    def delete(self, *args, **kargs):
        if self.image:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image.name))
        super(Image, self).delete(*args, **kargs)
    
    def save(self, *args, **kargs):
        if self.id:
          old_info = Image.objects.get(id=self.id)
          if self.image != old_info.image:
              if old_info.image:
                  os.remove(os.path.join(settings.MEDIA_ROOT, old_info.image.name))
        super(Image, self).save(*args, **kargs)

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    info = models.ForeignKey(Info, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

