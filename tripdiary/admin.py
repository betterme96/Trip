from django.contrib import admin
from.models import User
from.models import Diary
from.models import Credit

class UserInfoAdmin(admin.ModelAdmin):
    #显示字段
    list_display = ['id', 'username', 'password']
    #搜索字段
    search_fields = ['username']
    #分页
    list_per_page = 20


class DiaryInfoAdmin(admin.ModelAdmin):
    # 显示字段
    list_display = ['id', 'd_title', 'd_author', 'd_date']
    # 搜索字段
    search_fields = ['d_title']
    # 分页
    list_per_page = 20
    #排序
    ordering = ('id',)

class CreditAdmin(admin.ModelAdmin):
    list_display = ['id', 'c_author', 'c_diary', 'c_content', 'c_date']
    list_per_page = 20
    ordering = ('c_date',)

admin.site.register(User, UserInfoAdmin)
admin.site.register(Diary, DiaryInfoAdmin)
admin.site.register(Credit, CreditAdmin)
