import json
import models
from config import *

def get_latest_attacks(count):
    """
    Get the latest count alarms. Returns a list of Attack models.
    """
    latest = models.Attack.objects.order_by("-when")[:count]
    return latest





