from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

# 定义用户模型类
class User(models.Model):
    username = models.CharField(max_length=22, verbose_name='用户名')
    password = models.CharField(max_length=22, verbose_name='密码')
    name = models.CharField(max_length=20, null=True, verbose_name='昵称')
    create_time = models.DateTimeField(blank=True, auto_now_add=True, null=True, verbose_name='创建时间')
    is_stats = models.CharField(max_length=2, verbose_name='启用状态')


    class Meta:
        db_table = 'user'  # 设置数据库表名
        verbose_name = '用户'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.username