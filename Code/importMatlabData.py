import scipy.io as spio
import pandas as pd


def import_vib_data(filename):
    """Import speed, density, temperature"""
    mat = spio.loadmat(filename)
    array = mat['matchedVib']#[::1000]
    df = pd.DataFrame(array)
    return df


def import_pass_data(filename):
    """Import pass count, roller direction"""
    passCountList = []
    directionList = []
    passData = []
    usefulPass = spio.loadmat(filename)
    usefulPass = usefulPass['usefulPass']
    for array in usefulPass:
        for element in array:
            for cell in element:
                passCountList.append(cell[0][0][0])
                directionList.append(cell[1][0])
    for index in range(len(passCountList)):
        passData.append([passCountList[index], directionList[index]])
    df = pd.DataFrame(passData)
    return df


def import_GPS_data(filename):
    """Import latitude, longitude"""
    mat = spio.loadmat(filename)
    array = mat['matchedGps']
    df = pd.DataFrame(array)
    return df


def import_spec_data(filename):
    """Import power spectrum data"""
    mat = spio.loadmat(filename)
    array = mat['spec']
    df = pd.DataFrame(array)
    df.columns = df.iloc[0]
    df = df[1:]
    return df
