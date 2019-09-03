import urllib2 as _urllib2
import functools as _functools
import time as _time
import datetime


DATE_FORMAT = '%d-%m-%Y'

ARRAYS = ['UQ Centre, St Lucia',
          'Concentrating Array',
          'Multi Level Car Park #1',
          'Multi Level Car Park #2',
          'Sir Llew Edwards Bld.',
          'Prentice Building',
          'Advanced Engineering Bld.',
          'Learning Innovation Bld.',
          'Global Change Institute']


# Hint: print STATS_ROW.format(<name>, <power>)
# Example:  STATS_ROW.format("UQ Centre, St Lucia", 270.463)  gives:
# "UQ Centre, St Lucia                  270.4kW"

STATS_ROW = "{0:<30} {1:>11.1f}kW"

WEEKLY_HEADER = """
Date               Temp        Sunlight        Power
----------------------------------------------------"""

WEEKLY_ROW = "{0:>10}:  {1:>8.1f} C  {2:>8.1f} W/m^2  {3:>8.1f} kW"

class RequestError(Exception):
    pass


def _throttle(f):
    requests = []
    limit = 10

    @_functools.wraps(f)
    def wrapped(*args, **kwargs):
        now = _time.time()
        if len(requests) >= limit and (now - requests[-limit]) < 3.0:
            raise RequestError("Too many requests at once")
        else:
            requests.append(now)
            del requests[:-limit]
        return f(*args, **kwargs)
    return wrapped


@_throttle
def get_data_for_date(date):
    """Retrieve weather and PV data for the given date.

    'date' must be a string in the format DD-MM-YYYY
    Returns a string in the specified CSV format.

    Too many requests in a short time will cause the program to halt.
    """
    key = "%242a%2412%24di9J224JczEzGaBtM4gSjOvmhQRKIajQxoBuyVGtqTy6AvjhYytHq"
    url = "http://csse1001.uqcloud.net/cgi-bin/pv?date={0}&key={1}"
    conn = _urllib2.urlopen(url.format(date, key))
    text = conn.read()
    conn.close()

    if text.startswith('ERROR: '):
        raise ValueError(text.split(' ', 1)[1])
    return text


@_throttle
def get_max_data(date):
    """Retrieve daily maximum data for the given date.

    'date' must be a string in the format DD-MM-YYYY
    Returns a string in the specified CSV format.

    Too many requests in a short time will cause the program to halt.
    """
    key = "%242a%2412%24di9J224JczEzGaBtM4gSjOvmhQRKIajQxoBuyVGtqTy6AvjhYytHq"
    url = "http://csse1001.uqcloud.net/cgi-bin/pv?max=1&date={0}&key={1}"
    conn = _urllib2.urlopen(url.format(date, key))
    text = conn.read()
    conn.close()

    if text.startswith('ERROR: '):
        raise ValueError(text.split(' ', 1)[1])
    return text

