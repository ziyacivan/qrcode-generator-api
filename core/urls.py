from django.contrib import admin
from django.urls import path

from users.views import LoginView, RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/register/', RegisterView.as_view()),
    path('api/v1/login/', LoginView.as_view()),
]
