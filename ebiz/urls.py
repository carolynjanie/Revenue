from django.urls import path, include
from djgeojson.views import GeoJSONLayerView
from ebiz.models import Footprints,Parcels,parking
from . import views

app_name='ebiz'


urlpatterns = [
    # path('contact/',views.ContactView,name='contact'),
    path('',views.home,name='home'),
    path('home/',views.Homepage.as_view(), name='index'),
    path('parcels/',views.parcel,name='parcels'),
    path('parks/',views.parkingview,name='parks'),
    path('parcel-data/',GeoJSONLayerView.as_view(model=Parcels),name='parcel-data'),
    path('footprint-data/',GeoJSONLayerView.as_view(model=Footprints),name='ftp-data'),
    path('parking-data/',GeoJSONLayerView.as_view(model=parking),name='parkn-data'),
    path('footprint/<int:ftid>/',views.FootprintInfoEncoder.as_view(),name='footprint'),
    path('floor/<int:ftid>/',views.FloorInfoEncoder.as_view(),name='floor'),
    path('floor/<int:ftid>/<int:stair>/',views.StairsInfoEncoder.as_view(),name='stairs'),
]