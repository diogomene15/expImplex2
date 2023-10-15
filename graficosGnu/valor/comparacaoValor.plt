set terminal pngcairo enhanced font 'Verdana,11' size 800, 600
set output 'comparacaoValores.png'

set title 'DP vs Greedy - Valores segmentos'
set xlabel 'n'
set ylabel 'Valor'

n = 1
DP = 2
Greedy = 4

set grid
set key left top

plot 'resultados.dat' using n:DP with linespoints  lw 2 title 'DP', \
     'resultados.dat' using n:Greedy with linespoints  lw 2 title 'Greedy', \