from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Notification
from .forms import NotificationForm
from django.db.models import Q

@login_required
def create_notification(request):
    if not request.user.is_admin:
        return redirect('dashboard')

    if request.method == 'POST':
        form = NotificationForm(request.POST, request.FILES)
        if form.is_valid():
            notification = form.save(commit=False)
            notification.sender = request.user
            notification.save()
            return redirect('notifications:list_notifications')
    else:
        form = NotificationForm()
    return render(request, "notifications/create_notification.html", {"form": form})


@login_required
def list_notifications(request):
    notifications = Notification.objects.filter(
        Q(receiver=request.user) | Q(to_all_teachers=True)
    ).order_by('-created_at')
    return render(request, "notifications/list_notifications.html", {"notifications": notifications})


@login_required
def notification_detail(request, pk):
    notification = get_object_or_404(Notification, pk=pk)

    # Проверка доступа
    if notification.receiver and notification.receiver != request.user:
        return redirect('notifications:list_notifications')

    # Автоматическое помечание как прочитанное
    if not notification.is_read and (notification.receiver == request.user or notification.to_all_teachers):
        notification.is_read = True
        notification.save()

    return render(request, "notifications/notification_detail.html", {"notification": notification})
