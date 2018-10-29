from django.shortcuts import render,redirect
from django.core.serializers import serialize
from django.views.generic import TemplateView
# from collections import OrderedDict
# from fusioncharts import FusionCharts
import datetime
from django.shortcuts import render,get_object_or_404
from django.views import View
from django.http import JsonResponse,HttpResponse
from .models import Parcels,parking,Footprints,Floors,Rooms,Contacts,BusinessOperator,Business_Info
from ebiz import forms as e_forms
from django.core.management import CommandError
import json
from collections import Counter


# Create your views here.

def home(request):
	return render(request,'index1.html')
def about(request):
	return render(request,'about.html')
def footprint(request):
	foot = serialize('geojson',Footprints.objects.all())
	print(foot)
	return HttpResponse(foot, content_type='json' )
def parcel(request):
	parcel= serialize('geojson',Parcels.objects.all() )
	return HttpResponse(parcel, content_type='json' )
def parkingview(request):
	Park = serialize('geojson',parking.objects.all() )
	return HttpResponse(Park, content_type='json' )
def tax(request):
	tax = serialize('geojson',Business_Info.objects.all() )
	return HttpResponse(tax, content_type='json' )
class Homepage(View):
	def get(self,request):
		# business info
		business=Business_Info.objects.all()
		expectpermit=[]
		paidpermit=[]
		paidnot = []

		for b in business:
			expectpermit.append(b.permit_expected)
			paidpermit.append(b.paid_permit)
			npp = float(b.permit_expected)-float(b.paid_permit)
			paidnot.append(npp)
		ep = sum(expectpermit)
		ep = float(ep)
		pm = sum(paidpermit)
		npp = sum(paidnot)
		
		paid = []
		not_paid = []
		parki = parking.objects.all()
		for p in parki:
			# print(p.amount_pai)
			if p.amount_pai>0:
				paid.append(p.amount_pai)
			elif p.amount_pai<=0:
				not_paid.append(p.amount_pai)
			else:
				print('Invalid request')

		pd_count = Counter(paid)
		print(pd_count)
		np_count = Counter(not_paid)
		print(np_count)
		xs = [i for i,_ in enumerate(pd_count)]
		print(xs)
		pd = [pd_count[x]*50 for x in pd_count]
		print(sum(pd))
		np = [np_count[x]*50 for x in np_count]
		# query = request.GET.get('q')
		# if query:
		# 	qs = qs.filter(name__icontains=query)

		return render(request,'index.html',
			{
		
			'pd':pd,
			'np':np,
			'xs':xs,
			'ep':ep,
			'npp':npp,
			'pm':pm
			})
	

class FootprintInfoEncoder(View):
	def get(self,request,ftid):
		ftp=get_object_or_404(Footprints,id=ftid)
		return JsonResponse({'name':ftp.name,'plot_no':ftp.plot_no,'height':ftp.height,'floors':Floors.objects.filter(footprint=ftp).count()})

class FloorInfoEncoder(View):
	def get(self,request,ftid):
		footprint=get_object_or_404(Footprints,id=ftid)
		try:
			floors=Floors.objects.filter(footprint=footprint)
		except:
			raise CommandError('No Floors registered for this footprint. Kindly register and try again')
		else:
			fls=[]
			for floor in floors:
				fls.append({'name':floor.floor_name,'no':floor.floor_no,'rooms':Rooms.objects.filter(floor=floor).count()})
			return JsonResponse({'objs':fls})

class StairsInfoEncoder(View):
	def get(self,request,ftid,stair):
		footprint=get_object_or_404(Footprints,id=ftid)
		try:			
			floor=Floors.objects.filter(footprint=footprint).filter(floor_no=stair)[0]
		except:
			raise CommandError('No Floors registered for this footprint. Kindly register and try again')
		else:
			try:
				rooms=Rooms.objects.filter(floor=floor)
			except:
				raise CommandError('No Rooms registered for this floor. Kindly register and try again')
			else:
				resp=[]
				for room in rooms:
					try:
						biz=Business_Info.objects.filter(room=room)[0]
						owner=BusinessOperator.objects.filter(business=biz)[0]
					except:
						raise CommandError('No Owners registered alonside the room. Kindly do the necessary and try again')
					else:
						resp.append({'sector':biz.business_sector,'activity':biz.business_activity,'pnumber':biz.permit_number,
							'ppaid':biz.paid_permit,'owner':owner.name,'phone':owner.phone,'idno':owner.idno})
		return JsonResponse({'objs':resp})
#