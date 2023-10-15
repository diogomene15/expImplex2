set terminal pngcairo enhanced font 'Verdana,11' size 800, 600
set output 'valorGreedy.png'

set title 'Greedy - Valores segmentos'
set xlabel 'n'
set ylabel 'Valor'

n = 1
Greedy = 4

set grid
set key left top

plot 'resultados.dat' using n:Greedy with linespoints  lw 2 title 'Greedy', \