from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.my_expense, name='cost-list'),
    path('add/', views.add_expense, name='add-expense'),
]


