from django.urls import path
from socialweb import views
urlpatterns=[
    path("signup",views.SignView.as_view(),name="register"),
    path("",views.LoginView.as_view(),name="signin"),
    path("home",views.IndexView.as_view(),name="home"),
    path("posts/add/",views.PostCreateView.as_view(),name="post-add"),
    path("posts/all",views.PostListView.as_view(),name="post-list"),
    path("posts/detail/<int:id>/",views.PostDetailView.as_view(),name="post-detail"),
    path("posts/<int:id>/remove/",views.PostDeleteView.as_view(),name="post-delete"),
    path("posts/<int:id>/change/",views.PostEditView.as_view(),name="post-edit"),
    path("posts/otherall",views.PostListAllView.as_view(),name="post-alldetail"),
    path("userpro/",views.UserProfileView.as_view(),name="userpro")
    
   

]