from django.apps import AppConfig



class TiendaenlineaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Aplicaciones.tiendaEnLinea'

    def ready(self):
        import Aplicaciones.tiendaEnLinea.signals