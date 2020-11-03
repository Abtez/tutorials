from . import views
from django.urls import path

urlpatterns=[
    path('api/tutorials/', views.tutorials_list),
    path('api/tutorials/<int:pk>', views.image_detail)
]