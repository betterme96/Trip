#!/usr/bin/env python
#-*- coding:utf-8 -*-
from rest_framework.serializers import ModelSerializer
from tripdiary.models import User, Diary

class UserSerializer(ModelSerializer):
    # 设置序列化
    class Meta:
        model = User
        fields = "__all__"


class DiarySerializer(ModelSerializer):
    # 设置序列化
    class Meta:
        model = Diary
        fields = "__all__"