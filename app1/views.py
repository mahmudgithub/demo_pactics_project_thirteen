# cost_management/views.py

from django.shortcuts import render
from .models import Expense
from .forms import ExpenseForm


def my_expense(request):
    model = Expense
    expenses = Expense.objects.all()
    context = {'expenses': expenses}
    return render(request, 'home.html', context)

def add_expense(request):
    form = ExpenseForm
    return render(request, 'home.html', {'form': form})