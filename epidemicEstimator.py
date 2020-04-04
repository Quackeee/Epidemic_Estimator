import os
import sys
import subprocess
from utils import wgetFile, generatePlotScript
from datetime import datetime, timedelta
from corrections import correct

data = []

if len(sys.argv) > 1:
    country = sys.argv[1]
else:
    country = str(input("What country do you want to calculate for? "))

if len(sys.argv) > 2:
    startdate = datetime.strptime(sys.argv[2], "%m-%d-%Y")
else:
    startdate = datetime.strptime(input("please input the beginning date [mm-dd-yyyy]: "), "%m-%d-%Y")

if len(sys.argv) > 3:
    limit = int(sys.argv[3])
else:
    limit = int(input("please input the estimated case limit: "))


i = 0

print("\nDownloading data, please wait...")

while True:
    filename = ((startdate + timedelta(days=i)).date()).strftime("%m-%d-%Y") + ".csv"
    try:
        if not os.path.isfile("./rawData/" + filename):
            url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data" \
                  "/csse_covid_19_daily_reports/" + filename
            wgetFile(url, 'rawData')
        i+=1
    except:
        break

for f in os.listdir("rawData"):
    f = open("./rawData/" + f)
    for line in f.readlines():
        line = line.split(',')
        if country in line:
            if len(line) > 11:
                data.append((line[4], line[7]))
            else:
                data.append((line[2], line[3]))

data = correct(data, country)
generatePlotScript(limit)

outfile = open("./covid.data", "w")
outfile.write("#day | number_of_cases")

for i in range(0, len(data)):
    if data[i][0][5:7] == '03':
        data[i] = (str(int(data[i][0][8:10])-1), data[i][1])
    elif data[i][0][5:7] == '01':
        data[i] = (str(int(data[i][0][8:10]) - 60), data[i][1])
    elif data[i][0][5:7] == '02':
        data[i] = (str(int(data[i][0][8:10]) - 29), data[i][1])
    elif data[i][0][5:7] == '04':
        data[i] = (str(int(data[i][0][8:10]) + 30), data[i][1])
    elif data[i][0][5:7] == '05':
        data[i] = (str(int(data[i][0][8:10]) + 60), data[i][1])
    outfile.write(data[i][0] + " " + data[i][1] + "\n")

outfile.close()
print("Calculating parameters, please wait...\n")

subprocess.run(['./plotscript.sh'])
