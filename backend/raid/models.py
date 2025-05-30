from django.db import models
from django.contrib.auth.models import User

# 1. 역할군(Role): ENUM + 모델(부가정보/확장)
class Role(models.Model):
    ROLE_TYPE = [
        ('tank', '탱커'),
        ('healer', '힐러'),
        ('melee', '근딜'),
        ('ranged', '원딜'),
        ('caster', '마딜'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_TYPE, unique=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


# 2. 직업(Job): 모델만, choices 없이 (신규 추가/변경 가능)
class Job(models.Model):
    code = models.CharField(max_length=20, unique=True)      # 예: PLD, RPR 등
    name = models.CharField(max_length=30)                   # 예: 나이트, 리퍼
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="jobs")
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

# 3. 공대(레이드 그룹)
class RaidGroup(models.Model):
    name = models.CharField(max_length=100)
    raid_name = models.CharField(max_length=100)
    item_level = models.IntegerField()
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='managed_groups')

    def __str__(self):
        return f"{self.raid_name} - {self.name}"

# 4. 플레이어
class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    group = models.ForeignKey(RaidGroup, on_delete=models.CASCADE, related_name='players')
    is_manager = models.BooleanField(default=False)

    def __str__(self):
        return self.nickname

# 5. 레이드 일정
class RaidEvent(models.Model):
    group = models.ForeignKey(RaidGroup, on_delete=models.CASCADE, related_name='events')
    event_date = models.DateField()
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.group.name} - {self.event_date}"

# 6. 장비(아이템) - choices (변하지 않는 ENUM 값들)
class Item(models.Model):
    PART_CHOICES = [
        ('weapon', '무기'),
        ('head', '머리'),
        ('body', '상의'),
        ('hands', '장갑'),
        ('legs', '하의'),
        ('feet', '신발'),
        ('earring', '귀걸이'),
        ('necklace', '목걸이'),
        ('bracelet', '팔찌'),
        ('ring', '반지'),
        ('reinforce', '보강재'),
    ]
    SOURCE_CHOICES = [
        ('heroic', '영웅 레이드'),
        ('normal', '일반 레이드'),
        ('tome', '석판'),
        ('crafted', '제작'),
        ('other', '기타'),
    ]
    name = models.CharField(max_length=100)
    part = models.CharField(max_length=20, choices=PART_CHOICES)
    source = models.CharField(max_length=20, choices=SOURCE_CHOICES)
    is_reinforced = models.BooleanField(default=False)

    def __str__(self):
        return self.name

# 7. 장비 세트 - set_type은 choices
class GearSet(models.Model):
    SET_TYPE_CHOICES = [
        ('start', '출발'),
        ('final', '최종'),
        ('current', '현재'),
    ]
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='gearsets')
    set_type = models.CharField(max_length=10, choices=SET_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.player.nickname} - {self.get_set_type_display()}"

# 8. 세트 내 부위별 장비 정보
class GearPiece(models.Model):
    gearset = models.ForeignKey(GearSet, on_delete=models.CASCADE, related_name='pieces')
    part = models.CharField(max_length=20, choices=Item.PART_CHOICES)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.gearset} - {self.part}"

# 9. 아이템 획득 이력
class LootHistory(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    acquired_at = models.DateField()
    source = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.player.nickname} - {self.item.name} ({self.acquired_at})"