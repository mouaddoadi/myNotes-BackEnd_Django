from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('api/notes/', views.getNotes, name="notes"),
    path('notes/<str:pk>', views.getNote, name="note"),
]