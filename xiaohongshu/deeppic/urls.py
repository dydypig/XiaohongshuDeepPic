from django.urls import path
from . import views as deeppicview

urlpatterns = [
    path('', deeppicview.home, name='home'),
    path('cloud/',deeppicview.CloudPicsView.as_view(), name='cloud_pics'),
    path('cloud/<int:pk>/',deeppicview.cloud_pic_select, name='cloud_pics_select'),
    path('process/',deeppicview.process_pic,name='process_pic')
]