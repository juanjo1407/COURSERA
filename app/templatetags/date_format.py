from juanjo1407 import template
from juanjo1407.utils import formats
from datetime import datetime

register = template.Library()

@register.filter
def parseDateFormat(value, args):
    date = datetime.strptime(value, args)
    year = date.year
    month = date.strftime("%B")
    day = date.strftime("%d")
    hour = date.strftime("%H")
    minute = date.strftime("%M")
    formated_date = f'{day} {month} {year} at {hour}:{minute} UTC'
    return formated_date
