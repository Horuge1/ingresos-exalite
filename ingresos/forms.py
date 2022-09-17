from django.forms import ModelForm, Form
from django.forms.widgets import HiddenInput
from .models import *


# class BetCalculatorForm(Form):
#     quote=


class BetCreateForm(ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super(BetCreateForm, self).__init__(*args, **kwargs)
    #     self.fields['user'].value = self.request.user
    #
    class Meta:
        model = Bet
        fields = '__all__'
        exclude = ['user', 'result', 'result_desc']
        # widgets = {
        #             'user': HiddenInput
        #         }


class BetUpdateForm(ModelForm):
    class Meta:
        model = Bet
        fields = ['result', 'result_desc']

