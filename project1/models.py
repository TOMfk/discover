from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=32, verbose_name="用户姓名")
    password = models.CharField(max_length=128, verbose_name="密码")


    def __str__(self):
        return self.username


class UserToken(models.Model):
    user = models.OneToOneField("User")
    token = models.CharField(max_length=32)
    create_time = models.DateTimeField(auto_now=True)


class Desc(models.Model):
    user = models.OneToOneField("User")
    time = models.DateField(verbose_name="发布日期", blank=True, null=True)
    content = models.TextField("内容", max_length=512)



