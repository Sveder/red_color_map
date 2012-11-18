import json
import time
import traceback

from dajaxice.decorators import dajaxice_register

import views
import models

@dajaxice_register
def check_attacks(request):
    """
    Get the latest attacks that happened since the client last talked with us.
    """
    try:
        views.sync_attacks()
        
        last_check = request.session["last_check"]
        since_last = models.Attack.objects.filter(when__gt=last_check)
        request.session["last_check"] = time.time()
        
        
        data = []
        for report in since_last:
            data.append({"lat" : report.area.center_lat,
                         "long" : report.area.center_long,
                         "hebrew_name" : report.area.hebrew_name,
                         })
            
        return json.dumps({"latest" : data})
    except:
        print "Something went wrong when checking_attacks:"
        traceback.print_exc()
        