set terminal pngcairo enhanced font 'Verdana,11' size 800, 600
set output 'comparacaoDecrescenteMenores.png'

set title 'Algoritmos de Ordenacao - Vetor decrescente'
set xlabel 'n'
set ylabel 'Tempo (segundos)'

n = 1
Selection = 2
Insertion = 3
Merge = 4
Heap = 5
Quick = 6
Counting = 7

set grid
set key left top

plot 'comparacaoDecrescente.dat' using n:Merge with linespoints  lw 2 title 'Merge', \
     'comparacaoDecrescente.dat' using n:Counting with linespoints  lw 2 title 'Counting', \
     'comparacaoDecrescente.dat' using n:Heap with linespoints  lw 2 title 'Heap'