from .views import RegisterView
# CheckRegisterView

from django.urls import path

urlpatterns = [
    path('register/', RegisterView.as_view()),
    # path('check-registr/', CheckRegisterView.as_view())
]
