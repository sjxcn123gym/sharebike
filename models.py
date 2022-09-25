#from django.db import models
from django.db import models
# Create your models here.


class login_msg(models.Model):
    user = models.CharField(max_length=30)#用户名
    pw = models.CharField(max_length=128) #用户密码
    mail = models.CharField(max_length=30)#邮件
