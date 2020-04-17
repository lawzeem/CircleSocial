from django.db import models
from cse312.users.models import User
# from cse312.users.models import feed
from PIL import Image


class Post(models.Model):
    title = models.CharField('title', max_length=100)
    image = models.ImageField(default='post/default.jpg', upload_to='post')
    description = models.CharField('description', max_length=1000)
    upvotes= models.IntegerField(default=0)
    comment = models.CharField('comment', max_length = 2000)
    user_id = models.ForeignKey(User, unique=False, on_delete = models.CASCADE)

    def save_img(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (600, 600)
            img.thumbnail(output_size)
            img.save_img(self.image.path)

    def publish_post(self):
        self.save()

    def __str__(self):
        return self.title


class Comments(models.Model):
    post_id = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    user_id = models.ForeignKey(User, unique=False, on_delete = models.CASCADE)
    comment = models.TextField()
    upvotes = models.IntegerField(default=0)

    def __str__(self):
        return self.comment


# Create your models here.
