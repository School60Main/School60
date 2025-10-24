# awards/models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Award(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='awards')
    student_name = models.CharField("ФИО ученика", max_length=255)
    student_class = models.CharField("Класс", max_length=50)
    event_name = models.CharField("Название мероприятия", max_length=255)
    place = models.CharField("Место", max_length=255)
    photo = models.ImageField("Фото", upload_to='awards_photos/', blank=True, null=True)
    date = models.DateField("Дата мероприятия")
    created_at = models.DateTimeField(auto_now_add=True)
    resaulted = models.CharField("Результат", max_length=255, blank=True, null=True)

    class Meta:
        ordering = ['-date', 'student_name']
        verbose_name = "Достижение"
        verbose_name_plural = "Достижения"

    def __str__(self):
        return f"{self.student_name} — {self.event_name}"
