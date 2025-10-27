from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Announcement

@login_required
def announcement_list(request):
    """
    Страница со всеми объявлениями (для всех пользователей)
    """
    announcements = Announcement.objects.filter(is_active=True)
    return render(request, 'announcements/announcement_list.html', {'announcements': announcements})

@login_required
def recent_announcements(request, count=5):
    """
    Для главной страницы: вывод последних count активных объявлений
    """
    announcements = Announcement.objects.filter(is_active=True)[:count]
    return render(request, 'announcements/_recent_announcements.html', {'announcements': announcements})
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.utils import admin_required  # твой декоратор для админов
from .models import Announcement
from .forms import AnnouncementForm

@login_required
@admin_required
def admin_dashboard(request):
    announcements = Announcement.objects.all()
    return render(request, 'announcements/admin_dashboard.html', {'announcements': announcements})

@login_required
@admin_required
def add_announcement(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Объявление добавлено!")
            return redirect('announcements:admin_dashboard')
    else:
        form = AnnouncementForm()
    return render(request, 'announcements/announcement_form.html', {'form': form, 'title': 'Добавить объявление'})

@login_required
@admin_required
def edit_announcement(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    if request.method == 'POST':
        form = AnnouncementForm(request.POST, request.FILES, instance=announcement)
        if form.is_valid():
            form.save()
            messages.success(request, "Объявление обновлено!")
            return redirect('announcements:admin_dashboard')
    else:
        form = AnnouncementForm(instance=announcement)
    return render(request, 'announcements/announcement_form.html', {'form': form, 'title': 'Редактировать объявление'})

@login_required
@admin_required
def delete_announcement(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    if request.method == 'POST':
        announcement.delete()
        messages.success(request, "Объявление удалено!")
        return redirect('announcements:admin_dashboard')
    return render(request, 'announcements/announcement_confirm_delete.html', {'announcement': announcement})
