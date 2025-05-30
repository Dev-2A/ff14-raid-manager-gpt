from rest_framework import serializers
from .models import Role, Job, Player, RaidGroup, Item, GearSet, GearPiece, LootHistory, RaidEvent

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
    role = RoleSerializer(read_only=True)
    role_id = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all(), write_only=True, source='role')
    
    class Meta:
        model = Job
        fields = ['id', 'code', 'name', 'role', 'role_id', 'description']

class RaidGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = RaidGroup
        fields = '__all__'

class PlayerSerializer(serializers.ModelSerializer):
    job = JobSerializer(read_only=True)
    job_id = serializers.PrimaryKeyRelatedField(queryset=Job.objects.all(), write_only=True, source='job')
    group = RaidGroupSerializer(read_only=True)
    group_id = serializers.PrimaryKeyRelatedField(queryset=RaidGroup.objects.all(), write_only=True, source='group')
    
    class Meta:
        model = Player
        fields = ['id', 'nickname', 'job', 'job_id', 'group', 'group_id', 'is_manager']

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class GearSetSerializer(serializers.ModelSerializer):
    player = PlayerSerializer(read_only=True)
    player_id = serializers.PrimaryKeyRelatedField(queryset=Player.objects.all(), write_only=True, source='player')
    
    class Meta:
        model = GearSet
        fields = ['id', 'player', 'plyaer_id', 'set_type', 'created_at']

class GearPieceSerializer(serializers.ModelSerializer):
    gearset = GearSetSerializer(read_only=True)
    gearset_id = serializers.PrimaryKeyRelatedField(queryset=GearSet.objects.all(), write_only=True, source='gearset')
    item = ItemSerializer(read_only=True)
    item_id = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all(), write_only=True, source='item')
    
    class Meta:
        model = GearPiece
        fields = ['id', 'gearset', 'gearset_id', 'part', 'item', 'item_id']

class LootHistorySerializer(serializers.ModelSerializer):
    player = PlayerSerializer(read_only=True)
    player_id = serializers.PrimaryKeyRelatedField(queryset=Player.objects.all(), write_only=True, source='player')
    item = ItemSerializer(read_only=True)
    item_id = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all(), write_only=True, source='item')
    
    class Meta:
        model = LootHistory
        fields = ['id', 'player', 'player_id', 'item', 'item_id', 'acquired_at', 'source']

class RaidEventSerializer(serializers.ModelSerializer):
    group = RaidGroupSerializer(read_only=True)
    group_id = serializers.PrimaryKeyRelatedField(queryset=RaidGroup.objects.all(), write_only=True, source='group')
    
    class Meta:
        model = RaidEvent
        fields = ['id', 'group', 'group_id', 'event_date', 'description']