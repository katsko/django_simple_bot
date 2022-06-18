from django.conf import settings
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import telebot
from .tg import bot


@csrf_exempt
def tg_webhook(request, tg_secret_link):
    if tg_secret_link != settings.TG_SECRET_LINK:
        raise PermissionDenied
    json_data = request.body.decode('utf-8')
    update = telebot.types.Update.de_json(json_data)
    bot.process_new_updates([update])
    return HttpResponse()


@user_passes_test(lambda user:user.is_superuser)
def tg_webhook_url_settings(request):
    host = request.META['HTTP_HOST']
    url = f'https://{host}/tg/{settings.TG_SECRET_LINK}'
    bot.set_webhook(url=url)
    return HttpResponse(url)
