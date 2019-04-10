from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings 

# Create your models here.

def post_image_path(instance, filename):
    return 'posts/images/{}'.format(filename)
    
# def post_image_path(instance):
#     return f'posts/{instance.user.username}/{instance.content}.jpeg'

# def post_image_path(instance, filename):
#     return f'posts/{instance.user.username}/{filename}'

# def post_image_path(instance, filename): #instance와 filename은 꼭 있어야 함
#     return f'posts/images/{filename}'

# def post_image_path(instance, filename):
    # return 'posts/{}/{}'.format(instance.content, filename)

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    # image = models.ImageField(blank=True)
    image = ProcessedImageField(
        upload_to = post_image_path, #저장 위치
        processors = [ResizeToFill(600,600)], #처리할 작업 목록
        format = 'JPEG', #저장 포맷
        options = {'quality':90}, #옵션
        )