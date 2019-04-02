import markdown
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# 种类
from django.urls import reverse
from django.utils.html import strip_tags

from comments.models import Comment


class Category(models.Model):
    """
        Django 要求模型必须继承 models.Model 类。
        Category 只需要一个简单的分类名 name 就可以了。
        CharField 指定了分类名 name 的数据类型，CharField 是字符型，
        CharField 的 max_length 参数指定其最大长度，超过这个长度的分类名就不能被存入数据库。
        """
    name = models.CharField(max_length=100, unique=True, verbose_name='类别')

    class Meta:
        db_table = 't_category'
        verbose_name_plural = '类别'

    def __str__(self):
        return self.name


# 标签
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='标签')

    class Meta:
        db_table = 't_tags'
        verbose_name_plural = '标签'

    def __str__(self):
        return self.name


# 帖子
class Post(models.Model):
    # 标题
    title = models.CharField(max_length=100, unique=True, verbose_name='帖子')
    # 内容
    # TextField用于存储大段文本
    content = models.TextField()
    # 创建时间
    created_time = models.DateTimeField()
    # 最后一次修改时间
    modified_time = models.DateTimeField()
    # 摘要，可以没有文章摘要，但默认情况下 CharField 要求我们必须存入数据，否则就会报错。
    # 指定 CharField 的 blank=True 参数值后就可以允许空值了。
    excerpt = models.CharField(max_length=200, blank=True)
    # 种类
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    # 标签
    # 规定一篇文章只能对应一个分类，但是一个分类下可以有多篇文章，使用的是 ForeignKey，即一对多的关联关系。
    # 而对于标签来说，一篇文章可以有多个标签，同一个标签下也可能有多篇文章，所以我们使用 ManyToManyField，表明这是多对多的关联关系。
    # 同时我们规定文章可以没有标签，因此为标签 tags 指定了 blank=True。
    tags = models.ManyToManyField(Tag, blank=True)
    # 作者
    # django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、登录等流程，User 是 Django已经写好的用户模型。
    # 这里我们通过 ForeignKey 把文章和 User 关联了起来。
    # 规定一篇文章只能有一个作者，而一个作者可能会写多篇文章，因此这是一对多的关联关系，和 Category 类似。
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    # 阅读量
    views = models.PositiveIntegerField(default=0)

    def increase_view(self):
        self.views += 1
        self.save(update_fields=['views'])

    class Meta:
        db_table = 't_post'
        verbose_name_plural = '帖子'
        ordering = ['-created_time']

    def save(self, *args, **kwargs):
        # 如果没有填写摘要
        if not self.excerpt:
            # 首先实例化一个 Markdown 类，用于渲染 content 的文本
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # 先将 Markdown 文本渲染成 HTML 文本
            # strip_tags 去掉 HTML 文本的全部 HTML 标签
            # 从文本摘取前 54 个字符赋给 excerpt
            self.excerpt = strip_tags(md.convert(self.content))[:54]
        # 调用父类的 save 方法将数据保存到数据库中
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    # 自定义 get_absolute_url 方法
    # 记得从 django.urls 中导入 reverse 函数
    def get_absolute_url(self):
        return reverse('blog_view:detail', kwargs={'pk': self.pk})
