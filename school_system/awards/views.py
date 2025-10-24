# awards/views.py
from collections import defaultdict
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Award
from .forms import AwardForm
from users.utils import teacher_required, admin_required
from django.core.paginator import Paginator
# Список достижений
@login_required
def award_list(request):
    # Получаем текущего пользователя
    user = request.user

    # Если пользователь — администратор, показываем все достижения
    if user.is_staff:
        awards = Award.objects.all()
    else:
        # Если пользователь — не администратор (учитель), показываем только его достижения
        awards = Award.objects.filter(teacher=user)

    # Фильтрация по классу, имени ученика, дате начала и дате окончания
    search_class = request.GET.get('class', '')
    search_name = request.GET.get('name', '')
    search_start_date = request.GET.get('start_date', '')
    search_end_date = request.GET.get('end_date', '')

    if search_class:
        awards = awards.filter(student_class__icontains=search_class)
    if search_name:
        awards = awards.filter(student_name__icontains=search_name)
    if search_start_date:
        awards = awards.filter(date__gte=search_start_date)
    if search_end_date:
        awards = awards.filter(date__lte=search_end_date)

    # Пагинация
    paginator = Paginator(awards, 10)  # 10 достижений на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'awards/award_list.html', {
        'awards': page_obj,
        'search_class': search_class,
        'search_name': search_name,
        'search_start_date': search_start_date,
        'search_end_date': search_end_date,
    })

# Детальный просмотр
@login_required
def award_detail(request, pk):
    award = get_object_or_404(Award, pk=pk)
    if not request.user.is_admin and award.teacher != request.user:
        messages.error(request, "У вас нет доступа к этому достижению.")
        return redirect('awards:award_list')
    return render(request, 'awards/award_detail.html', {'award': award})

# Создание (только учитель)
@login_required
@teacher_required
def award_create(request):
    if request.method == 'POST':
        form = AwardForm(request.POST, request.FILES)
        if form.is_valid():
            award = form.save(commit=False)
            award.teacher = request.user
            award.save()
            messages.success(request, "Достижение добавлено!")
            return redirect('awards:award_list')
    else:
        form = AwardForm()
    return render(request, 'awards/award_form.html', {'form': form})

# Редактирование (только учитель или админ)
@login_required
def award_update(request, pk):
    award = get_object_or_404(Award, pk=pk)
    if not request.user.is_admin and award.teacher != request.user:
        messages.error(request, "У вас нет доступа для редактирования этого достижения.")
        return redirect('awards:award_list')

    form = AwardForm(request.POST or None, request.FILES or None, instance=award)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Достижение обновлено!")
        return redirect('awards:award_list')
    return render(request, 'awards/award_form.html', {'form': form})

# Удаление (только админ)
@login_required
@admin_required
def award_delete(request, pk):
    award = get_object_or_404(Award, pk=pk)
    if request.method == 'POST':
        award.delete()
        messages.success(request, "Достижение удалено!")
        return redirect('awards:award_list')
    return render(request, 'awards/award_confirm_delete.html', {'award': award})
