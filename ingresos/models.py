from django.db import models
from django.db.models import Sum, Avg, Max
from django.contrib.auth.models import User


class Balance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    initial_bank = models.FloatField()

    def total_amount(self):
        if self.user.bet_set.count()>1:
            return self.user.bet_set.aggregate(total=Sum('amount'))['total']
        return 0

    def total_gain(self):
        total = 0
        bets = self.user.bet_set.all()
        for bet in bets:
            total += bet.gain()
        return round(total, 2)

    def bank(self):
        return round(self.total_gain()+self.initial_bank, 2)

    def profit(self):
        return round(((self.bank()-self.initial_bank)/self.initial_bank)*100, 2)

    def yield_numb(self):
        if self.user.bet_set.count() > 1:
            return round((self.total_gain()/self.total_amount())*100, 2)
        return 0

    def total_wins(self):
        return self.user.bet_set.filter(result='W').count()

    def total_loses(self):
        return self.user.bet_set.filter(result='L').count()

    def total_null(self):
        return self.user.bet_set.filter(result='N').count()

    def win_rate(self):
        if self.user.bet_set.count() > 1:
            return round((self.total_wins()/(self.total_loses()+self.total_wins()))*100, 2)
        return 0

    def odd_avg(self):
        if self.user.bet_set.count() > 1:
            return round(self.user.bet_set.aggregate(avg=Avg('odd'))['avg'], 2)
        return 0

    def amount_avg(self):
        if self.user.bet_set.count() > 1:
            return round(self.user.bet_set.aggregate(avg=Avg('amount'))['avg'], 2)
        return 0

    def max_amount(self):
        if self.user.bet_set.count() > 1:
            return self.user.bet_set.aggregate(max=Max('amount'))['max']
        return 0

    def max_gain(self):
        max_gain = 0
        bets = self.user.bet_set.all()
        for bet in bets:
            if bet.gain() > max_gain:
                max_gain = bet.gain()
        return round(max_gain, 2)


class Type(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')

    def __str__(self):
        return self.name


class Bet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.CharField(max_length=120, verbose_name='Evento')
    pick = models.CharField(max_length=120, verbose_name='Pick')
    type = models.ForeignKey(Type, verbose_name='Tipo', on_delete=models.SET_NULL, null=True)
    amount = models.FloatField(verbose_name='Apuesta')
    odd = models.FloatField(verbose_name='Cuota')
    bank = models.FloatField(verbose_name='Bank', blank=True)
    result = models.CharField(max_length=5, choices=(('W', 'W'), ('L', 'L'), ('N', 'N')), verbose_name='W/L/N', blank=True)
    result_desc = models.CharField(max_length=150, verbose_name='Resultado', blank=True)
    created_at = models.DateField(auto_now_add=True)

    def gain(self):
        if self.result == 'W':
            return round(self.amount*self.odd-self.amount, 2)
        elif self.result == 'L':
            return round(-self.amount, 2)
        else:
            return 0

    def save(self, *args, **kwargs):
        # change total_price
        self.bank=self.user.balance.bank()+self.gain()
        super(Bet, self).save(*args, **kwargs)
