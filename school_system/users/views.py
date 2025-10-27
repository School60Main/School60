from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model
from .forms import UserRegisterForm, UserLoginForm
from users.utils import teacher_required, admin_required
from awards.models import Award
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib import messages
User = get_user_model()
from users.models import CustomUser
from announcements.models import Announcement
# ----------------------------
# Регистрация пользователя
# ----------------------------
def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Пользователь успешно зарегистрирован. Роли назначает администратор.')
            return redirect('users:login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


# ----------------------------
# Кастомный LoginView
# ----------------------------
class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    authentication_form = UserLoginForm

    def form_valid(self, form):
        """Автоматический вход после успешной авторизации"""
        login(self.request, form.get_user())
        return super().form_valid(form)

    def get_success_url(self):
        """Редирект на dashboard после входа"""
        return '/dashboard/'


# ----------------------------
# Dashboard
# ----------------------------
@login_required
def dashboard(request):
    announcements = Announcement.objects.filter(is_active=True).order_by('-created_at')[:5]  # последние 5
    context = {
        'announcements': announcements,
    }

    # Проверка ролей
    if hasattr(request.user, 'is_admin') and request.user.is_admin:
        return render(request, 'dashboard/admin_dashboard.html', context)
    elif hasattr(request.user, 'is_teacher') and request.user.is_teacher:
        return render(request, 'dashboard/teacher_dashboard.html', context)
    else:
        return render(request, 'dashboard/guest_dashboard.html', context)


# ----------------------------
# Logout
# ----------------------------
@login_required
def logout_view(request):
    logout(request)
    return redirect('users:login')

@login_required
def user_list(request):
    if not request.user.is_staff:
        messages.error(request, "У вас нет прав для просмотра пользователей.")
        return redirect('home')  # Перенаправление на главную страницу или страницу ошибки

    # Получаем всех пользователей
    users = CustomUser.objects.all()

    return render(request, 'users/user_list.html', {
        'users': users
    })

@login_required
def assign_role(request, user_id):
    if not request.user.is_staff:
        messages.error(request, "У вас нет прав для назначения ролей.")
        return redirect('home')

    user = get_object_or_404(CustomUser, id=user_id)

    if request.method == 'POST':
        # Получаем значения для ролей
        is_teacher = 'is_teacher' in request.POST
        is_admin = 'is_admin' in request.POST

        # Обновляем роли пользователя
        user.is_teacher = is_teacher
        user.is_admin = is_admin
        user.save()

        messages.success(request, f"Роли для пользователя {user.username} успешно обновлены.")
        return redirect('users:user_list')

    return render(request, 'users/assign_role.html', {
        'user': user
    })
