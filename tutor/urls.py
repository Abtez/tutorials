from . import views
from django.urls import path

urlpatterns=[
    path('', views.index, name='index'),
    path('api/tutorials/', views.tutorials_list),
    path('api/tutorials/<int:pk>', views.image_detail)
]