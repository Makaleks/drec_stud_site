from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from django.db.models import Q
from django.utils import timezone
import datetime
import json
import re
from .models import Order, Service

# Create your views here.

def unlock(request, slug):
    uid = request.GET.get('uid')
    today = timezone.now()
    orders = Order.objects.all().filter(Q(user__uid = uid, item__service__slug = slug, date_start = today.date(), time_start__lte = today.time()) & (Q(time_end__gt = today.time()) | Q(time_end = datetime.time(0,0,0))))
    #return HttpResponse(str([vars(o) for o in orders]))
    if orders:
        return HttpResponse('yes')
    else:
        return HttpResponse('no')

def to_H_M(t):
    return re.sub(r'(?P<part>^|:)0', '\g<part>', t.strftime('%H:%M'))

def list_update(request, slug):
    today = timezone.now()
    orders = Order.objects.all().filter(Q(date_start = today.date(), item__service__slug = slug) & (Q(time_end__gt = today.time()) | Q(time_end = datetime.time(0,0,0))) | Q(date_start__gt = today.date())).order_by('date_start', 'time_end')
    return HttpResponse(json.dumps([{'uid': o.user.uid, 'date_start': str(o.date_start), 'time_start': to_H_M(o.time_start), 'time_end': to_H_M(o.time_end)} for o in orders]))

class ServiceListView(ListView):
    model = Service
    template_name = 'service_list.html'

class ServiceDetailView(DetailView):
    model = Service
    template_name = 'service_timetable.html'
    def post(self, request, *args, **kwargs):
        # TODO: check required 'Rules accepted' checkbox
        return HttpResponse(str(request.POST.dict()))
