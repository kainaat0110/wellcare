from django.urls import path
from . import views
urlpatterns = [
    path('', views.index9, name="login"),
    path('login.html', views.index2, name="login"),
     path('add.html', views.index3, name="add"),
      path('diary.html', views.index4, name="diary"),
      path('comm.html', views.index5, name="comm"),
      path('sos.html', views.index6, name="sos"),
      path('afterlogin.html', views.index7,name="afterlogin"),
      path('therapist.html', views.index8,name="therapist"),



]
