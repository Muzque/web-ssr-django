from django.apps import AppConfig
from django.conf import settings
from django.contrib.auth.management.commands import createsuperuser
from django.db.models import signals
from configparser import ConfigParser


class BasicConfig(AppConfig):
    name = __package__

    def ready(self):
        if not settings.DEBUG:
            return

        from django.contrib.auth import models as auth_models

        def create_testuser(**kwargs):
            User = auth_models.User
            manager = User.objects
            cfg = ConfigParser()
            cfg.read('private/envs.cfg')
            USERNAME = cfg.get('Model', 'SUPERUSER_ROOT')
            EMAIL = cfg.get('Model', 'SUPERUSER_EMAIL')
            PASSWORD = cfg.get('Model', 'SUPERUSER_PASSWORD')
            try:
                manager.get(username=USERNAME)
            except User.DoesNotExist:
                manager.create_superuser(USERNAME, EMAIL, PASSWORD)

        # Prevent interactive question about wanting a superuser created
        signals.post_migrate.disconnect(createsuperuser, sender=auth_models,
                                        dispatch_uid='django.contrib.auth.management.create_superuser')
        signals.post_migrate.connect(create_testuser, sender=auth_models,
                                     dispatch_uid='common.models.create_testuser')
