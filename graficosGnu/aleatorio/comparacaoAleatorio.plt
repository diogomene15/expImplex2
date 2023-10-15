set terminal pngcairo enhanced font 'Verdana,11' size 800, 600
set output 'comparacaoAleatorio.png'

set title 'Algoritmos de Ordenacao - Vetor aleatório'
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

plot 'comparacaoAleatorio.dat' using n:Selection with linespoints  lw 2 title 'Selection', \
     'comparacaoAleatorio.dat' using n:Insertion with linespoints  lw 2 title 'Insertion', \
     'comparacaoAleatorio.dat' using n:Merge with linespoints  lw 2 title 'Merge', \
     'comparacaoAleatorio.dat' using n:Heap with linespoints  lw 2 title 'Heap', \
     'comparacaoAleatorio.dat' using n:Quick with linespoints  lw 2 title 'Quick', \
     'comparacaoAleatorio.dat' using n:Counting with linespoints  lw 2 title 'Counting'