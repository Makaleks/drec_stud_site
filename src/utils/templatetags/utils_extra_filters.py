from django import template
from django.utils import timezone
import datetime
import re

from service.models import Participation

register = template.Library()

@register.filter
def util_by_key(dictionary, key):
    return dictionary.get(key)

@register.filter
def util_range(i):
    return range(i)

@register.filter
def util_add_user_info(lst, user):
    for day in lst:
        for machine in day['items'].values():
            i = 0
            column = machine['time']
            length = len(column)
            while i < length:
                u = column[i].get('user')
                if u and u == user:
                    if (i != 0 and 'user' in column[i - 1]
                        and column[i - 1]['user'] != user):
                        column[i - 1].update({'show_info': True})
                    if (i != length - 1 and 'user' in column[i + 1]
                        and column[i + 1]['user'] != user):
                        column[i + 1].update({'show_info': True})
                id = column[i].get('id')
                if id and Participation.objects.filter(order = id, user = user):
                    column[i]['participated'] = True
                i+=1
            machine['time'] = column
    return lst

@register.filter
def util_is_started(time_start, service):
    service_td = datetime.datetime.combine(datetime.date.min, service.time_after_now) - datetime.datetime.min
    current_td = ((datetime.datetime.combine(
            datetime.date.min, timezone.now().time()) 
            - datetime.datetime.min) 
        - (datetime.datetime.combine(datetime.date.min, time_start)
            - datetime.datetime.min))
    if current_td <= service_td and current_td.days >= 0:
        return 'started'
    elif current_td > service_td and current_td.days >= 0:
        return 'ended'
    else:
        return 'ok'

@register.filter
def util_contains_string(url, s):
    r = re.compile(s)
    return bool(r.match(url))

# Django make_list supports only strings, it`s terrible
@register.filter
def util_to_list(lst):
    return list(lst)

# Django make_list supports only strings, it`s terrible
@register.filter
def util_by_index(lst,i):
    return lst[i]
