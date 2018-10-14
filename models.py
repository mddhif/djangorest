from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.conf  import settings



class Flights(models.Model):
    Id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    month = models.IntegerField(db_column='Month', blank=True, null=True)  # Field name made lowercase.
    day = models.IntegerField(db_column='Day', blank=True, null=True)  # Field name made lowercase.
    deptime = models.IntegerField(db_column='DepTime', blank=True, null=True)  # Field name made lowercase.
    arrtime = models.IntegerField(db_column='ArrTime', blank=True, null=True)  # Field name made lowercase.
    uniquecarrier = models.CharField(db_column='UniqueCarrier', max_length=2, blank=True, null=True)  # Field name made lowercase.
    flightnum = models.IntegerField(db_column='FlightNum', blank=True, null=True)  # Field name made lowercase.
    tailnum = models.CharField(db_column='TailNum', max_length=7, blank=True, null=True)  # Field name made lowercase.
    actualelapsedtime = models.IntegerField(db_column='ActualElapsedTime', blank=True, null=True)  # Field name made lowercase.
    airtime = models.IntegerField(db_column='AirTime', blank=True, null=True)  # Field name made lowercase.
    origin = models.CharField(db_column='Origin', max_length=4, blank=True, null=True)  # Field name made lowercase.
    dest = models.CharField(db_column='Dest', max_length=4, blank=True, null=True)  # Field name made lowercase.
    distance = models.IntegerField(db_column='Distance', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Flights'


    def __str__(self):
        return self.origin