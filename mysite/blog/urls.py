from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('about/',views.about),
    path('asso_list/',views.asso_list),
    path('test/',views.test),
    path('<int:blog_pk>',views.blog_detail,name="blog detail"),
]