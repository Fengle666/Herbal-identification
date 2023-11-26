from rest_framework import serializers
from .models import *


class WikipediaInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wikipedia
        fields = '__all__' # 输出所以字段信息
