# Diogo de Lima Menezes e Marcos Vinicius Medeiros
import sys
import experimentosUtil
from argumentosUtil import Args
sys.setrecursionlimit(1000000000) # para evitar qualquer possível erro de recursão

args = Args()
experimentosUtil.iniciar(args.inc, args.fim, args.stp)
