#
# Support for assignment 2
#

# Imports for use in your assignment
from Tkinter import *
import tkMessageBox

# Imports used only in the support code
import urllib2 as _urllib2
import functools as _functools
import datetime as _datetime
import time as _time


# This gives the purple colour used in plotting the power
POWER_COLOUR = "#c87cff"

# Note that the data will contain one more "array" than assignment 1.
ARRAYS = ['UQ Centre, St Lucia',
          'Concentrating Array',
          'Multi Level Car Park #1',
          'Multi Level Car Park #2',
          'Sir Llew Edwards Bld.',
          'Prentice Building',
          'Advanced Engineering Bld.',
          'Learning Innovation Bld.',
          'Global Change Institute',
          'All Arrays Combined']


def yesterday():
    """Returns yesterday's date as a string."""
    d = _datetime.datetime.today() - _datetime.timedelta(days=1)
    return d.strftime('%d-%m-%Y')


def pretty_print_data(date, time, temperature, sunlight, power,
                      is_cumulative=False):
    """Generate the string to be shown at the top of the application.

    If no time is currently selected, put `None` for all except the first
    parameter.

    Only CSSE7030 students will need to provide the is_cumulative parameter.
    """
    result = "Data for {}".format(date)
    if time is not None:
        result += " at {}:".format(time)
    if temperature is not None:
        result += '    Temperature {:>2.1f}C'.format(temperature)
    if sunlight is not None:
        result += '    Sunlight {:>4.1f}W/m^2'.format(sunlight)
    if power is not None:
        if is_cumulative:
            result += '    Energy {:>4.1f}kWh'.format(power/60000.0)
        else:
            result += '    Power {:>4.1f}kW'.format(power/1000.0)
    return result


class CoordinateTranslator(object):
    """Manages translation of data values into (x, y) coordinates.

    The application manages real-world data (temperatures, power, sunlight
    strength), but the Canvas drawings require (x, y) coordinates. This class
    converts between the two.

    The "index" parameter in each of the methods refers to the position of the
    value in the entire set of data (e.g. the first row of data corresponds to
    index = 0, the second row corresponds to index = 1, etc.)
    """
    # Internal data:
    ARRAY_MAXS = {'UQ Centre, St Lucia': 433000,
                  'Concentrating Array': 9500,
                  'Multi Level Car Park #1': 339000,
                  'Multi Level Car Park #2': 339000,
                  'Sir Llew Edwards Bld.': 91000,
                  'Prentice Building': 14000,
                  'Advanced Engineering Bld.': 121000,
                  'Learning Innovation Bld.': 45000,
                  'Global Change Institute': 154000,
                  'All Arrays Combined': 1500000}
    TERMPERATURE_MAX = 40.0
    SUNLIGHT_MAX = 1400.0

    def __init__(self, width, height, data_length):
        """Create a CoordinateTranslator with the given canvas width/height,
           and the number of rows of data.

        Constructor: CoordinateTranslator(int, int, int)
        """
        self._length = data_length
        self.resize(width, height)

    def resize(self, width, height):
        """Adjust the scaling factors to account for a new width/height.

        After the Canvas resizes, call this method to fix the scaling.
        """
        self._xscale = float(self._length) / width
        self._array_scale = {name: float(maxval) / height
                             for name, maxval in self.ARRAY_MAXS.items()}
        self._temperature_scale = self.TERMPERATURE_MAX / height
        self._sunlight_scale = self.SUNLIGHT_MAX / height

        self._width = width
        self._height = height

    def power_coords(self, index, power, array_name):
        """Given an index into the data, and a power value (in Watts),
           return (x, y) coordinates to plot.
        """
        return (index / self._xscale,
                self._height - power / self._array_scale[array_name])

    def temperature_coords(self, index, temperature):
        """Given an index into the data, and a temperature (in degrees C),
           return (x, y) coordinates to plot.
        """
        return (index / self._xscale,
                self._height - temperature / self._temperature_scale)

    def sunlight_coords(self, index, sunlight):
        """Given an index into the data, and a sunlight value,
           return (x, y) coordinates to plot.
        """
        return (index / self._xscale,
                self._height - sunlight / self._sunlight_scale)

    def get_index(self, x):
        """Given an x coordinate on the Canvas, return the index that it
           corresponds to.

           For example, get_index(0) -> 0,
           and get_index(width) -> highest index
        """
        return int(x * self._xscale + 0.5)


def _throttle(f):
    # You can safely ignore this function
    class RequestError(Exception):
        pass

    requests = []
    limit = 5

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


# The is taken from the solution to assignment 1. You're not required to use
# it, but you may wish to do so.
def load_data(dateStr):
    """Return the data for the arrays at the given date

    load_data(str) -> [(str,float,float,(int,...))]

    Precondition: dateStr corresponds to a valid date in dd-mm-yyyy foramt

    """
    text = get_data_for_date(dateStr)
    data = []

    for line in text.splitlines():
        time, temp, sun, powerStr = line.split(',', 3)

        power = []
        for p in powerStr.split(','):
            power.append(int(p))

        data.append((time, float(temp), float(sun), tuple(power)))

    return data

