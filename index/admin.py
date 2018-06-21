from django.contrib import admin
from django.db import models
from .models import *

# Register your models here.
#myModels = [models.Profile, models.Education, models.Experience, models.Abilities]
myModels = [Profile, Education, Experience, Abilities]
admin.site.register(myModels)