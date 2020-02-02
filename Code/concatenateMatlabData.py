from os import path
from vibrationConversions import output_amp_freq
import csv


def get_file_number(path, start=-8, end=-5):
    while start < end:
        range = path[start:end]
        try:
            return int(range)
        except ValueError:
            start += 1
    return None


def sort_file_paths(filePaths):
    """Take file paths and sort them in ascending order"""
    sortedPaths = [None] * len(filePaths) * 4
    for path in filePaths:
        pathIndex = get_file_number(path)
        sortedPaths[pathIndex] = path
    sortedPaths[:] = [path for path in sortedPaths if path is not None]
    return sortedPaths


def get_vib_data(filePaths):
    fullAmps = []
    fullFreqs = []
    for filePath in filePaths:
        amps, freqs = output_amp_freq(path.relpath(filePath[:-1]))
        for i in range(len(amps)):
            if amps[i]:
                fullAmps.append(amps[i])
            if freqs[i]:
                fullFreqs.append(freqs[i])
    return fullAmps, fullFreqs


def write_file_lines(fout, filePaths):
    """Write all lines in a single file to the concatenated file"""
    filePaths = sort_file_paths(filePaths)
    fullAmps, fullFreqs = get_vib_data(filePaths)
    with open(fout, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(zip(fullAmps, fullFreqs))


def main():
    fout = "fullVIBdata.csv"
    textPath = input("Please enter the absolute path for the VIB list file.\n")
    textPath = textPath.strip('\"')
    filePathsVib = open(textPath, "r").readlines()
    write_file_lines(fout, filePathsVib)


if __name__ == "__main__":
    main()
