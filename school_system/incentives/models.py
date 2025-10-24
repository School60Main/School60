from django.db import models
from users.models import CustomUser

class Incentive(models.Model):
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'teacher'}, verbose_name="Учитель")
    period = models.CharField(max_length=100, verbose_name="Период выплаты (например, Сентябрь 2025)")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма выплаты")
    comment = models.TextField(blank=True, null=True, verbose_name="Комментарий")
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='incentives')

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Стимулирующая выплата"
        verbose_name_plural = "Стимулирующие выплаты"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.teacher} — {self.period}"
