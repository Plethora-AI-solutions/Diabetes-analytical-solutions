

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("Pdai.urls")),
    path("patients/", include("Pdai.urls")),
    path("verification/", include("verify_email.urls")),
]

