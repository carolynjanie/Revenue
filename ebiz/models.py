from django.db import models
from django.contrib.gis.db import models
import datetime
from datetime import datetime



class Footprints(models.Model):
    id = models.BigIntegerField(primary_key=True)
    osm_id = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    plot_no = models.FloatField()
    height = models.FloatField()
    category = models.CharField(max_length=254)
    fid = models.CharField(max_length=254)
    geom = models.MultiPolygonField(srid=4326)
    def __str__(self):
        return '%s' %(self.name)

class Parcels(models.Model):
    objectid_1 = models.IntegerField()
    parcel_id = models.IntegerField()
    parcelid = models.IntegerField()
    status = models.CharField(max_length=22)
    zone_no = models.CharField(max_length=50)
    plot_no = models.CharField(max_length=50)
    ref_plot_n = models.CharField(max_length=50)
    sq_km = models.FloatField()
    area = models.FloatField()
    shape_leng = models.FloatField()
    shape_le_1 = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return '%s' %(self.plot_no)

class Personal_Info(models.Model):
    footprints= models.ForeignKey('Footprints', models.CASCADE, db_column='footprints')
    name=models.CharField(max_length=54)
    phone_no=models.CharField(max_length=10)
    


class parking(models.Model):
    pid = models.FloatField()
    amount_pai = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

    class Meta:
        verbose_name_plural = "Parking"

class Floors(models.Model):
    footprint=models.ForeignKey('Footprints', models.CASCADE, db_column='footprint')
    floor_no=models.BigIntegerField()
    floor_name=models.CharField(max_length=254)
    def __str__(self):
        return '%d -> %s : %s' %(self.footprint.id,self.floor_no,self.floor_name)
   
class Rooms(models.Model):
    floor=models.ForeignKey('Floors', models.CASCADE, db_column='floor')
    room_no=models.CharField(max_length=10)
    room_area=models.FloatField()
    def __str__(self):
        return '%s' %(self.room_no)

class Business_Info(models.Model):
    business_sector=models.CharField(max_length=254)
    business_activity=models.CharField(max_length=254)
    room=models.ForeignKey('Rooms', models.CASCADE, db_column='room')
    permit_number=models.CharField(max_length=30)
    paid_permit=models.FloatField()
    permit_expected=models.FloatField()
    # datePaid=DateTimeField()
    # permit_bal=models.CharField(max_length=30)
    timestamp=models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table='business_information'
        ordering=('-timestamp',)
    def  __str__(self):
        return '%s' %(self.business_activity)

class Contacts(models.Model):
    fullname = models.CharField(max_length=200)
    def __str__(self):
        return self.fullname

class BusinessOperator(models.Model):
    business=models.ForeignKey(Business_Info,on_delete=models.CASCADE)
    phone=models.CharField(max_length=14)
    name=models.CharField(max_length=200)
    idno=models.IntegerField()
    timestamp=models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table='business_operators'
        ordering=('-timestamp',)
    def __str__(self):
        return '%s' %(self.name) 

