from django.contrib import admin
from django import forms
from django.contrib import messages
from django.core.exceptions import ValidationError

from .models import (
    Character,
    Skill,
    Contact,
    Stage,
    Team,
    News,
    Mission,
)


class CharacterAdmin(admin.ModelAdmin):
    pass


class StageInline(admin.StackedInline):
    model = Stage
    extra = 0


class MissionAdminForm(forms.ModelForm):

    def clean(self):
        # raise ValidationError("SKILL VALIDATION ERROR")
        stage_skills_needed_keys = [
            k for k
            in self.data.copy().keys()
            if "skills_needed" in k
        ]

        stage_current_chars_keys = [
            k for k
            in self.data.copy().keys()
            if "current_characters" in k
        ]

        for stage_id, _ in enumerate(stage_current_chars_keys):
            # stage 0
            skills_needed_ids = self.data.copy().pop(
                    'stages-%s-skills_needed' % stage_id,
                    []
            )
            character_ids = self.data.copy().pop(
                    'stages-%s-current_characters' % stage_id,
                    []
            )
            characters = Character.objects.filter(
                id__in=character_ids
            )
            stage_skills = Skill.objects.filter(
                id__in=skills_needed_ids
            )
            stage_skills = set([s.name for s in stage_skills])

            if characters:
                group_skills = set()
                for character in characters:
                    group_skills.update(
                        [s.name for s in character.skills.all()]
                    )
                if stage_skills.issubset(group_skills):
                    pass
                else:
                    raise ValidationError("SKILL VALIDATION ERROR")


class MissionAdmin(admin.ModelAdmin):
    inlines = [
        StageInline,
    ]
    form = MissionAdminForm


class SkillAdmin(admin.ModelAdmin):
    pass


class ContactAdmin(admin.ModelAdmin):
    pass


def make_published(modeladmin, request, queryset):
    # queryset.update(status='p')
    for stage in queryset:
        if not stage.current_characters.all():
            messages.error(request, 'NO CHARACTERS IN STAGE.')
            return
        team_size = len(stage.current_characters.all())
        glory_each = int(stage.glory_on_success / team_size)
        for character in stage.current_characters.all():
            character.glory = character.glory + glory_each
            if character.team_members.all():
                team = character.team_members.all()[0]
                team.glory = team.glory + glory_each
                team.save()
            character.save()
        stage.current_characters.clear()
        messages.success(request, 'Stage "%s" completed, glory allocated.' % stage.name)
        # TODO: Add cooldown to chars here

make_published.short_description = "Complete stage"


class StageAdmin(admin.ModelAdmin):
    actions = [make_published]


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
admin.site.register(News, NewsAdmin)
admin.site.register(Mission, MissionAdmin)
