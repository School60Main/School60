from django import forms
from .models import Incentive

class IncentiveForm(forms.ModelForm):
    class Meta:
        model = Incentive
        fields = '__all__'
        widgets = {
            'teacher_name': forms.TextInput(attrs={'class': 'form-control'}),
            'reason': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        labels = {
            'teacher_name': 'Преподаватель',
            'reason': 'Причина',
            'amount': 'Сумма',
            'date': 'Дата',
        }