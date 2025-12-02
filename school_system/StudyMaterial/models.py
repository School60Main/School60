from django.db import models
from users.models import CustomUser

class StudyMaterial(models.Model):
    SUBJECT_CHOICES = [
        ('math', 'Математика'),
        ('physics', 'Физика'),
        ('chemistry', 'Химия'),
        ('biology', 'Биология'),
        ('history', 'История'),
        ('literature', 'Литература'),
        ('english', 'Английский язык'),
        # Добавляйте свои предметы
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES)
    file = models.FileField(upload_to='study_materials/')
    uploaded_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-uploaded_at']
        verbose_name = "Учебный материал"
        verbose_name_plural = "Учебные материалы"
