from django.db import models

class Area(models.Model):
    hebrew_name = models.CharField(max_length=200)
    english_name = models.CharField(max_length=200, null=True)
    
    center_long = models.FloatField(null=True)
    center_lat = models.FloatField(null=True)
    


class Attack(models.Model):
    area = models.ForeignKey(Area, null=True)
    when = models.BigIntegerField()
    guid = models.CharField(max_length=300)
    raw_item = models.TextField()
    
    def get_dict(self):
        return {"area_name_english" : self.area.english_name,
                "area_center_long" : self.area.center_long,
                "area_center_lat" : self.area.center_lat,
                "when" : self.when,}

class AreaError(models.Model):
    name = models.CharField(max_length=200)
    solved = models.BooleanField(default=False)