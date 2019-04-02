# blog

具体教程参考有道云：http://note.youdao.com/noteshare?id=3047ba0d48a21e04700bc70a59913df1

开发环境与使用模块：

      python3.6, pycharm, django, 
      django-haystack, whoosh, jieba（以上三个主要用于实现全文搜索） 
      数据库采用sqlite
      

使用全文搜索，需要在settings.py文件中INSTALLED_APPS中添加'haystack'

        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'post',
            'haystack'
        ]

在settings末尾添加：

      # 指定生成的索引路径
      HAYSTACK_CONNECTIONS = {
          'default': {
              'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
              'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
          },
      }

      # 实时生成索引文件
      HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
      
创建搜索引擎模板

      (project/templates/search/indexes/yourapp/post_text.txt)
            post_text.txt------搜索引擎要执行的对象(模板)_text.txt
            在项目根目录/templates/目录下创建search/indexes/blog/post_text.txt文件
      编辑post_text.txt文件
            {{object.title}}
            {{object.content}}
      通过命令生成索引文件
            python manage.py rebuild_index

未实现功能

      添加帖子功能，目前只能从后台以管理员身份添加，在命令行输入
      “python manage.py createsuperuser”
      创建管理员
      数据库中已有管理员name\password：admins\qwer1234
