from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),  # 🌍 URL para cambiar idioma
]

# Rutas que se traducirán automáticamente
urlpatterns += i18n_patterns(
    path("", include("web.urls")),
    path("admin/", admin.site.urls),
)
