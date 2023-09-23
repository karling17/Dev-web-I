from django.db import models

# Create your models here.
class Farm(models.Model): 
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=100)
    farmerId = models.ForeignKey(null=True)
    AgronomistId = models.ForeignKey(null=True)
    cooperativeID = models.ForeignKey(null=True)
    geolocalization = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name
