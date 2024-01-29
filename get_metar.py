import urllib.request, re
from metar import Metar


def get_metar_encoded(airport):
    try:
        stream = urllib.request.urlopen('https://aviationweather-cprk.ncep.noaa.gov/metar/data?ids=' + airport + '&format=raw&hours=0&taf=off&layout=off')
        html_str = str(stream.read())
        metar = html_str.split("<code>")[1].split("</code>")[0]
        return metar
    except:
        raise ValueError("Failed to load METAR for %s" % airport)

metar_str = get_metar_encoded("KOCF")

obs = Metar.Metar(metar_str)

a=3
