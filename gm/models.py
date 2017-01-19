"""Game models."""
# flake8: noqa: E203,D211
from django.db.models import (
    Model,
    IntegerField,
    ForeignKey,
    CharField,
    ManyToManyField,
    TextField,
    NullBooleanField,
    DateTimeField,
)


class BaseModel(Model):
    """Shared attributes."""
    name = CharField(max_length=200)

    def __str__(self):
        return self.name


class Skill(BaseModel):
    """Players' skills."""
    pass


class Contact(BaseModel):
    pass


class Stage(BaseModel):
    description = TextField()
    on_success = ForeignKey("Stage", related_name="stage_on_success", blank=True, null=True)
    on_failure = ForeignKey("Stage", related_name="stage_on_failure", blank=True, null=True)
    code = CharField(max_length=200)
    uid = CharField(max_length=200)
    glory_on_success = IntegerField()
    glory_on_failure = IntegerField()
    showdown = NullBooleanField(blank=True, null=True)
    start_time = DateTimeField(null=True, blank=True)
    end_time = DateTimeField(null=True, blank=True)
    contact = ManyToManyField(Contact)
    news_on_success = ManyToManyField("News", related_name="news_on_success")
    news_on_failure = ManyToManyField("News", related_name="news_on_failure")
    cooldown_on_success = IntegerField()
    cooldown_on_failure = IntegerField()
    skills_needed = ManyToManyField(Skill)


class Character(BaseModel):
    """Characters."""
    glory = IntegerField(default=0)
    skills = ManyToManyField(Skill)
    contacts = ManyToManyField(Contact)
    cooldown = DateTimeField(blank=True, null=True)


class Team(BaseModel):
    lead = ForeignKey(Character)
    members = ManyToManyField(Character, related_name="team_members")
    glory = IntegerField(default=0)


class MissionGroup(BaseModel):
    members = ManyToManyField(Character)
    the_stage = ForeignKey(Stage, related_name="mission_group")


class News(BaseModel):
    contacts = ForeignKey(Contact)
    trigger_time = DateTimeField(blank=True, null=True)
