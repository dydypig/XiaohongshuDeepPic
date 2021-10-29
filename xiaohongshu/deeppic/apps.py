from django.apps import AppConfig


class DeeppicConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'deeppic'

    def ready(self):
        import deeppic.signals