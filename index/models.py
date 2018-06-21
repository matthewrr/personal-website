from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=256)
    subtitle = models.CharField(max_length=256)
    # image = models.ImageField()
    description = models.TextField()
    location = models.CharField(max_length=256)
    email = models.EmailField()
    linkedin = models.URLField()
    
    class Meta:
        verbose_name_plural = "profile"
    
    def __str__(self):
        return self.name

class Education(models.Model):
    school = models.CharField(max_length=256)
    start_date = models.DateField() #fix for month/year
    end_date = models.DateField() #include 'current'
    degree = models.CharField(max_length=256) #dropdown including no degree, certificate, custom
    subject = models.CharField(blank=True, max_length=256)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=256)
    
    class Meta:
        verbose_name_plural = "education"
    
    def dates(self):
        return self.start_date.strftime('%m/%Y') + ' - ' + self.end_date.strftime('%m/%Y')
        
    def __str__(self):
        return self.school

class Experience(models.Model):
    company = models.CharField(max_length=256)
    start_date = models.DateField()
    end_date = models.DateField()
    title = models.CharField(max_length=256)
    description = models.TextField()
    location = models.CharField(max_length=256)
    display = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "experience"
    
    def dates(self):
        return self.start_date.strftime('%m/%Y') + ' - ' + self.end_date.strftime('%m/%Y')

    def __str__(self):
        return self.company
    
# class Projects(models.Model):
#     image = models.ImageField()
#     title = models.CharField(max_length=256)
#     description = models.TextField()
    
class Abilities(models.Model):
    ABILITIES_CATEGORIES = (('skills','Skills'),('tools','Tools'))
    SKILL_LEVELS = ((1,1),(2,2),(3,3),(4,4),(5,5))
    category = models.CharField(max_length=256, choices=ABILITIES_CATEGORIES)
    description = models.CharField(max_length=256)
    skill_level = models.IntegerField(choices=SKILL_LEVELS)
    
    class Meta:
        verbose_name_plural = "abilities"

    def __str__(self):
        return self.description