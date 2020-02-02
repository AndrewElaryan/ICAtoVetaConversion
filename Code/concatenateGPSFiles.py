from os import path


def sort_file_paths(filePaths):
    """Take file paths and sort them in ascending order"""
    sortedPaths = [None] * 100  # Use 100 because we will never that many files
    for path in filePaths:
        path = path[:-1]  # Remove newline ('\n') character
        pathNumber = path[-7:-4]  # Get number of the file
        pathIndex = int(pathNumber)  # Cast to int
        sortedPaths[pathIndex] = path

    sortedPaths[:] = [path for path in sortedPaths if path is not None]
    return sortedPaths


def write_file_lines(fout, filePaths):
    """Write all lines in a single file to the concatenated file"""
    filePaths = sort_file_paths(filePaths)
    for path in filePaths:
        file = open(path, "r").readlines()
        for line in file:
            fout.write(line)


def main():
    foutGPS = open("fullGPSdata.txt", "w", newline='')
    textPath = input("Please enter the absolute path for the GPS list file.\n")
    textPath = textPath.strip('\"')
    filePathsGPS = open(textPath, "r").readlines()
    filePathsGPS = filePathsGPS[:-1]  # Gets rid of the listtxt.txt file itself
    write_file_lines(foutGPS, filePathsGPS)
    foutGPS.close()


if __name__ == "__main__":
    main()
