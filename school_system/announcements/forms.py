from django import forms
from .models import Announcement

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'content','image', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

        }
        labels = {
            'title': 'Заголовок',
            'content': 'Содержание',
            'image': 'Изображение',
            'is_active': 'Активно',
        }

        