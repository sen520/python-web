from django.db import models

# Create your models here.
class Category(models.Model):
    cname = models.CharField(max_length=20, unique=True, verbose_name='类别')

    class Meta:
        db_table = 't_category'
        verbose_name_plural = '类别'

    def __str__(self):
        return u'Category:%s' % self.cname


class Tags(models.Model):
    tname = models.CharField(max_length=20, unique=True, verbose_name='标签')

    class Meta:
        db_table = 't_tags'
        verbose_name_plural = '标签'

    def __str__(self):
        return u'Tags:%s' % self.tname


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='帖子')
    desc = models.TextField()
    content = models.TextField()
    created = models.DateField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    # auto_now  当前时间
    # auto_now_add  创建时间
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING,null=False)
    tags = models.ManyToManyField(Tags)

    class Meta:
        db_table = 't_post'
        verbose_name_plural = '帖子'

    def __str__(self):
        return u'Post:%s'%self.title
