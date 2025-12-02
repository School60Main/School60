from django import forms
from .models import StudyMaterial

class StudyMaterialForm(forms.ModelForm):
    class Meta:
        model = StudyMaterial
        fields = ['title', 'description', 'subject', 'file']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название материала'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание', 'rows': 3}),
            'subject': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'title': 'Название материала',
            'description': 'Описание',
            'subject': 'Предмет',
            'file': 'Файл',
        }
