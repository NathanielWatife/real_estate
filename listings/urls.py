from django.urls import path
from .import views

urlpatterns = [
    path('', views.Items, name="items"),
    path('getItem/<pk>/', views.getItem, name="getItem"),
    path('createItem/', views.createItem, name="createItems"),
    path('updateItems/<pk>/edit/', views.updateItem, name="updateItems"),
    path('deleteItem/<pk>/delete/', views.deleteItem, name="deleteItem"),
]
