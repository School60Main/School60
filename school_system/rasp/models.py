from django.db import models


class LessonSchedule(models.Model):
    DAYS = [
        ("Понедельник", "Понедельник"),
        ("Вторник", "Вторник"),
        ("Среда", "Среда"),
        ("Четверг", "Четверг"),
        ("Пятница", "Пятница"),
        ("Суббота", "Суббота"),
    ]

    day_of_week = models.CharField("День недели", max_length=20, choices=DAYS)
    lesson_number = models.PositiveIntegerField("Номер урока")
    class_name = models.CharField("Класс", max_length=20)
    subject = models.CharField("Предмет", max_length=255)
    teacher = models.CharField("Учитель", max_length=255)
    classroom = models.CharField("Кабинет", max_length=50)

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Расписание уроков"
        ordering = ["day_of_week", "lesson_number"]

    def __str__(self):
        return f"{self.day_of_week} — {self.class_name} ({self.lesson_number} урок)"
