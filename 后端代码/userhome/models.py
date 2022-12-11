from django.db import models


class User(models.Model):
    user_image = models.ImageField("用户头像", max_length=255, default='', upload_to='static/avatar')
    username = models.CharField('账号', max_length=255, unique=True)
    password = models.CharField('密码', max_length=255)
    nickname = models.CharField('昵称', max_length=255, default='HelloWorld')
    email = models.CharField('邮箱', max_length=255, default='')
    introduction = models.TextField('简介', default='')
    num_views = models.CharField('浏览量', max_length=255, default=0)
    num_comment = models.CharField('评论量', max_length=255, default=0)
    is_active = models.BooleanField(default=1)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'

