---
title: "README.md"
author: "Andrew Elaryan"
date: "2/2/2020"
output:
  rmarkdown::html_vignette:
    toc: true
---

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

This will be the most effort intensive step on the user&#39;s end.

1. Navigate to the folder where the code resides and enter the &quot;Data&quot; tab.
2. Copy and paste the ICA project data into this folder
3. In each subfolder, named after the workday, create two new subfolders: &quot;GPS&quot; and &quot;VIB&quot;
  a. Place all GPS **text** files in the &quot;GPS&quot; folder
  b. Place all vibration **MATLAB** files in the &quot;VIB&quot; folder

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
  b. Hold &quot;Shift&quot; and right click on the folder representing the workday
  c. Select &quot;Open PowerShell window here&quot;
  d. Copy and paste the following into the window and press &quot;Enter&quot;:

    `cd GPS & dir /s/b *.txt & zzlistgps.txt & cd .. & cd VIB & dir /s/b *.mat & zzlistvib.txt`

5. Exit the PowerShell window

# Conversion

We will concatenate all the data files for each day into two files: one for the GPS data and one for the vibration data

## Concatenating GPS Files

1. In the GPS folder, click on the file &quot;zzlistgps.txt&quot;
2. Press &quot;Home&quot; on the top navigation bar and click &quot;Copy path&quot;
3. Go to the code folder, hold &quot;Shift&quot; and right click
4. Select &quot;Open PowerShell window here&quot;
5. Run the following:

    `python concatenateGPSFiles.py`

6. When prompted, paste the path into the console and press enter



## Concatenating vibration Files

1. In the VIB folder, click on the file &quot;zzlistvib.txt&quot;
2. Press &quot;Home&quot; on the top navigation bar and click &quot;Copy path&quot;
3. Go to the code folder, hold &quot;Shift&quot; and right click
4. Select &quot;Open PowerShell window here&quot;
5. Run the following:

    `python concatenateMatlabData.py`

6. When prompted, paste the path into the console and press enter

## Creating Final Output

1. Open a PowerShell window in the &quot;Code&quot; directory
2. Run the following:

    `python createFile.py`

1. The final output will be held in &quot;converted\_output.csv&quot;

## Importing into Veta

If this is the first file in a project, then simply open the &quot;converted\_output.csv&quot; with Veta.

If this is not the first file, then click on add new data file and us &quot;converted\_output.csv&quot; as the new file.
