import time
import pprint

import django.shortcuts as shortcuts
from django.template import RequestContext, Context, loader
from django.http import HttpResponse, Http404, HttpResponseBadRequest

import feedparser

import models
import red_color_parser



FEED_URL = r"https://www.facebook.com/feeds/page.php?id=201182249942365&format=rss20"


def _log(message, _pprint=False, _traceback=False):
    if _pprint:
        pprint.pprint(message)
    else:
        print message
    
    if _traceback:
        traceback.print_exc()


def filter_old_reports(reports):
    """
    Filter all the reports that are already in the database (this is done using item GUID only).
    """
    new_reports = []
    for report in reports:
        try:
            models.Attack.objects.get(guid=report.guid)
        except models.Attack.DoesNotExist:
            new_reports.append(report)
    print new_reports
    return new_reports

def find_areas_in_report(report):
    """
    Return a list of Areas found in the report given.
    """
    all_areas = models.Area.objects.all()
    found_areas = []
    for city in report.cities:
        found = False
        for area in all_areas:
            if area.hebrew_name in city:
                found = True
                found_areas.append(area)
        
        if not found:
            print "not found"
    
    return found_areas

def insert_reports(reports):
    """
    Insert the given reports to the database according to country.
    """
    for rep in reports:
        areas = find_areas_in_report(rep)
        
        for area in areas:
            area_model = models.Attack(area=area, when=rep.time, raw_item=rep.item)
            area_model.save()

def sync_attacks():            
    reports = red_color_parser.parse_feed_into_items()
    new_reports = filter_old_reports(reports)
    insert_reports(new_reports)
    return new_reports


def home(request):
    request.session["last_check"] = time.time()
    sync_attacks()
    
    #Show latest five:
    latest = models.Attack.objects.order_by("when")[:5]
    for i in latest:
        print i.when
    
    t = loader.get_template("index.html")
    c = RequestContext(request, {"latest" : latest})
    return HttpResponse(t.render(c))



