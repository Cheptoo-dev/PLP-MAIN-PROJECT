from django import forms
from .models import Trade

class TradeForm(forms.ModelForm):
    class Meta:
        model = Trade  # The model this form is based on
        fields = ['date', 'type', 'entry_price', 'exit_price', 'profit_loss', 'strategy', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  # Customize the date input to show a date picker
        }
