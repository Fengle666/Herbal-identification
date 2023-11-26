from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import User
import json


# 用户登录接口

# 用户登录试图
def Login(request):

    if request.method == 'POST':
        # 处理数据
        print(111)
        postBody = request.body
        postBodyStr = postBody.decode('utf-8')
        json_result = json.loads(postBodyStr)
        username = json_result['username']
        password = json_result['password']
        data = {}

        userDate = User.objects.filter(username=username, password=password)
        for user in userDate:
            data = {
                "id": user.id,
                "username": user.username,
                "name": user.name,
            }
        if not userDate.exists():
            return JsonResponse({"code": 500, "error": "用户名或密码错误"})

        print(data)
        return JsonResponse({"code": 200, "data": data})



