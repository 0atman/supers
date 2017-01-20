from django.contrib import admin

from .models import (
    Character,
    Skill,
    Contact,
    Stage,
    Team,
    MissionGroup,
    News
)


class CharacterAdmin(admin.ModelAdmin):
    pass

class SkillAdmin(admin.ModelAdmin):
    pass

class ContactAdmin(admin.ModelAdmin):
    pass

class StageAdmin(admin.ModelAdmin):
    pass

class TeamAdmin(admin.ModelAdmin):
    pass

class MissionGroupAdmin(admin.ModelAdmin):
    pass

class NewsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Character, CharacterAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Stage, StageAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(MissionGroup, MissionGroupAdmin)
admin.site.register(News, NewsAdmin)
