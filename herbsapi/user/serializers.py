from rest_framework import serializers
from .models import *


class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__' # 输出所以字段信息
