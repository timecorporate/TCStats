from rest_framework.routers import DefaultRouter
from stats.views import UserViewSet, \
    GroupViewSet, ChannelsViewSet

# from django.contrib import admin
router = DefaultRouter()
router.register("user", UserViewSet)
router.register("group", GroupViewSet)
router.register('channel', ChannelsViewSet)

urlpatterns = router.urls
