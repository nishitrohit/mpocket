from rest_framework import serializers
from .models import userinfo

class userinfoserializers(serializers.ModelSerializer):
    Name = serializers.CharField(max_length=100,default='')
    Mobileno = serializers.CharField(max_length=10,default='')
    Email = serializers.EmailField(max_length=200,default='')
    add = serializers.CharField(max_length=100,default='')
    village = serializers.CharField(max_length=100,default='')

    def create(self, validated_data):
        return userinfo.objects.create(**validated_data)



    class Meta:
        model = userinfo
        fields = '__all__'
