from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, StreamingHttpResponse, FileResponse
from tripdiary.models import User, Diary, Credit
from tripdiary.Serializer import UserSerializer, DiarySerializer
from rest_framework.renderers import JSONRenderer
from django.core import serializers
import json, os
import ast


def index(request):
    return HttpResponse('Test')


def login(request):
    context = {'status': 400, 'content': 'null'}
    if request.method == 'POST':
        username = request.POST.get('username', )
        password = request.POST.get('password')
        try:
            user = User.manager.get(username=username, password=password)
            if user:
                context['status'] = 200
        except:
            context['status'] == 400
        if context['status'] == 200:
            serializer = UserSerializer(user)
            context['content'] = serializer.data
        else:
            context['content'] = 'null'
        content = JSONRenderer().render(context)
        return HttpResponse(content)
    return HttpResponse(JSONRenderer(), render(context))


# 用户注册
def register(request):
    context = {'status': 400}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.manager.create(username, password)
            user.save()
            if user:
                context['status'] = 200
        except Exception:
            context['status'] == 400
        return HttpResponse(JSONRenderer().render(context))
    return HttpResponse(JSONRenderer().render(context))
