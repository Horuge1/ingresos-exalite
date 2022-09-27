from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import *
# from django.views.generic.edit import CreateView as asd
from .models import *
from .forms import *
from django.contrib.auth.models import User
import numpy as np
from django.db.models.functions import Cast
from django.db.models import CharField


class Home(TemplateView):
    template_name = 'bets/index.html'


class BetCalculator(FormView):
    template_name = 'tools/bet.html'
    form_class = BetCalculatorForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'odd' in self.request.GET and 'gain' in self.request.GET:
            num1 = self.request.GET['odd']
            num2 = self.request.GET['gain']
            a = np.array([[float(num1), -1],
                         [-1, 1]])
            b = np.array([[0],
                         [float(num2)]])
            ainv = np.linalg.inv(a)
            x = np.multiply(ainv, b)

            context['num1'] = round(x[1][0], 2)
            context['num2'] = round(x[1][1], 2)
        return context


class BetList(LoginRequiredMixin, ListView):
    model = Bet
    template_name = 'bets/index.html'

    def get_queryset(self):
        return self.request.user.bet_set.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user
        context['evolution'] = list(Bet.objects.annotate(y=Cast('created_at', output_field=CharField())).values('y').annotate(
            a=Sum('amount')).values('y','a')
        )
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
