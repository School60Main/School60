from django.contrib.auth.decorators import user_passes_test

def teacher_required(function):
    return user_passes_test(lambda u: u.is_teacher)(function)

def admin_required(function):
    return user_passes_test(lambda u: u.is_admin)(function)
