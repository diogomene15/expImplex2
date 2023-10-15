set terminal pngcairo enhanced font 'Verdana,11' size 800, 600
set output 'comparacaoQuaseOrdMenores.png'

set title 'Algoritmos de Ordenacao - Vetor quase ordenado'
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

plot 'comparacaoQuaseOrd.dat' using n:Quick with linespoints  lw 2 title 'Quick', \
     'comparacaoQuaseOrd.dat' using n:Merge with linespoints  lw 2 title 'Merge', \
     'comparacaoQuaseOrd.dat' using n:Counting with linespoints  lw 2 title 'Counting', \
     'comparacaoQuaseOrd.dat' using n:Heap with linespoints  lw 2 title 'Heap'