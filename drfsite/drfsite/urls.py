
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from hockey.views import  *

router = routers.SimpleRouter()
router.register(r'staff', StaffViewSet)
router.register(r'prof', ProfViewSet)
router.register(r'player', PlayerViewSet)
router.register(r'hockey', HockeyViewSet)
router.register(r'trener', TrenerViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'post', PostViewSet)
router.register(r'posts', PostsViewSet)
router.register(r'guide', GuideViewSet)
router.register(r'articles', ArticlesViewSet)
router.register(r'pressservice', PressServiceViewSet)
router.register(r'profpress', ProfPressViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
