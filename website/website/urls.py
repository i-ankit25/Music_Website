from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from music import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('music', include('music.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
]

if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

