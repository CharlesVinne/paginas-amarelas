from django.contrib import admin
from django.urls import path, include
from lista_telefonica.views import ContatoViewSet, AnuncioViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'contatos', ContatoViewSet)
router.register(r'anuncios', AnuncioViewSet)
urlpatterns = [
    path(r'', include(router.urls)),
    path('admin/', admin.site.urls),
]
