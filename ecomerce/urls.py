from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.header = "Peleza ecommerce task"
admin.site.title = "Peleza ecommerce task Admin portal"
admin.site.index_title = "Welcome to Peleza e-commerce task Admin portal"
