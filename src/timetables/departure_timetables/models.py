from django.db import models


# Create your models here.

class Level(models.Model):
    level_id = models.CharField(max_length=20, primary_key=True, unique=True)
    level_index = models.FloatField()
    level_name = models.CharField(max_length=255)

class Stop(models.Model):
    # https://developers.google.com/transit/gtfs/reference/#stopstxt
    stop_id = models.CharField(max_length=20, primary_key=True, unique=True)
    stop_code = models.CharField(max_length=20)
    stop_name = models.CharField(max_length=255)
    stop_desc = models.TextField()
    stop_lat = models.IntegerField()
    stop_lon = models.IntegerField()
    zone_id = models.CharField(max_length=20)
    stop_url = models.URLField()
    parent_station = models.ForeignKey("self", on_delete=models.CASCADE)
    # not sure about this one, not used here, but it's in the specs
    stop_timezone = models.CharField(max_length=50)
    wheelchair_boading = models.IntegerField()
    level_id = models.ForeignKey(Level, on_delete=models.CASCADE)
    platform_code = models.CharField(max_length=50)


