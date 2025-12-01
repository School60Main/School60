from django.db import models

class Announcement(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    content = models.TextField("Содержание")
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField("Активно", default=True)
    image = models.ImageField("Изображение", upload_to='announcements/', blank=True, null=True)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

