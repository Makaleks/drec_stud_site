# coding: utf-8
from django.conf import settings
from .utils import util_get_new_question_num

def custom_context(request):
    return {
        'notification': {
            'enabled': False,
            'text': 'Разработчик забыл установить текст :)',
            # Bootstrap-like colors
            # Possible: info (light blue), danger (red), dark (black),
            #           primary (blue), secondary (gray), success (green),
            #           warning (red-yellow), light (white)
            'type': 'light',
        },
        'pay_yandex': {
            'payment_text': settings.PAYMENT_TEXT_YANDEX,
            'enable_card': settings.PAYMENT_YANDEX_ENABLE_CARD,
            'enable_phone': settings.PAYMENT_YANDEX_ENABLE_PHONE,
            'success_redirect_url': settings.PAYMENT_SUCCESS_REDIRECT_YANDEX,
            'account': settings.PAYMENT_ACCOUNT_YANDEX,
        },
        'social': {
            'vk': {
                'key': settings.SOCIAL_AUTH_VK_OAUTH2_KEY,
            }
        },
        'is_emergency_login_mode': settings.IS_EMERGENCY_LOGIN_MODE,
        'is_agressive_question_notification': settings.IS_AGRESSIVE_QUESTION_NOTIFICATION,
        'util_get_new_question_num': util_get_new_question_num(),
        'webmaster_tags': {
            'yandex': settings.WEBMASTER_TAG_YANDEX,
            'google': settings.WEBMASTER_TAG_GOOGLE,
        },
    }
