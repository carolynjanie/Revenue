from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from ebiz import models as e_models
# from .models import Footprint,Parcels,Personal

# Register your models here.
class FootprintsAdmin(LeafletGeoAdmin):
	list_display=['geom','plot_no','name','fid']
    
class ParcelsAdmin(LeafletGeoAdmin):
	list_display = ['geom','plot_no','area']

class FloorsAdmin(LeafletGeoAdmin):
	list_display=['floor_name','floor_no','footprint']

class RoomAdmin(LeafletGeoAdmin):
	list_display=['room_no','room_area','floor']
class Personal_InfoAdmin(LeafletGeoAdmin):
	list_display=['footprints','name','phone_no']
class Business_InfoAdmin(LeafletGeoAdmin):
	list_display=['business_sector','business_activity','permit_expected','paid_permit','paid_permit','permit_number','timestamp']

class parkingAdmin(LeafletGeoAdmin):
	list_display=['pid','amount_pai','geom']
class BusinessOperatorAdmin(LeafletGeoAdmin):
	list_display=['business','idno','phone','name','timestamp']

admin.site.register(e_models.Contacts,LeafletGeoAdmin)

admin.site.register(e_models.Footprints,FootprintsAdmin)
admin.site.register(e_models.Parcels,ParcelsAdmin)
admin.site.register(e_models.Personal_Info,Personal_InfoAdmin)
admin.site.register(e_models.Rooms,RoomAdmin)
admin.site.register(e_models.Floors,FloorsAdmin)
admin.site.register(e_models.Business_Info,Business_InfoAdmin)
admin.site.register(e_models.parking,parkingAdmin)
admin.site.register(e_models.BusinessOperator,BusinessOperatorAdmin)
