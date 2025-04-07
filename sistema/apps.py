from django.apps import AppConfig


class SistemaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sistema'

class ApresentacaoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apresentacao'