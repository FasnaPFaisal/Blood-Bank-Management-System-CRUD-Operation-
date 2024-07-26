from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('donate/', views.donate, name='donate'),
    path('details/<id>',views.details, name='details'),
    path('update/<id>',views.update, name='update'),
    path('delete/<id>',views.delete, name='delete'),
]