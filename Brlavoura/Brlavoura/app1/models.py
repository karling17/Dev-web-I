from django.db import models

# Create your models here.

class Users(models.Model):
    PROFILES = (
    ('farmer', 'Fazendeiro'),
    ('agronomist', 'Agrônomo'),
    ('cooperative', 'Cooperativa'),
    )

    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    profile = models.CharField(max_length=20, choices=PROFILES)

    def __str__(self):
        return self.profile

class Farm(models.Model): 
    name = models.CharField(max_length=100)
    farmerId = models.ForeignKey(Users,
                                  null=False,
                                  on_delete=models.CASCADE, 
                                  related_name='farms',
                                  limit_choices_to={'profile':'farmer'}
                                )
    AgronomistId = models.ForeignKey(Users,
                                  null=False,
                                  on_delete=models.CASCADE,
                                  related_name='Agronomists', 
                                  limit_choices_to={'profile':'agronomist'}
                                )
    cooperativeID = models.ForeignKey(Users,
                                  null=False,
                                  on_delete=models.CASCADE,
                                  related_name='cooperatives', 
                                  limit_choices_to={'profile':'cooperative'}
                                )
    geolocalization = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name
    
class Harvest(models.Model):
    localization = models.CharField(max_length=100)
    farmId = models.ForeignKey(Farm,
                               null=False, 
                               on_delete=models.CASCADE,
                               related_name='harvests',
                               )
    
class Tillage(models.Model):
    SEEDS = (
    ('Thompson_Seedless', 'Uva Thompson Seedless'),
    ('Red_Globe', 'Uva Red Globe'),
    ('Flame_Seedless', 'Uva Flame Seedless'),
    ('Concord', 'Uva Concord'),
    ('Muscat', 'Uva Muscat'),
    ('Cabernet_Sauvignon', 'Uva Cabernet Sauvignon'),
    ('Chardonnay', 'Uva Chardonnay'),
    ('Merlot', 'Uva Merlot'),
    ('Pinot_Noir', 'Uva Pinot Noir'),
    ('Zinfandel', 'Uva Zinfandel'),
    )

    startdate = models.DateField(auto_now=True)
    active = models.BooleanField(default=False)
    enddate = models.DateField()
    health = models.CharField(max_length=100)
    usedseed = models.CharField(max_length=60, choices=SEEDS)
    harvestId = models.ForeignKey(Harvest,
                                  null=False,
                                  on_delete=models.CASCADE,
                                  related_name='tillages')
    
class Pictures(models.Model): 
    timestamp = models.DateTimeField(auto_now=True)
    notes = models.CharField(max_length=400)
    file = models.CharField(max_length=100)
    tillagedId = models.ForeignKey(Tillage,
                                   null=False,
                                  on_delete=models.CASCADE,
                                  related_name='picsoftillage'
                                   )

class Humidity(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    humidity = models.FloatField(max_length=4)
    tillageId = models.ForeignKey(Tillage,
                                  null=False,
                                  on_delete=models.CASCADE,
                                  related_name='tillages'
                                  )
    
class References(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    internalRef = models.FloatField(max_length=4)
    externalRef = models.FloatField(max_length=4)
