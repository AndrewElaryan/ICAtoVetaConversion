<!---
---
title: "README.md"
author: "Andrew Elaryan"
date: "2/2/2020"
output:
  rmarkdown::html_vignette:
    toc: true
---
-->

**Conversion of Intelligent Compaction Analyzer (ICA) Data to a Veta Compatible Format**

*Manual by Andrew Elaryan*

# Requirements

- Veta Software
- A python distribution and the ability to run python scripts
- Windows operating system


# Installation and Setup

1. Go to [https://github.com/AndrewElaryan/ICAtoVetaConversion](https://github.com/AndrewElaryan/ICAtoVetaConversion)
2. Click on the green &quot;Clone or download&quot; button
3. Select "Download as ZIP"
4. Extract into your folder of choice

# Formatting Data

This will be the most effort intensive step on the user's end.

1. Navigate to the folder where the code resides and enter the "Data" tab.
2. Copy and paste the ICA project data into this folder
3. In each subfolder, named after the workday, create two new subfolders: "GPS" and "VIB"
  a. Place all GPS **text** files in the "GPS" folder
  b. Place all vibration **MATLAB** files in the "VIB" folder

An example folder structure may look like:

+---Data

|   \---EOC

|       \---Jun2718

|           +---GPS

|           |       Jun2718gps0010.txt

|           |       Jun2718gps0011.txt

|           |       Jun2718gps0012.txt

…

|           |       Jun2718gps0045.txt

|           |       Jun2718gps005.txt

|           |       Jun2718gps006.txt

|           |

|           \---VIB

|                   Jun2718vib001.mat

|                   Jun2718vib0010.mat

|                   Jun2718vib0011.mat

|                   Jun2718vib0012.mat

…

|                   Jun2718vib006.mat

|                   Jun2718vib007.mat

|                   Jun2718vib008.mat

|                   Jun2718vib009.mat

|



4. Repeat the following for each workday in a project
  a. Select the folder of the requisite workday
  b. Hold "Shift" and right click on the folder representing the workday
  c. Select "Open PowerShell window here" or "Open Command Prompt Here";
  d. Copy and paste the following into the window and press "Enter":
    
    - For Powershell
    `cd GPS;cmd /r dir /s/b *.txt>zzlistgps.txt;cd ..;cd VIB;cmd /r dir /s/b *.mat>zzlistvib.txt`
    
    - For CMD
    `cd GPS;dir /s/b *.txt>zzlistgps.txt;cd ..;cd VIB;dir /s/b *.mat>zzlistvib.txt`

5. Exit the window

## Requirements

In a PowerShell window or CMD prompt, in the main folder, run:
`python -m pip install -r requirement.txt`

This should download all necessary requirements for conversion.

# Conversion

We will concatenate all the data files for each day into two files: one for the GPS data and one for the vibration data

## Concatenating GPS Files

1. In the GPS folder, click on the file "zzlistgps.txt"
2. Press "Home" on the top navigation bar and click "Copy path"
3. Go to the code folder, hold "Shift" and right click
4. Select "Open PowerShell window here" or "Open Command Prompt Here";
5. Run the following:

    `python concatenateGPSFiles.py`

6. When prompted, paste the path into the console and press enter



## Concatenating vibration Files

1. In the VIB folder, click on the file "zzlistvib.txt";
2. Press "Home" on the top navigation bar and click "Copy path";
3. Go to the code folder, hold "Shift"; and right click
4. Select "Open PowerShell window here" or "Open Command Prompt Here";
5. Run the following:

    `python concatenateMatlabData.py`

6. When prompted, paste the path into the console and press enter

## Creating Final Output

1. Open a PowerShell window or a Command Prompt window in the &quot;Code&quot; directory
2. Run the following:

    `python createFile.py`

1. The final output will be held in "converted_output.csv"

## Importing into Veta

If this is the first file in a project, then simply open the "converted_output.csv" with Veta.

If this is not the first file, then click on add new data file and us "converted_output.csv" as the new file.
