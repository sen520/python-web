from django.db import models


# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey('blog_view.Post', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.text[:20]
