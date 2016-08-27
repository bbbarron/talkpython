"""
New weather application developed as part of a Talk Python to Me class
Create on 8/25/2016. Adapted from the original. Retrieves from NWS site. Ultimately
date will go to Tkinter for Windows-like appearance.
bbarron
"""

# TODO: Modify to add Tkinter format

import collections      # Note this is a module from the Python standard library
import bs4              # Beautiful Soup module which enhances finding and parsing of web data
import requests         # Module to locate and load web page data

WeatherData = collections.namedtuple('WeatherData',
                                       'loc, temp, scale, cond, elev, measure')


def main():

    print_the_header()

    zcode = input('What zipcode do you want the weather for (e.g. 94526)? ')

    html = get_html_from_web(zcode)
    report = get_weather_from_html(html)

    print('The temp in {} is {} {} and {}'.format(
        report.loc,
        report.temp,
        report.scale,
        report.cond
    ))
    print('and the elevation is {}{}'.format(report.elev, report.measure))

    # display for the forecast


def print_the_header():
    print('---------------------------------')
    print('         NEW WEATHER APP')
    print('---------------------------------')
    print()


def get_html_from_web(zipcode):
    # TODO: change url to the NWS web site
    # url = 'http://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    url = 'http://forecast.weather.gov/MapClick.php?lat=37.8216&lon=-122#.V79EpZMrKf4'
    response = requests.get(url)
    # print(response.status_code)
    # print(response.text[0:1000])

    return response.text


def get_weather_from_html(html):

    # TODO: Modify items to get: Current temp, Today high, elevation, current conditions, and extended forecast

    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(id='current-conditions').find('h2').get_text()
    elev = soup.find(id='current-conditions').find(class_='smallTxt').get_text()
    # measure = soup.find(id='current').find(class_='wx-unit').get_text()
    condition = soup.find(id='seven-day-forecast').find(class_='short-desc').get_text()
    # temp = soup.find(id='curTemp').find(class_='wx-value').get_text()
    # scale = soup.find(id='curTemp').find(class_='wx-unit').get_text()
    #
    loc = cleanup_text(loc)
    print(loc)
    # loc = find_city_and_state_from_location(loc)
    elev = cleanup_text(elev)
    print(elev)
    condition = cleanup_text(condition)
    print(condition)
    print()
    # temp = cleanup_text(temp)
    # scale = cleanup_text(scale)

    # print(condition, temp, scale, loc)
    # return condition, temp, scale, loc
    # report = WeatherData(cond=condition, temp=temp, scale=scale, loc=loc, elev=elev, measure=measure)
    # return report


def find_city_and_state_from_location(loc: str):
    parts = loc.split('\n')
    return parts[0].strip()


def cleanup_text(text: str):
    if not text:
        return text

    text = text.strip()
    return text


if __name__ == '__main__':
    main()
