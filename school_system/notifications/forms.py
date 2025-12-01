from django import forms
from .models import Notification
from users.models import CustomUser

class NotificationForm(forms.ModelForm):
    to_all_teachers = forms.BooleanField(
        required=False,
        label="Отправить всем учителям",
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"})
    )

    receiver = forms.ModelChoiceField(
        queryset=CustomUser.objects.filter(is_teacher=True),
        label="Выберите учителя",
        required=False
    )

    class Meta:
        model = Notification
        fields = ['title', 'message', 'attachment', 'receiver', 'to_all_teachers']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'attachment': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

        labels = {
            'title': 'Заголовок',
            'message': 'Сообщение',
            'attachment': 'Приложение',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Показываем ФИО вместо username
        self.fields['receiver'].queryset = CustomUser.objects.filter(is_teacher=True)
        self.fields['receiver'].label_from_instance = lambda obj: f"{obj.last_name} {obj.first_name}"
