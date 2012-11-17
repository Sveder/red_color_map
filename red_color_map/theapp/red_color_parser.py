# -*- coding: utf-8 -*-
import re
import pytz
import time
import pprint
import datetime
import htmlentitydefs

import feedparser

from config import *


REMOVE_ALARM = u"אזעקת צבע אדום"
HEBREW_SPLIT = "וב"



def decode_unicode_references(text):
    """
    The RSS feed is returned with HTML unicode encoding. This turns it back into unicode.
    Taken from:
    http://effbot.org/zone/re-sub.htm#unescape-html
    """
    def fixup(m):
        text = m.group(0)
        if text[:2] == "&#":
            # character reference
            try:
                if text[:3] == "&#x":
                    return unichr(int(text[3:-1], 16))
                else:
                    return unichr(int(text[2:-1]))
            except ValueError:
                pass
        else:
            # named entity
            try:
                text = unichr(htmlentitydefs.name2codepoint[text[1:-1]])
            except KeyError:
                pass
        return text # leave as is
    return re.sub("&#?\w+;", fixup, text)


def parse_cities(title):
    """
    Parse the attacked city from the title. The current way is very uninteligent, but pretty much works.
    """
    title = title.strip()
    without_alarm = title[len(REMOVE_ALARM):]
    all_cities = without_alarm.split(",")
    
    final_cities = []
    for city in all_cities:
        final_cities.append(city.strip())
    return final_cities

class Report:
    def __init__(self, cities, _time, item, guid):
        self.cities = cities
        #Time is given in +0000 timezone. Israel is in +0200 or +0300, so fix this:
        self.time = time.mktime(_time)
        self.time += 2 * 60 * 60
        self.item = item
        self.guid = guid


def parse_feed_into_items():
    parsed = feedparser.parse(FEED_URL)
    items = parsed["items"]
    
    reports = []
    for i in items:
        published = i["published_parsed"]
        
        title = i["title"]
        if not title:
            continue

        title = decode_unicode_references(title)
        cities = parse_cities(title)
        
        reports.append(Report(cities, published, i, i["guid"]))
        
    return reports


