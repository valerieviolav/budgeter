from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Budget
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    user = request.user
    user_budgets = Budget.objects.filter(user=user)
    context = {'user': user, 'user_budgets': user_budgets}
    return render(request, 'budgets/budgets_index.html', context)

@login_required
def budget_detail(request, budget_id):
    budget = get_object_or_404(Budget, pk=budget_id, user=request.user)
    context = {'budget': budget}
    return render(request, 'budgets/budget.html', context)

