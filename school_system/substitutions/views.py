from collections import defaultdict
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import IntegerField
from django.db.models.functions import Cast
import pandas as pd
from users.utils import admin_required
from .models import Substitution

@login_required
def substitution_list(request):
    substitutions = Substitution.objects.annotate(
        lesson_int=Cast('lesson_number', IntegerField())
    ).order_by('date', 'lesson_int')

    # Группировка по дате и заменяемому учителю
    grouped_subs = defaultdict(lambda: defaultdict(list))
    for sub in substitutions:
        grouped_subs[sub.date][sub.replaced_teacher].append(sub)

    # Преобразуем в список кортежей для шаблона
    grouped_list = []
    for date in sorted(grouped_subs.keys()):
        teachers_list = []
        for teacher, subs in grouped_subs[date].items():
            teachers_list.append((teacher, subs))
        grouped_list.append((date, teachers_list))

    return render(request, 'substitutions/substitution_list.html', {
        'grouped_list': grouped_list
    })

@login_required
@admin_required
def upload_substitutions(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']

        try:
            df = pd.read_excel(file)

            expected_columns = [
                "Дата", 
                "ФИО учителя которого замещают",
                "Номер урока",
                "Класс",
                "ФИО учителя который замещает",
                "Предмет",
                "Кабинет",
            ]

            for col in expected_columns:
                if col not in df.columns:
                    messages.error(request, f"Отсутствует колонка: {col}")
                    return redirect('substitutions:upload_substitutions')

            # Удаляем старые записи
            Substitution.objects.all().delete()

            # Создаем новые
            for _, row in df.iterrows():
                Substitution.objects.create(
                    date=row["Дата"],
                    replaced_teacher=row["ФИО учителя которого замещают"],
                    lesson_number=str(row["Номер урока"]),
                    class_name=row["Класс"],
                    substitute_teacher=row["ФИО учителя который замещает"],
                    subject=row["Предмет"],
                    classroom=row["Кабинет"],
                )

            messages.success(request, "Замены успешно обновлены!")
            return redirect('substitutions:substitution_list')

        except Exception as e:
            messages.error(request, f"Ошибка при загрузке: {e}")

    return render(request, 'substitutions/upload.html')
