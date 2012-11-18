import time
import pprint

import django.shortcuts as shortcuts
from django.template import RequestContext, Context, loader
from django.http import HttpResponse, Http404, HttpResponseBadRequest

import feedparser

import logic
import models
import red_color_parser
from config import *


def filter_old_reports(reports):
    """
    Filter all the reports that are already in the database (this is done using item GUID only).
    """
    new_reports = []
    for report in reports:
        if not models.Attack.objects.filter(guid=report.guid):
            new_reports.append(report)

    return new_reports

def find_areas_in_report(report):
    """
    Return a list of Areas found in the report given.
    """
    all_areas = models.Area.objects.all()
    found_areas = []
    not_found = []
    
    for city in report.cities:
        found = False
        for area in all_areas:
            if area.hebrew_name in city:
                found = True
                found_areas.append(area)
                break
        
        if not found:
            not_found.append(city)
    
    logic.handle_unresolved_areas(not_found)
    
    return found_areas

def insert_reports(reports):
    """
    Insert the given reports to the database according to country.
    """
    for rep in reports:
        areas = find_areas_in_report(rep)
        
        for area in areas:
            area_model = models.Attack(area=area, when=rep.time, raw_item=rep.item, guid=rep.guid)
            area_model.save()

def sync_attacks():            
    reports = red_color_parser.parse_feed_into_items()
    new_reports = filter_old_reports(reports)
    insert_reports(new_reports)
    return new_reports


def home(request):
    request.session["last_check"] = time.time()
    sync_attacks()
    
    latest = logic.get_latest_attacks(10)
    
    t = loader.get_template("index.html")
    c = RequestContext(request, {"latest" : latest})
    return HttpResponse(t.render(c))



