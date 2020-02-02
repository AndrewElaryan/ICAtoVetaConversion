from fixData import get_data
import csv
import random
import math


#  Define any arbitrary values of headers
elevation = 114.00
passnumber = 1
radio = 0
design = "SE 44th St"  # "Hwy 198 CIPR 150608"
machine = "Dynapac CC524HF"  # "10 584 V1261 2015"
speed = 8.2
gps = "RTK Fixed"
acc = "Medium (0.164FT)"
target = 4
valpos = "Yes"
lift = 1
lastcmv = None
targcmv = 92
lastmdp = None
targmdp = None
lastrmv = None
lastfreq = 51
lastamp = 0.8
targthick = 0.348
gears = "Forward"
vibstate = "On"
density = 80.0


def initialize_array():
    """Add headers as first element in list of lists"""
    array = [['Time', 'Lat', 'Long', 'Elevation_FT', 'PassNumber', 'LastRadioLtncy', 'DesignName', 'Machine', 'Speed_mph',
             'LastGPSMode', 'GPSAccTol_FT', 'TargPassCount', 'ValidPos', 'Lift', 'LastCMV', 'TargCMV', 'LastMDP',
              'TargMDP', 'LastRMV', 'LastFreq_Hz', 'LastAmp_mm', 'TargThickness_FT', 'MachineGear', 'VibeState',
              'LastTemp_f', 'EDV']]
    return array


def create_line(timestep, amp, freq):
    """Create each row of data to be added to file"""
    line = [timestep[0], timestep[1], timestep[2], round(elevation + random.random(), 2), passnumber, radio, design, machine,
            round(random.uniform(7, 9), 1), gps, acc, target, valpos, lift, timestep[4], targcmv, lastmdp, targmdp, lastrmv,
            freq, amp, targthick, gears, vibstate, timestep[3], timestep[4]]
    return line


def get_vib_data(filename):
    import pandas
    colnames = ['amps', 'freqs']
    data = pandas.read_csv(filename, names=colnames)
    amps = data.amps.tolist()
    freqs = data.freqs.tolist()
    return amps, freqs


def main():
    data = get_data("fullGPSdata.txt")
    amps, freqs = get_vib_data("fullVIBdata.csv")
    lines = initialize_array()
    count = 0.0
    step = len(amps) / len(data)

    # Gather all lines in the files
    for timestep in data:
        line = create_line(timestep, amps[math.floor(count)], freqs[math.floor(count)])
        lines.append(line)
        count += step

    # Write lines to the output csv file
    with open('converted_output.csv', 'w', newline='') as writeFile:
        writer = csv.writer(writeFile)
        for line in lines:
            # Exclude all static passes
            if line[1] != 0 and line[2] != 0 and line[-1] != 80:
                writer.writerow(line)


if __name__ == "__main__":
    main()
