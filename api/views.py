from django.shortcuts import render
from rest_framework.response import Response
from api.serializers import PostsSerializers,UserSerializer
from django.contrib.auth.models import User
from api.models import Posts
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import authentication,permissions

# Create your views here.
class PostsModelViewsetView(ModelViewSet):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=PostsSerializers
    queryset=Posts.objects.all()

    def perform_create(self, serializer):
            serializer.save(user=self.request.user)
    #def create(self, request, *args, **kwargs):
        #serializer=PostsSerializers(data=request.data)
        #if serializer.is_valid():
           # serializer.save(user=request.user)
            #return Response(data=serializer.data)
        #else:
            #return Response(data=serializer.errors)


    def list(self, request, *args, **kwargs):
        qs=Posts.objects.all()
        serializer=PostsSerializers(qs,many=True)
        print(request.user)
        return Response(data=serializer.data)
  
class UserView(ModelViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all()

    

    def create(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            ur=User.objects.create_user(**serializer.validated_data)
            serializer=UserSerializer(ur,many=False) #deseialization
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)