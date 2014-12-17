import json

import models
from config import *

def get_latest_attacks(count):
    """
    Get the latest count alarms. Returns a list of Attack models.
    """
    latest = models.Attack.objects.order_by("-when")[:count]
    return latest


def handle_unresolved_areas(not_found):
    """
    Update the unresolved areas table.
    """
    for area in not_found:
        try:
            models.AreaError.objects.get(name=area)
        except models.AreaError.DoesNotExist:
            error_model = models.AreaError(name=area)
            error_model.save()
            lol_model = models.AreaError(name=area)
            lol_model.save()
            