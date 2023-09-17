from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from app1.models import *
from app1.forms import *
from django.contrib.auth.decorators import login_required
from .models import Maid, AvailabilitySlot
from datetime import datetime
from django.db.models import Q
# Create your views here.



    

def find_maids(request):
    sdd=AvailabilitySlot.objects.all()
    d={'sdd':sdd}
    if request.method=='POST':
        try:
            requested_time_str = request.POST['datetime']
            requested_time=' '.join(requested_time_str.split('T'))
            

            available_maids = Maid.objects.filter(
                (Q(availabilityslot__start_time__lte=requested_time) |
                Q(availabilityslot__end_time__gte=requested_time)) & 
                (Q(availabilityslot__start_time__lte=requested_time) &
                Q(availabilityslot__end_time__gte=requested_time))
            ).order_by('-rating')

            if not available_maids:
                message = "Sorry, no maids available."
                return render(request, 'error.html', {'message': message})

            return render(request, 'maid_list.html', {'maids': available_maids})
        except ValueError:
            message = "Invalid time format. Please use HH:MM."
            return render(request, 'error.html', {'message': message})
    return render(request,'b.html',d)

def home(request):
    return render(request,'home.html')



def booking(request):
    data=booking_detail.objects.all()
    book=booking_detail2()
    d={'book':book,'data':data}
    if request.method=='POST':
        bok=booking_detail2(request.POST)
        for i in data:
            if i.maid in data:
                if bok.is_valid() :
                    bok.save()
                return HttpResponse('booking done')
            else:
                return HttpResponse('data already store')
                
    return render(request,'booking.html',d)