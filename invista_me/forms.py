from django.forms import ModelForm
from .models import Investimento

class InvestimentoModelForm(ModelForm):
    class Meta:
        model = Investimento
        fields = '__all__'