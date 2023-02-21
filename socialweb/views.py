from django.shortcuts import render,redirect
from django.views.generic import View
from socialweb.forms import Userform,Loginform,Postform,PostEditform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from api.models import Posts,UserProfile
# Create your views here.
class SignView(View):
    def get(self,request,*args,**kwargs):
        form=Userform()
        return render(request,"register.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form=Userform(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return redirect("signin")
        else:
            return render(request,"register.html",{"form":form})
    
class LoginView(View):
    def get(self,request,*args,**kwargs):
        form=Loginform()
        return render(request,"login.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form=Loginform(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            psd=form.cleaned_data.get("password")
            usr=authenticate(username=uname,password=psd)
            if usr:
                login(request,usr)
                return redirect("home")
            else:
                return render(request,"login.html",{"form":form})
            

class IndexView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"index.html")

class PostCreateView(View):
    def get(self,request,*args,**kwargs):
        form=Postform()
        return render(request,"post-add.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=Postform(request.POST)
        if form.is_valid():
            form.instance.user=request.user
            form.save()
            print("saved")
            return redirect("post-list")
        else:
            return render(request,"post-add.html",{"form":form})

class PostListView(View):
    def get(self,request,*args,**kwargs):
        qs=Posts.objects.filter(user=request.user).order_by("-date")
        return render(request,"post-list.html",{"posts":qs})

class PostDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Posts.objects.get(id=id)
        return render(request,"post-detail.html",{"posts":qs})

class PostDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Posts.objects.filter(id=id).delete()
        return redirect("post-list")

class PostEditView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        obj=Posts.objects.get(id=id)
        form=PostEditform(instance=obj)
        return render(request,"post-edit.html",{"form":form})

    def post(self,request,*args,**kwargs):
        id=kwargs.get("id")
        obj=Posts.objects.get(id=id)
        form=PostEditform(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("post-list")
        else:
            return render(request,"post-edit.html",{"form":form})

class PostListAllView(View):
    def get(self,request,*args,**kwargs):
        logged_in_user=request.user
        qs=Posts.objects.exclude(id=logged_in_user.id)
        return render(request,"post-alldetail.html",{"posts":qs})

class UserProfileView(View):
    def get(self,request,*args,**kwargs):
        
        return render(request,"user-pro.html")


     

            