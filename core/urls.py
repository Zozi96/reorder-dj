from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from apps.movies.views import MovieListView, save_ordering
from core.settings import DEBUG

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MovieListView.as_view(), name='list'),
    path('order/', save_ordering, name='save'),
]

if DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)