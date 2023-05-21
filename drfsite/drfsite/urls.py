
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from hockey.views import  *

router = routers.SimpleRouter()
router.register(r'player', PlayerViewSet)
router.register(r'hockey', HockeyViewSet)
router.register(r'trener', TrenerViewSet)
router.register(r'staff', StaffViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'post', PostViewSet)
router.register(r'prof', ProfViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
