from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:budget_id>/', views.budget_detail, name='budget_detail')
]
