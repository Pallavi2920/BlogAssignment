from django.urls import path
from .import views

urlpatterns = [
    path('',views.list,name='list'),
    path('create/',views.create,name='create'),
    path('detail/',views.detail,name='detail'),
    path('list/<str:pk>/',views.detail,name='detail'),
    path('list/<str:pk>/update/',views.update,name='update'),
    path('list/<str:pk>/delete/',views.delete,name='delete'),
]
