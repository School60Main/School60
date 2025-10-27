from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),      # страницы логина/дашборд
    path('awards/', include('awards.urls')),
    path('incentives/', include('incentives.urls')),
    path('events/', include('events.urls')),
    path('stats/', include('stats.urls')),
    path('substitutions/', include('substitutions.urls')),
    path('announcements/', include('announcements.urls', namespace='announcements')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)