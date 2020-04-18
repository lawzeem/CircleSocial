from django.db import models
from cse312.users.models import User
# from cse312.users.models import feed
from PIL import Image


class Post(models.Model):
    title = models.CharField('title', max_length=100)
    image = models.ImageField(default='post/default.jpg', upload_to='post')
    description = models.CharField('description', max_length=1000)
    upvotes= models.ManyToManyField(User, related_name='upvotes', blank=True)
    user = models.ForeignKey(User, unique=False, on_delete = models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 720 or img.width > 1280:
            output_size = (720, 1280)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, unique=False, on_delete = models.CASCADE)
    comment = models.TextField()
    upvotes = models.IntegerField(default=0)

    def __str__(self):
        return self.comment

