from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import userinfo
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import userinfoserializers

from rest_framework.decorators import api_view





# Create your views here.

# def home(request):
#     return render(request,'home1.html')



class UserApi(APIView):
    def get(self,request, pk = None, format=None):
        id = pk
        if id is not None:
            info = userinfo.objects.get(id  = id)
            serializer = userinfoserializers(info)
            return Response(serializer.data)
        info = userinfo.objects.all()
        serializer = userinfoserializers(info, many=True)
        return Response(serializer.data)

    def post(self,request, format=None ,partial=True):
        serializer = userinfoserializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            obj_generator = serializers.json.Deserializer(request.POST['serializer.data'])
            print(obj_generator)

            return Response({'msg': 'Data Created'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request,format = None):
        no = request.data['id']
        info = userinfo.objects.get(id=no)
        serializer= userinfoserializers(info,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partialy data updated'})
        return Response(serializer.errors)






