import pprint

import django.shortcuts as shortcuts
from django.template import RequestContext, Context, loader
from django.http import HttpResponse, Http404, HttpResponseBadRequest

import feedparser


FEED_URL = r"https://www.facebook.com/feeds/page.php?id=201182249942365&format=rss20"


def _log(message, _pprint=False, _traceback=False):
    if _pprint:
        pprint.pprint(message)
    else:
        print message
    
    if _traceback:
        traceback.print_exc()

def home(request):
    parsed = feedparser.parse(FEED_URL)
    
    items = parsed["items"]
    
    _log(items[0], True)