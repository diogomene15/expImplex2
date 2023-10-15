# Diogo de Lima Menezes e Marcos Vinicius Medeiros
import sys
import experimentosUtil
from argumentosUtil import Args
sys.setrecursionlimit(1000000000) # para evitar o erro de recursão no quicksort com vetores grandes ordenados

args = Args()
experimentosUtil.iniciar(args.inc, args.fim, args.stp)
