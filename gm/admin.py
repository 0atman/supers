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

[admin.site.register(model)
 for model in locals().values()
 if hasattr(model, "pk")]
