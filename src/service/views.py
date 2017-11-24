from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.utils import timezone
from django.conf import settings
from decimal import Decimal
import datetime
import json
import re
from user.models import User
from .models import Order, Item, Service

# TODO: REMOVE THIS!!!
import os

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

def _is_decimal(s):
    try:
        Decimal(s)
        return True
    except ValueError:
        return False
def _is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

class ServiceListView(ListView):
    model = Service
    template_name = 'service_list.html'
    def post(self, request, *args, **kwargs):
        data = request.POST.dict()
        user_id = data['label']
        amount = data['withdraw_amount']
        if user_id and _is_int(user_id) and int(user_id) > 0 and _is_decimal(amount):
            user = User.objects.get(id = user_id)
            if not user or not user.is_authenticated:
                f = open(os.path.join(settings.MEDIA_ROOT, 'error_pay {0}.txt'.format(datetime.datetime.now())), 'w')
                f.write(str(data))
                f.close()
            else:
                user.account += Decimal(amount)
                user.save()
        # TODO: REMOVE THIS!
        f = open(os.path.join(settings.MEDIA_ROOT, 'root post {0}.txt'.format(datetime.datetime.now())), 'w')
        f.write(str(data))
        f.close()
        return HttpResponse(str(data))

class ServiceDetailView(DetailView):
    model = Service
    status = ''
    def get_template_names(self):
        return ['service_timetable.html' if not self.object.is_single_item else 'service_timetable_single.html']
    def get_context_data(self, **kwargs):
        context = super(ServiceDetailView, self).get_context_data(**kwargs)
        note = {}
        if self.status:
            status = self.status
            note['enabled'] = True
            note['type'] = self.status
            if status == 'success':
                note['text'] = 'Успех!'
            elif status == 'info':
                note['text'] = 'Заявка зарегистрирована. Осталось принести служебку. При наличии нескольких претендентов, удовлетворена будет заявка первого предъявившего служебку.'
            else:
                note['text'] = 'Это уведомление не должно было появиться! Сообщите о нём администрации'
                note['type'] = 'danger'
        context['notification'] = note
        return context
    def get(self, request, *args, **kwargs):
        data = request.GET.dict()
        status = data.get('status')
        if status:
            self.status = status
        return super(ServiceDetailView, self).get(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        # TODO: check required 'Rules accepted' checkbox
        status = 'success'
        data = request.POST.dict()
        lst = []
        title = data['title'] if data.get('title') else ''
        for k in data.keys():
            if k[:6] == 'order=':
                tmp = k[6:].split('&&')
                lst.append({'name': tmp[0], 'time_start': datetime.datetime.strptime(tmp[1], '%H:%M').time(), 'time_end': datetime.datetime.strptime(tmp[2], '%H:%M').time(), 'date_start': datetime.datetime.strptime(tmp[3], '%Y-%m-%d').date()})
        names = []
        for l in lst:
            names.append(l['name'])
        items = list(Item.objects.all())
        items_dict = {}
        for i in items:
            items_dict[i.name] = i
        total_price = 0
        for l in lst:
            total_price += items_dict[l['name']].get_price()
        #data['success'] = False
        final_orders = []
        if request.user.account >= total_price:
            # Can`t use bulk_create because 
            # it does not call save() and pre_save and post_save
            for l in lst:
                final_orders.append(Order(date_start = l['date_start'], 
                    time_start = l['time_start'], time_end = l['time_end'],
                    item = items_dict[l['name']], user = request.user, title = title))
            for o in final_orders:
                o.clean()
                #pass
            for o in final_orders:
                o.save()
                #pass
            request.user.account -= total_price
            request.user.save()

        #tmp = data['name'].split('&&')
        #data['result'] = str(total_price)
        #return HttpResponse(final_orders)
        return HttpResponseRedirect('?status={0}'.format(status))
