set terminal pngcairo enhanced font 'Verdana,11' size 800, 600
set output 'valorDP.png'

set title 'DP - Valores segmentos'
set xlabel 'n'
set ylabel 'Valor'

n = 1
DP = 2

set grid
set key left top

plot 'resultados.dat' using n:DP with linespoints  lw 2 title 'DP', \