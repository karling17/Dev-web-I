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
    startdate = 
    active = models.BooleanField(default=False)
    enddate =
    health = models.CharField(max_length=100)
    harvestId = models.ForeignKey(Harvest,
                                  null=False,
                                  on_delete=models.CASCADE,
                                  related_name='tillages')




    
    

