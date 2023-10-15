set terminal pngcairo enhanced font 'Verdana,11' size 800, 600
set output 'comparacaoTempo.png'

set title 'DP vs Greedy - Tempo de execução'
set xlabel 'n'
set ylabel 'Tempo (segundos)'

n = 1
DP = 3
Greedy = 5

set grid
set key left top

plot 'resultados.dat' using n:DP with linespoints  lw 2 title 'DP', \
     'resultados.dat' using n:Greedy with linespoints  lw 2 title 'Greedy', \