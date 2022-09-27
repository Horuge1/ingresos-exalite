from django.forms import *
from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm, UsernameField


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'

    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))


class BetCalculatorForm(forms.Form):
    odd = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 0}))
    gain = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 0}))


class BetCreateForm(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(BetCreateForm, self).__init__(*args, **kwargs)
    #     self.fields['user'].value = self.request.user
    #
    class Meta:
        model = Bet
        fields = '__all__'
        exclude = ['user', 'result', 'result_desc', 'bank']
        widgets = {
            'event': TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'pick': TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'type': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'amount': NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'odd': NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),

        }


class BetUpdateForm(ModelForm):
    class Meta:
        model = Bet
        fields = ['result', 'result_desc']
        widgets={
            'result_desc': TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'result': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
        }
