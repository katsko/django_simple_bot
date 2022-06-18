from django.contrib import admin
from django.urls import path
from base.views import tg_webhook, tg_webhook_url_settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tg/settings', tg_webhook_url_settings),
    path('tg/<str:tg_secret_link>', tg_webhook),
]
