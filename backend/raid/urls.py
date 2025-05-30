from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RoleViewSet, JobViewSet, PlayerViewSet, RaidGroupViewSet,
    ItemViewSet, GearSetViewSet, GearPieceViewSet,
    LootHistoryViewSet, RaidEventViewSet
)

router = DefaultRouter()
router.register(r'roles', RoleViewSet)
router.register(r'jobs', JobViewSet)
router.register(r'players', PlayerViewSet)
router.register(r'groups', RaidGroupViewSet)
router.register(r'items', ItemViewSet)
router.register(r'gearsets', GearSetViewSet)
router.register(r'gearpieces', GearPieceViewSet)
router.register(r'loothistory', LootHistoryViewSet)
router.register(r'raidevents', RaidEventViewSet)

urlpatterns = [
    path('', include(router.urls)),
]