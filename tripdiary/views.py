from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, StreamingHttpResponse, FileResponse
from rest_framework.decorators import api_view
from django.shortcuts import redirect
from tripdiary.models import User, Diary, Credit
from tripdiary.Serializer import UserSerializer, DiarySerializer
from rest_framework.renderers import JSONRenderer
from django.core import serializers
import json, os
import ast


def index(request):
    return HttpResponse('Test')

#用户登陆
@api_view(['POST'])
def login(request):
    context = {'status': 400}
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            user = User.manager.get(username=username, password=password)
            if user:
                context['status'] = 200
        except:
            context['status'] == 400
        content = JSONRenderer().render(context)
        return HttpResponse(content)
    return HttpResponse(JSONRenderer(), render(context))


# 用户注册
@api_view(['POST'])
def register(request):
    context = {'status': 400}
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            user = User.manager.create(username, password)
            user.save()
            if user:
                context['status'] = 200
        except Exception:
            context['status'] == 400
        return HttpResponse(JSONRenderer().render(context))
    return HttpResponse(JSONRenderer().render(context))


#文件上传

def upload(request):
    context = {'status': 400}
    if request.method == 'POST':
        handle_uploaded_file(request.FILES['file'], str(request.FILES['file']))
        context['status'] = 200
        return HttpResponse(JSONRenderer().render(context))
    return HttpResponse(JSONRenderer().render(context))

def handle_uploaded_file(file, filename):
    if not os.path.exists('upload/'):
        os.mkdir('upload/')
    with open('upload/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

#保存日记
@api_view(['POST'])
def diary_save(request):
    context = {'status': 400}
    if request.method == 'POST':
        #获取到对象之后序列化
        d_title = request.data.get('d_title')
        d_author = request.data.get('d_author')
        d_content = request.data.get('d_content')
        d_date = request.data.get('d_date')
        # 先在USER表中查询出前端选中的用户对应对象
        user1 = User.manager.get(username=d_author)
        try:
            diary = Diary(d_title=d_title, d_author=user1, d_content=d_content,d_date=d_date)
            diary.save()
            if diary:
                context['status'] = 200
        except Exception:
            context['status'] == 400
        return HttpResponse(JSONRenderer().render(context))
    return HttpResponse(JSONRenderer().render(context))

#删除日记
@api_view(['POST'])
def diary_delete(request):
    context = {'status': 400}
    if request.method == 'POST':
        #获取到对象之后序列化
        title = request.data.get('title')
        try:
            diary = Diary.manager1.filter(d_title=title)
            if diary:
                diary.delete()
                context['status'] = 200
        except Exception:
            context['status'] == 500
        return HttpResponse(JSONRenderer().render(context))
    return HttpResponse(JSONRenderer().render(context))
#更新日记
@api_view(['POST'])
def diary_update(request):
    context = {'status': 400}
    if request.method == 'POST':
        #获取到对象之后序列化
        d_title = request.data.get('d_title')
        d_title_new = request.data.get('d_title_new')
        d_content = request.data.get('d_content')
        context['status'] = 100
        try:
            diary = Diary.manager1.filter(d_title=d_title)
            diary.update(d_title=d_title_new, d_content=d_content)
            context['status'] = 200
        except Exception:
            context['status'] == 500
        return HttpResponse(JSONRenderer().render(context))
    return HttpResponse(JSONRenderer().render(context))

# 查询指定用户的日记信息
@api_view(['POST'])
def userdiary(request):
    context = {'status': 400, 'content': 'null'}
    if request.method == 'POST':
        username = request.data.get('username')
        try:
            diary_list = Diary.manager1.filter(d_author__username=username).values_list('id', 'd_title', 'd_author__username', 'd_content', 'd_date')
            if diary_list.count()!= 0:
                context['status'] = 200
                diary_list1 = convert_to_json_string(diary_list)
                # 这里先将json对象转化为列表进行存储缺少这一步的话将无法解析。
        except:
            context['status'] == 500
        return HttpResponse(diary_list1)
    return HttpResponse(JSONRenderer(), render(context))


#查询所有用户的日记信息
@api_view(['POST'])
def alldiary(request):
    context = {'status': 400, 'content': 'null'}
    if request.method == 'POST':
        diary_list = Diary.manager1.all().values_list('id', 'd_title', 'd_author__username', 'd_content','d_date')
        ask_list1 = convert_to_json_string(diary_list)
        return HttpResponse(ask_list1)
    return HttpResponse(JSONRenderer().render(context))

def convert_to_json_string(data):
        return json.dumps({'diary':
                           [{'id': int(i[0]),
                             'title': i[1],
                             'author': i[2],
                             'content':i[3],
                             'date':i[4],
                             } for i in data]}, indent=4)




