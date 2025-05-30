from django.contrib import admin
from .models import Role, Job, RaidGroup, Player, RaidEvent, Item, GearSet, GearPiece, LootHistory

admin.site.register(Role)
admin.site.register(Job)
admin.site.register(RaidGroup)
admin.site.register(Player)
admin.site.register(RaidEvent)
admin.site.register(Item)
admin.site.register(GearSet)
admin.site.register(GearPiece)
admin.site.register(LootHistory)