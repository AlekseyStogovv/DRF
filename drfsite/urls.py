from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from women.views import *

router = routers.SimpleRouter()
router.register(r'women', WomenViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),

]
