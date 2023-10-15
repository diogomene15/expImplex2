# Diogo de Lima Menezes e Marcos Vinicius Medeiros
import random
import time
import copy
from toraDinamicaUtil import *


def medirTempo(metodo, vetor, ini=None, fim=None):
  vetorCopia = vetor.copy()
  params = [vetorCopia, ini, fim]
  params = [p for p in params if p != None]

  inicioT = time.perf_counter()
  metodo(*params)
  fimT = time.perf_counter()
  return fimT - inicioT


def geraVetorAleatorio(tam):
  vetor = []
  for _ in range(1, tam + 1):
    vetor.append(random.randint(1, tam * 4))
  return vetor


def desordenaVetor(vetor, porcentagemDesordem=10):
  tamVetor = len(vetor)
  # Resolveu-se por dividir a porcentagem de desordem por 2
  # para que o número total de itens desordenados seja, de fato,
  # mais próxima de dois por cento, em relação ao tamanho do vetor.
  numItemsDesordem = int(porcentagemDesordem / 100 / 2 * tamVetor)
  indicesDesordenados = random.sample(range(tamVetor), numItemsDesordem)
  for indiceDes in indicesDesordenados:
    novoIndice = random.randint(0, tamVetor - 1)
    temp = vetor[novoIndice]
    vetor[novoIndice] = vetor[indiceDes]
    vetor[indiceDes] = temp


def geraVetores(tam):
  vetorAleatorio = geraVetorAleatorio(tam)
  vetorOrdemCresc = vetorAleatorio[:]
  vetorOrdemCresc.sort()
  vetorReverso = vetorAleatorio[:]
  vetorReverso.sort(reverse=True)
  vetorQuaseOrdenado = vetorOrdemCresc[:]
  desordenaVetor(vetorQuaseOrdenado)
  return {
    "RANDOM": vetorAleatorio,
    "SORTED": vetorOrdemCresc,
    "REVERSE": vetorReverso,
    "NEARLY SORTED": vetorQuaseOrdenado
  }


def media(vetor):
  return sum(vetor) / len(vetor)


def imprimirResultados(resultados):
  for tipoVetor, valoresTipoVetor in resultados.items():
    print(f"[ [{tipoVetor}] ]")
    print("n\tSelection\tInsertion\tMerge\t\tHeap\t\tQuick\t\tCounting")
    print("-" * 96)
    for tam, valoresTam in valoresTipoVetor.items():
      print(f"{tam}\t", end="")
      for nomeOrd, valOrd in valoresTam.items():
        print("{0:.6f}\t".format(valOrd), end="")
      print()
    print("\n")


def iniciar(inc, fim, stp, rpt):
  modeloResultado = {}
  tamanhosVetores = range(inc, fim + 1, stp)
  for tam in tamanhosVetores:
    modeloResultado[tam] = {}
    for nomeOrd in ordenadores:
      modeloResultado[tam][nomeOrd] = []
  resultados = {
    "RANDOM": copy.deepcopy(modeloResultado),
    "SORTED": copy.deepcopy(modeloResultado),
    "REVERSE": copy.deepcopy(modeloResultado),
    "NEARLY SORTED": copy.deepcopy(modeloResultado)
  }

  for tam in tamanhosVetores:
    for _ in range(rpt):
      vetoresTeste = geraVetores(tam)
      for nomeTipoVetor, vetor in vetoresTeste.items():
        if( (nomeTipoVetor == "SORTED" or nomeTipoVetor == "REVERSE") and _ > 0):
          continue
        for nomeOrd, metodoOrd in ordenadores.items():
          params = []
          if (nomeOrd == "mergeSort" or nomeOrd == "quickSort"):
            params = [metodoOrd, vetor, 0, len(vetor) - 1]
          elif (nomeOrd == "countingSort"):
            params = [metodoOrd, vetor, max(vetor)]
          else:
            params = [metodoOrd, vetor]
          resultados[nomeTipoVetor][tam][nomeOrd].append(medirTempo(*params))

  # Depois da execução de todo o conjunto de experimentos
  # realiza-se a média dos tempos de cada repetição.
  for tipoVetor in resultados:
    for tam in tamanhosVetores:
      for nomeOrd in ordenadores:
        vetorTempoOrd = resultados[tipoVetor][tam][nomeOrd]
        resultados[tipoVetor][tam][nomeOrd] = sum(vetorTempoOrd) / rpt
  imprimirResultados(resultados)
  return (resultados)
