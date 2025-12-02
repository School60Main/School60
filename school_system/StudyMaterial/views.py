from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import StudyMaterial
from .forms import StudyMaterialForm

@login_required
def material_list(request):
    materials = StudyMaterial.objects.all()

    # Фильтры
    subject_filter = request.GET.get('subject')
    teacher_filter = request.GET.get('teacher')
    search_query = request.GET.get('q')

    if subject_filter:
        materials = materials.filter(subject=subject_filter)
    if teacher_filter:
        materials = materials.filter(uploaded_by__id=teacher_filter)
    if search_query:
        materials = materials.filter(title__icontains=search_query)

    teachers = StudyMaterial.objects.values_list('uploaded_by__id', 'uploaded_by__first_name', 'uploaded_by__last_name').distinct()
    
    context = {
        'materials': materials,
        'teachers': teachers,
        'subject_filter': subject_filter,
        'teacher_filter': teacher_filter,
        'search_query': search_query,
    }
    return render(request, 'materials/material_list.html', context)

@login_required
def material_upload(request):
    if not request.user.is_teacher:
        return redirect('dashboard')

    if request.method == 'POST':
        form = StudyMaterialForm(request.POST, request.FILES)
        if form.is_valid():
            material = form.save(commit=False)
            material.uploaded_by = request.user
            material.save()
            return redirect('materials:material_list')
    else:
        form = StudyMaterialForm()

    return render(request, 'materials/material_upload.html', {'form': form})

@login_required
def material_detail(request, pk):
    material = get_object_or_404(StudyMaterial, pk=pk)
    return render(request, 'materials/material_detail.html', {'material': material})
