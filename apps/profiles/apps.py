from django.apps import AppConfig
#from django.utils import timezone


class ProfilesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.profiles"
    
    
    def ready(self):
        from apps.profiles import signals
    
    
    

