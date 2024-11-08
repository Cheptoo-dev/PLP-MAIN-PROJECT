from django.urls import path
from . import views

urlpatterns = [
    path('', views.trade_list, name='trade_list'),
    path('add/', views.trade_add, name='trade_add'),
    path('edit/<int:id>/', views.trade_edit, name='trade_edit'),
    path('delete/<int:id>/', views.trade_delete, name='trade_delete'),
]
