from django.apps import AppConfig

class FlickappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'flickapp'

    def ready(self):
        import flickapp.signals  # Make sure this is your actual app name
