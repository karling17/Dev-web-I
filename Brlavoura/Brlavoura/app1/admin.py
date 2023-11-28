from django.contrib import admin
from app1.models import Farm
from app1.models import Harvest
from app1.models import Tillage
from app1.models import Pictures
from app1.models import Humidity
from app1.models import References

# Register your models here.
admin.site.register(Farm)
admin.site.register(Harvest)
admin.site.register(Tillage)
admin.site.register(Pictures)
admin.site.register(Humidity)
admin.site.register(References)