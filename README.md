# Epidemic Estimator

## Aim
This small project, that I started out of boredom on the quarantine, aims at roughly estimating the course
of the SARS-CoV-2 epidemic in your country. Have fun and try it.

## How does it work?
Choose the country you want to estimate for, provide the beginning date and expected limit of cases
and the program will download data from the [CSSE database](https://github.com/CSSEGISandData/COVID-19)
and fit it with the logistic function.

## What are the requirements?
Unfortunately the program works only on Linux at the moment since it depends on **wget** to download
the data and on **gnuplot** to fit the data to the function and plot a graph. If you have an idea on
building versions for other platforms or making it platform-independent feel free to do it!

With that said make sure you have those two programs installed alongside **python 3** of course.

So go ahead and run:

`sudo apt update && sudo apt upgrade`

`sudo apt install gnuplot`

`sudo apt install python3`

**wget** should already be there but if for some reason it isn't:

`sudo apt install wget`

## How do I run the program?

Copy the repository from GitHub, cd to the directory and run:

`python3 epidemicEstimator.py`

From this point you will be asked to provide the details needed by the program to do the counting.

Alternatively you can input the details from terminal like so:

`python3 epidemicEstimator.py [country] [date in mm-dd-yyyy format] [case limit]`

Then the program generates an output file called *plot.png*. It contains a graph, have a look at it.

## How do I read the data?

0 on the x axis is the 1st of March 2020. The crosses are the number of cases read from the database.
The line is the logistic function which should illustrate the course of the epidemic according to the
data from the database and the case limit that you provided. The point where the curve flattens at the
upper right corner of the graph should be the time when the epidemic ends.

Additionally in your terminal there will be two numbers displayed: __*m*__, and __*s*__ alongside their
uncertainties. These correspond to the __*m*__ and __*s*__ parameters in the logistic function expressed by:

![g/(1+e^((m-x)/s))](https://latex.codecogs.com/gif.latex?\frac{g}{1&plus;e^{\frac{m-x}{s}}})


where:
* __*g*__ is the case limit
* __*e*__ is the Euler's constant

you can take these and plot this function in some other program if you wish.

##### Okay, but how do I determine this _" case limit "_ you've been talking about?

That is a good question... and one that I cannot answer with certainty.

At the  moment the only place where the epidemic seems to have reached the limit is China. The way I would do it
is take the number of cases there (or slightly more), divide it by the total population and multiply the resulting
ratio by your country's total population. Now the ratio will depend on whether we take whole China into consideration
(~0.00006) or only the Hubei Province (~0.0008).

There are however many other factors that will affect the case limit in your country like the population density,
the government's reaction time, people's attitude, etc. so I suggest experimenting with different numbers and finding
those that yield the best results for your 

## Exclaimers

There are some things that don't work yet but will be fixed. This includes:

* dates from before they started using mm-dd-yyyy format
* countries with multiple regions distinguished by the database (like France for example)

Some non-essential but nice-to-have features I might work on:

* swapping the command line parameters for something more flag-based
* making the graph display dates instead of numbers

## Can I help?

Sure you can! I invite everybody to contribute to the project in any way they can. So suggest features, help find errors,
work on aforementioned mods, refactor the code, do whatever you want.

What I would most appreciate however is for you to:

1. test the program for your country
1. check if there is any weird data in the covid.data (like sudden spikes of the number of cases)
1. find the reason for those and fix them if necessary in *corrections.py*

The database is somewhat imperfect, so there might be some country- or date-dependent errors to correct.

## Stay safe, friends!

