# events/views.py
import json
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event
from .forms import EventForm
from users.utils import teacher_required, admin_required
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Event
from datetime import date, timedelta
from collections import defaultdict
# ----------------------------
# Список мероприятий
# ----------------------------
@login_required
def event_list(request):
    today = date.today()
    week_end = today + timedelta(days=6)

    search_class = request.GET.get('class', '')

    # Берём события на предстоящую неделю
    events = Event.objects.filter(date__range=[today, week_end]).order_by('date')
    
    if search_class:
        events = events.filter(participants_classes__icontains=search_class)

    # Группируем по дате
    events_by_date = defaultdict(list)
    for event in events:
        events_by_date[event.date].append(event)

    return render(request, 'events/event_list.html', {
        'events_by_date': dict(events_by_date),
        'search_class': search_class,
        'today': today
    })
@login_required
def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/event_detail.html', {'event': event})


# ----------------------------
# Создание мероприятия (только админ)
# ----------------------------
@login_required
@admin_required
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            messages.success(request, 'Мероприятие добавлено!')
            return redirect('events:event_list')
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form})

# ----------------------------
# Редактирование мероприятия (только админ)
# ----------------------------
@login_required
@admin_required
def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk)
    form = EventForm(request.POST or None, instance=event)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Мероприятие обновлено!')
        return redirect('events:event_list')
    return render(request, 'events/event_form.html', {'form': form})

# ----------------------------
# Удаление мероприятия (только админ)
# ----------------------------
@login_required
@admin_required
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        messages.success(request, 'Мероприятие удалено!')
        return redirect('events:event_list')
    return render(request, 'events/event_confirm_delete.html', {'event': event})
