# events/models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()



class Event(models.Model):
    name = models.CharField("Название мероприятия", max_length=255)
    place = models.CharField("Место", max_length=255)
    participants_classes = models.CharField("Классы участников", max_length=255, blank=True)
    participants_teachers = models.CharField("Учителя", max_length=255, blank=True)
    date = models.DateField("Дата")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    time = models.TimeField("Время", blank=True, null=True)  # новое поле
    def __str__(self):
        return f"{self.name} — {self.date}"
    

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"
        ordering = ['date' , 'time']