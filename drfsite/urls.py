from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from women.views import *


class MyCustomRouter(routers.SimpleRouter):
    routers = [
        routers.Route(url=r'^{prefix}$',
                      mapping={'get': 'list'},
                      name='{basename}-list',
                      detail=False,
                      initkwargs={'suffix': 'list'}),
        routers.Route(url=r'^{prefix}/{lookup}$',
                      mapping={'get': 'retrieve'},
                      name='{basename}-detail',
                      detail=True,
                      initkwargs={'suffix': 'Detail'}),
    ]

router = MyCustomRouter()
router.register(r'women', WomenViewSet, basename='women')
print(router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),

]
