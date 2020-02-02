import datetime

# One file used to help convert data from the Pavement Materials and Systems Group's Intelligent Compaction Analyzer to
# the industry standard visualization software. This specific file provides functions to fix units and formatting for
# GPS and time data


def fix_time(rawtime):
    """Convert time output to standard format"""
    rawtime = rawtime[:-3]
    fixedtime = datetime.datetime.strptime(rawtime, '%H:%M:%S')
    fixedtime = fixedtime.replace(year=2018, month=6, day=27)
    fixedtime = fixedtime.strftime("%Y-%b-%d %H:%M:%S.%f")[:-3]
    return fixedtime


def degmin_to_deg(loc):
    if loc.find('.') >= 0:
        decimal = loc.find('.')
        degrees = float(loc[:decimal - 2])
        minutes = float(loc[decimal - 2:]) / 60.0
        degrees += minutes
        return degrees
    return 0.0


def fix_lat_lon(lat, lon):
    """Convert convert gps data to latitude, longitude"""
    lat = float(degmin_to_deg(lat[:-1]))
    lon = -1 * float(degmin_to_deg(lon[:-1]))
    return lat, lon


def process(line, dataPoints):
    """Process data from input file"""
    line = line[2:-2].split(',')
    dataPoints.append(fix_time(line[0]))
    dataPoints.append(fix_lat_lon(line[1], line[2]))
    dataPoints.append(float(line[3]))


def get_data(filename):
    """Get data from input file and return data points"""
    with open(filename, 'r') as data:
        dataStrings = []
        dataPoints = []
        for element in data:
            dataStrings.append(element[2:-2])
        for s in dataStrings:
            s = s.split(',')
            fixedTime = fix_time(s[0])
            fixedLat, fixedLon = fix_lat_lon(s[1], s[2])
            fixedTemperature = float(s[3])
            fixedDensity = float(s[4])
            dataPoints.append([str(fixedTime), fixedLat, fixedLon, fixedTemperature, fixedDensity])
    return dataPoints
