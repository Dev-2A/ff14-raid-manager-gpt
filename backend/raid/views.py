from rest_framework import viewsets
from .models import Role, Job, Player, RaidGroup, Item, GearSet, GearPiece, LootHistory, RaidEvent
from .serializers import (
    RoleSerializer, JobSerializer, PlayerSerializer, RaidGroupSerializer,
    ItemSerializer, GearSetSerializer, GearPieceSerializer,
    LootHistorySerializer, RaidEventSerializer
)

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class RaidGroupViewSet(viewsets.ModelViewSet):
    queryset = RaidGroup.objects.all()
    serializer_class = RaidGroupSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class GearSetViewSet(viewsets.ModelViewSet):
    queryset = GearSet.objects.all()
    serializer_class = GearSetSerializer

class GearPieceViewSet(viewsets.ModelViewSet):
    queryset = GearPiece.objects.all()
    serializer_class = GearPieceSerializer

class LootHistoryViewSet(viewsets.ModelViewSet):
    queryset = LootHistory.objects.all()
    serializer_class = LootHistorySerializer

class RaidEventViewSet(viewsets.ModelViewSet):
    queryset = RaidEvent.objects.all()
    serializer_class = RaidEventSerializer