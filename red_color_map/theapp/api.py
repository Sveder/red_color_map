import json
import time
import datetime

import django.shortcuts as shortcuts
from django.template import RequestContext, Context, loader
from django.http import HttpResponse, Http404, HttpResponseBadRequest

import logic
import models

def latest(request):
    latest = logic.get_latest_attacks(10)
    dict_list = []
    for i in latest:
        dict_list.append(i.get_dict())
        
    answer = json.dumps(dict_list)
    return HttpResponse(answer)



def latest_debug(request):
    latest = logic.get_latest_attacks(10)
    
    html = ""
    for rep in latest:
        html += str(datetime.datetime.fromtimestamp(rep.when))
        html += " --- "
        html += rep.area.hebrew_name
        html += "<br>"
        
    return HttpResponse(html)


def area_error(request):
    unsolved = models.AreaError.objects.filter(solved=False)
    
    html = "<br>".join([i.name for i in unsolved])
    return HttpResponse(html)