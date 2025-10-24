# awards/forms.py
from django import forms
from .models import Award

class AwardForm(forms.ModelForm):
    class Meta:
        model = Award
        fields = ['student_name', 'student_class', 'event_name', 'place','resaulted', 'date', 'photo']
        widgets = {
            'student_name': forms.TextInput(attrs={'class': 'form-control'}),
            'student_class': forms.TextInput(attrs={'class': 'form-control'}),
            'event_name': forms.TextInput(attrs={'class': 'form-control'}),
            'place': forms.TextInput(attrs={'class': 'form-control'}),
            'resaulted' : forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'student_name': 'ФИО ученика',
            'student_class': 'Класс',
            'event_name': 'Мероприятие',
            'place': 'Место проведения',
            'resaulted': 'Результат',
            'date': 'Дата',
            'photo': 'Фото',
        }