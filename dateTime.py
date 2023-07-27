from datetime import datetime as __datetime
from datetime import timedelta as __timedelta
import pytz as __pytz

"""
Comment
"""

__DTall__ = ["now", "dateTimeAfterDays"]

def now(timeZone = None) -> __datetime:

    '''
    Returns current Date and Time of given timezone, 
    
    ``Default:`` local timezone
    '''

    if timeZone != None:
        if timeZone not in __pytz.all_timezones:
            raise TypeError(f'Not a valid timezone: {timeZone}')
        else:
            tz = __pytz.timezone(timeZone)
            return __datetime.now(tz)
    else:
        return __datetime.now()

def dateTimeAfterDays(daysCount: int, timeZone = None) -> __datetime:

    '''
    Returns dateTime object after given days count, 
    
    ``Default:`` local timezone
    '''

    if timeZone != None:
        if timeZone not in __pytz.all_timezones:
            raise TypeError(f'Not a valid timezone: {timeZone}')
        else:
            tz = __pytz.timezone(timeZone)
            dateAfterdaysRes = __datetime.now(tz) + __timedelta(days=int(daysCount))
            return dateAfterdaysRes
    else:
        dateAfterdaysRes = __datetime.now() + __timedelta(days=int(daysCount))
        return dateAfterdaysRes
