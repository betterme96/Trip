from django.db import models
import django.utils.timezone as timezone

#创建模型的管理类
class UserManager(models.Manager):
    def create(self, username, password):
        user = User()
        user.username = username
        user.password = password
        return user

#创建模型类
class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    def __str__(self):
        return self.username

    #创建元数据
    class Meta:
        ordering = ['id']
        #设置表名字
        db_table = 'user'
    #添加管理器（django的模型进行数据库查询操作的接口，django应用的每个模型都拥有至少一个管理器）
    manager = UserManager()

class Diary(models.Model):
    PUBLIC_CHOICES = (
        (u'0', '仅自己'),
        (u'1', '所有人'),
    )
    d_date = models.DateTimeField(default=timezone.now)
    d_title = models.CharField(max_length=20)
    d_author = models.ForeignKey(User, on_delete=models.CASCADE,)
    d_content = models.CharField(max_length=1000)
    d_location = models.CharField(max_length=200)
    d_ispublic = models.CharField(max_length=2, choices=PUBLIC_CHOICES)

    def __str__(self):
        return  self.d_title
    class Meta:
        ordering = ['id']
        db_table = 'diary'


class  Credit(models.Model):
    c_date = models.DateTimeField(default=timezone.now)
    c_diary = models.ForeignKey(Diary, on_delete=models.CASCADE)
    c_author = models.ForeignKey(User, on_delete=models.CASCADE,)
    c_content = models.CharField(max_length=200)


