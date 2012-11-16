from django.db import models

class Area(models.Model):
    hebrew_name = models.CharField(max_length=200)
    english_name = models.CharField(max_length=200, null=True)
    
    center_long = models.FloatField(null=True)
    center_lat = models.FloatField(null=True)
    


class Attack(models.Model):
    area = models.ForeignKey(Area, null=True)
    when = models.BigIntegerField()
        
    raw_item = models.TextField()