from django.db import models
from users.models import CustomUser

class Notification(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_notifications')
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='received_notifications', null=True, blank=True)
    to_all_teachers = models.BooleanField(default=False)
    title = models.CharField(max_length=255)
    message = models.TextField()
    attachment = models.FileField(upload_to='notifications/', blank=True, null=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} → {self.receiver if self.receiver else 'Все учителя'}"

    class Meta:
        ordering = ['-created_at']
    