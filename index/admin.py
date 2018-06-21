from django.contrib import admin
from django.db import models
from .models import *

class AbilitiesAdmin(admin.ModelAdmin):
    list_display = ('description','skill_level','category')
class EducationAdmin(admin.ModelAdmin):
    list_display = ('school', 'degree', 'dates')
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('company', 'title', 'dates', 'display')
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'email')

admin.site.register(Abilities, AbilitiesAdmin)    
admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Profile, ProfileAdmin)