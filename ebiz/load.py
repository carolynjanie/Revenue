import os
from django.contrib.gis.utils import LayerMapping
from ebiz.models import Parcels, Footprints,parking
parcels_mapping = {
    'objectid_1': 'OBJECTID_1',
    'parcel_id': 'PARCEL_ID',
    'parcelid': 'PARCELID',
    'status': 'STATUS',
    'zone_no': 'ZONE_NO',
    'plot_no': 'PLOT_NO',
    'ref_plot_n': 'Ref_Plot_N',
    'sq_km': 'sq_km',
    'area': 'area',
    'shape_leng': 'Shape_Leng',
    'shape_le_1': 'Shape_Le_1',
    'shape_area': 'Shape_Area',
    'geom': 'MULTIPOLYGON',
}

parking_mapping = {
    'pid': 'pid',
    'amount_pai': 'amount_pai',
    'geom': 'MULTIPOLYGON',
}



footprints_mapping = {
    'id': 'id',
    'osm_id': 'osm_id',
    'name': 'name',
    'plot_no': 'plot_no',
    'height': 'height',
    'category': 'category',
    'fid': 'fid',
    'geom': 'MULTIPOLYGON',
}



parcels_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data','Parcels.shp'),)

def run(verbose=True):
	lm = LayerMapping(Parcels,parcels_shp,parcels_mapping,transform=True,encoding='iso-8859-1')
	lm.save(strict=True,verbose=verbose)
Footprints_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data','Footprints.shp'),)
def run1(verbose=True):
	lm = LayerMapping(Footprints,Footprints_shp,footprints_mapping,transform=True,encoding='iso-8859-1')
	lm.save(strict=True,verbose=verbose)

parking_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data','parking.shp'),)
def run4(verbose=True):
	lm = LayerMapping(parking,parking_shp,parking_mapping,transform=True,encoding='iso-8859-1')
	lm.save(strict=True,verbose=verbose)