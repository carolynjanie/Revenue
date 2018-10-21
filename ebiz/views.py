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
	business=Business_Info.objects.all()
	expectpermit=[]
	paidpermit=[]
	paidnot=expectpermit-paidpermit

	for b in business:
			paidpermit.append(b.permit_expected)
			print
			paidnot.append(b.paid_permit)

			bp_count=counter(paidpermit)
			print (sum(bp))
			ep=counter(paidnot)
			print (ep)
			xAxisName = [i for i,_ in enumerate(bp_count)]
			print(xAxisName)
			query = request.GET.get('q')
			if query:
				qs = qs.filter(name__icontains=query)
			return render(request,'index.html',
			{
			'qs':qs,
			'bp':bp,
			'ep':ep,
			'xAxisName':xs
			})

def footprint(request):
	foot = serialize('geojson',Footprints.objects.all() )
	return HttpResponse(foot, content_type='json' )
def parcel(request):
	parcel= serialize('geojson',Parcels.objects.all() )
	return HttpResponse(parcel, content_type='json' )
def parkingview(request):
	Park = serialize('geojson',parking.objects.all() )
	return HttpResponse(Park, content_type='json' )
class Homepage(View):
	def get(self,request):
		qs = Footprints.objects.all()
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
		query = request.GET.get('q')
		if query:
			qs = qs.filter(name__icontains=query)

		return render(request,'index.html',
			{
			'qs':qs,
			'pd':pd,
			'np':np,
			'xs':xs
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
							'ppaid':biz.paid_permit,'pbal':biz.permit_bal,'owner':owner.name,'phone':owner.phone,'idno':owner.idno})
		return JsonResponse({'objs':resp})
# def ContactView(request):
# 	form_class = e_forms.ContactForm
# 	if request.method == 'POST':
# 		form = form_class(data=request.POST)
# 		if form.is_valid():
# 			fullname = request.POST.get('fullname')
# 			newMessage = Contacts.objects.create(fullname=fullname)
# 			newMessage.save()
# 			print('testing')
# 			return HttpResponse('it worked')

# 		else:
# 			form = form_class
# 	return render(request,'index.html',{'form':form_class})

# def myFirstChart(request):

#     #Chart data is passed to the `dataSource` parameter, like a dictionary in the form of key-value pairs.
#     dataSource = OrderedDict()

#     # The `chartConfig` dict contains key-value pairs of data for chart attribute
#     chartConfig = OrderedDict()
#     chartConfig["caption"] = "Countries With Most Oil Reserves [2017-18]"
#     chartConfig["subCaption"] = "In MMbbl = One Million barrels"
#     chartConfig["xAxisName"] = "amount of money paid"
#     chartConfig["yAxisName"] = "yg"
#     chartConfig["numberSuffix"] = "K"
#     chartConfig["theme"] = "fusion"

#     # The `chartData` dict contains key-value pairs of data
#     chartData = OrderedDict()
   

#     dataSource["chart"] = chartConfig
#     dataSource["data"] = []

#     # Convert the data in the `chartData`array into a format that can be consumed by FusionCharts.
#     #The data for the chart should be in an array wherein each element of the array 
#     #is a JSON object# having the `label` and `value` as keys.

#     #Iterate through the data in `chartData` and insert into the `dataSource['data']` list.
#     for key, value in chartData.items():
#         data = {}
#     data["label"] = key
#     data["value"] = value
#     dataSource["data"].append(data)


# # Create an object for the column 2D chart using the FusionCharts class constructor
# # The chart data is passed to the `dataSource` parameter.
# column2D = FusionCharts("column2d", "myFirstChart", "600", "400", "myFirstchart-container", "json", dataSource)

# return render(request, 'index.html', {
#     'output': column2D.render()
# })