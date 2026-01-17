from django.apps import AppConfig


class AccountappConfig(AppConfig):
    name = 'accountapp'

    def ready(self):
        import accountapp.signals