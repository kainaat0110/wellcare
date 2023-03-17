from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('community/', views.index2, name="community")
]
