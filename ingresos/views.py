from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import *
# from django.views.generic.edit import CreateView as asd
from .models import *
from .forms import *
from django.contrib.auth.models import User


@login_required
def bet_calculator(request):
    return render(request, 'bets/index.html')


class UserList(ListView):
    model = User
    template_name = 'users/index.html'


class BetList(LoginRequiredMixin, ListView):
    model = Bet
    template_name = 'bets/index.html'

    def get_queryset(self):
        return self.request.user.bet_set.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user
        return context


class BetCreate(LoginRequiredMixin, CreateView):
    model = Bet
    form_class = BetCreateForm
    template_name = 'bets/create.html'
    success_url = reverse_lazy('bet-index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BetUpdate(LoginRequiredMixin, UpdateView):
    model = Bet
    form_class = BetUpdateForm
    template_name = 'bets/update.html'
    success_url = reverse_lazy('bet-index')


class BetDelete(LoginRequiredMixin, DeleteView):
    model = Bet
    template_name = 'bets/delete.html'
    success_url = reverse_lazy('bet-index')
