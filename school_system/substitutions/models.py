from django.db import models

class Substitution(models.Model):
    date = models.DateField("Дата")
    replaced_teacher = models.CharField("ФИО учителя, которого замещают", max_length=255)
    lesson_number = models.CharField("Номер урока", max_length=10)
    class_name = models.CharField("Класс", max_length=20)
    substitute_teacher = models.CharField("ФИО замещающего учителя", max_length=255)
    subject = models.CharField("Предмет", max_length=255)
    classroom = models.CharField("Кабинет", max_length=50)

    class Meta:
        verbose_name = "Замена"
        verbose_name_plural = "Замены"
        ordering = ["date", "lesson_number"]

    def __str__(self):
        return f"{self.date} — {self.class_name} ({self.lesson_number} урок)"
