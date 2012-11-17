FEED_URL = r"https://www.facebook.com/feeds/page.php?id=201182249942365&format=rss20"


def _log(message, _pprint=False, _traceback=False):
    if _pprint:
        pprint.pprint(message)
    else:
        print message
    
    if _traceback:
        traceback.print_exc()
