from django.urls import path, include
from app_accounts import views


app_name = "app_accounts"

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.register_account, name='register'),
]
