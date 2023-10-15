set terminal pngcairo enhanced font 'Verdana,11' size 800, 600
set output 'comparacaoCrescente.png'

set title 'Algoritmos de Ordenacao - Vetor crescente'
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

plot 'comparacaoCrescente.dat' using n:Quick with linespoints  lw 2 title 'Quick', \
     'comparacaoCrescente.dat' using n:Selection with linespoints  lw 2 title 'Selection', \
     'comparacaoCrescente.dat' using n:Merge with linespoints  lw 2 title 'Merge', \
     'comparacaoCrescente.dat' using n:Counting with linespoints  lw 2 title 'Counting', \
     'comparacaoCrescente.dat' using n:Heap with linespoints  lw 2 title 'Heap', \
     'comparacaoCrescente.dat' using n:Insertion with linespoints  lw 2 title 'Insertion'