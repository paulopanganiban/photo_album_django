from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'photo_album_project.users'

    def ready(self):
        try:
            import photo_album_project.users.signals  # noqa F401
        except ImportError:
             pass
