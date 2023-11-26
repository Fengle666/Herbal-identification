from django.db import models

# Create your models here.


class Wikipedia(models.Model):
    # 显示功效、生长环境、规模化种植
    name = models.CharField(max_length=20, verbose_name='中草药名称')
    describe = models.CharField(max_length=200, null=True, verbose_name='描述')
    efficacy = models.TextField(null=True, verbose_name='功效作用')
    environment = models.TextField(null=True, verbose_name='生长环境')
    cultivation = models.TextField(null=True, verbose_name='栽培技术')
    oviews = models.IntegerField(default=0, verbose_name='浏览量')
    image = models.ImageField(blank=True, null=True, verbose_name='图片')
    create_time = models.DateTimeField(blank=True,auto_now_add=True, null=True, verbose_name='创建时间')


    class Meta:
        db_table = 'wikipedia'  # 设置数据库表名
        verbose_name = '百科表'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.name