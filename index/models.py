from django.db import models

class Profile(models.Model):
    name =models.CharField(max_length=256)
    subtitle = models.CharField(max_length=256)
    description = models.TextField()
    location = models.CharField(max_length=256)
    email = models.EmailField()
    linkedin = models.URLField()

class Education(models.Model):
    school = models.CharField(max_length=256)
    start_date = models.DateField()
    end_date = models.DateField()
    degree = models.CharField(max_length=256)
    description = models.TextField()
    location = models.CharField(max_length=256)

class Experience(models.Model):
    company = models.CharField(max_length=256)
    start_date = models.DateField()
    end_date = models.DateField()
    title = models.CharField(max_length=256)
    description = models.TextField()
    location = models.CharField(max_length=256)
    
# class Projects(models.Model):
#     image = models.ImageField()
#     title = models.CharField(max_length=256)
#     description = models.TextField()
    
class Abilities(models.Model):
    ABILITIES_CATEGORIES = (('skills','Skills'),('tools','Tools'))
    category = models.CharField(max_length=1, choices=ABILITIES_CATEGORIES)
    skill_level = models.IntegerField()