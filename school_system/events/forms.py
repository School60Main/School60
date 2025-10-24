# events/forms.py
from django import forms
from .models import Event

# events/forms.py
from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'place', 'participants_classes', 'participants_teachers', 'date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'place': forms.TextInput(attrs={'class': 'form-control'}),
            'participants_classes': forms.TextInput(attrs={'class': 'form-control'}),
            'participants_teachers': forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'name': 'Название мероприятия',
            'place': 'Кабинет',
            'participants_classes': 'Классы участников',
            'participants_teachers': 'Учителя',
            'date': 'Дата',
            'time': 'Время',
            
        }