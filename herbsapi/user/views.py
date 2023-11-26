from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserInfoSerializer
from .models import *

# 系统管理用户接口


# 系统管理用户相关接口
class UserAdminList(ModelViewSet):
    queryset = User.objects.all()  # 指明该视图集在查询数据时使用的查询集
    serializer_class = UserInfoSerializer  # 指明该视图在进行序列化或反序列化时使用的序列化器
    filter_fields = ('username',)


