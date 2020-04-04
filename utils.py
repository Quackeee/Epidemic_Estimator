import subprocess


def run(cmd):
    proc = subprocess.Popen(cmd,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            )
    stdout, stderr = proc.communicate()
    return proc.returncode, stdout, stderr


def wgetFile(url, directory=''):
    wget = run(['wget', '-P', './' + directory, url])

    if wget[0] == 8:
        raise Exception("File doesn't exist")


def generatePlotScript(limit):
    plotscript = open("./plotscript.plot", 'w')
    plotscript.write("l(x)=" + str(limit) +

"""/(1+exp((m-x)/s))
fit l(x) "covid.data" via m,s
set xr [m-5*s:m+5*s]
set yr [0:""" + str(limit) + """]
set xtics 10
set ytics auto
set yzeroaxis
set terminal png size 1920,1080
set output "plot.png"
plot "covid.data" title "Confirmed Cases", l(x) title "Approximation"
quit
"""
                                            )
    plotscript.close()
