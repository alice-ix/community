from django.urls import path
from . import views


urlpatterns = [
    path('detail/<int:pk>/', views.boardDetail),
    path('list/', views.boardlist),
    path('write/', views.boardwrite),
]
