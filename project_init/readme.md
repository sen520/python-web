`pip install -r requirement.txt`

- 注册app

  app.__init__
    ```python
    from apps.xxx import *
    ```

- 注册路由

  xxx.__init
    ```python
    from apps import app
    from apps.user.resource import UserRegisterView
    app.add_url_rule('/user/register', view_func=UserRegisterView.as_view('register'))
    ```
- 实现功能
  - mysql主从读写分离
  - jwt
  - aes
  - 模型控制器
  - swagger
  - 中间件