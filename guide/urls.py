from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('code/', views.CodeView.as_view(), name='code_list'),
    path('code/<int:pk>/', views.CodeDetail.as_view(), name='code_detail')
]