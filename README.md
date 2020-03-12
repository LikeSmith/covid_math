#COVID-2019 Math

The purpose of this repo is to provide some base examples and tools for analyzing the
raw data we are getting concerning the ongoing Coronavirus pandemic.

## My Thoughts and Goals
In this day and age, we are inundated with a massive amount of raw data concerning the 2019
Coronavirus outbreak.  While data transparency is fantastic, it can also be misleading
without the proper tools to incorporate this data.  I want to create a starting point for
those who are interested in doing some analysis on their own.  I was inspired by the
2blue1brown video [here](https://www.youtube.com/watch?v=Kas0tIxDvrg).  As we continue to
weather this pandemic, I plan to build more examples into this repo, and I welcome anyone
else interested to contribute as well.

## Prerequisites
To use this repo, I recommend you install python and jupyter.  This is easily done with
a standard [Anaconda](https://www.anaconda.com/) installation.  Also make sure to install
numpy, and matplotlib.

## Usage
This repo is meant to be used in conjunction with the data provided by the Johns Hopkins
University Center for Systems Science and Engineering.  This data can be found on 
[github](https://github.com/CSSEGISandData/COVID-19), they also provide a nice dashboard
visualiser is [here](https://www.arcgis.com/apps/opsdashboard/index.html?fbclid=IwAR03dLt0vNGmB8zSftFXsRiBdQAwjBkptxid28LyUge6QQ_o12AFPIATpbI#/bda7594740fd40299423467b48e9ecf6)

Download the github repository, and modify the ```PATH_TO_DATA_REPO``` variable in the
```load_data.py``` file under ```covid_math/utilities``` in this repo.  This will point
the data loader to the correct spot.  If you are using windows, make sure to use
backslashes if you are using an absolute path.  You should also change the variable
```PATH_TO_DATA_DIR``` to use back slashes if you are using windows.  After you have
downloaded the data and fixed the ```load_data.py``` file, you are ready to begin!  Each
analysis project is self contained, and has a readme associated with it.  Each project comes
with a python file as well as a Jupyter notebook that explains the analysis in greater
detail.

## Authors
Dr. Kyle Crandall

Please wash your hands, cough into your elbow, and avoid touching your face.
