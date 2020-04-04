l(x)=30000/(1+exp((m-x)/s))
fit l(x) "covid.data" via m,s
set xr [m-5*s:m+5*s]
set yr [0:30000]
set xtics 10
set ytics auto
set yzeroaxis
set terminal png size 1920,1080
set output "plot.png"
plot "covid.data" title "Confirmed Cases", l(x) title "Approximation"
quit
