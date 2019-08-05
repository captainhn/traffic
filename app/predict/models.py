from django.db import models


# Create your models here.
class TrafficData(models.Model):
    time = models.TimeField()
    flow = models.IntegerField(default=0)
    class Meta():
        db_table = 'traffic_data'
    traffic = models.Manager()

