# Diogo de Lima Menezes e Marcos Vinicius Medeiros
import random
import time
import copy
from toraDinamicaUtil import *


def realizarExperimento(metodo, precos, tamanhoTora):
  params = [precos, tamanhoTora]
  inicioT = time.perf_counter()
  valorMaxTora = metodo(*params)
  fimT = time.perf_counter()
  return {"tempo": (fimT - inicioT), "valor":valorMaxTora}


def geraVetorAleatorio(tam):
  vetor = []
  for _ in range(1, tam + 1):
    vetor.append(random.randint(1, tam))
  return vetor

def imprimirResultados(resultados):
  print("n\tvDP\t\ttDP\t\tvGreedy\t\ttGreedy\t\t%")
  print("-" * 70)
  for tam, valoresTam in resultados.items():
    print(f"{tam}\t", end="")
    print("{:d}\t\t".format(valoresTam["vDP"]), end="")
    print("{0:.6f}\t".format(valoresTam["tDP"]), end="")
    print("{:d}\t\t".format(valoresTam["vGreedy"]), end="")
    print("{0:.6f}\t".format(valoresTam["tGreedy"]), end="")
    print("{0:.2f}\t".format(valoresTam["%"]), end="")
    print()
  print("\n")


def iniciar(inc, fim, stp):
  modeloResultado = {}
  tamanhosTora = range(inc, fim + 1, stp)
  for tam in tamanhosTora:
    modeloResultado[tam] = {}
    for nomeMetodo in rodCutters:
      modeloResultado[tam]["v"+nomeMetodo] = 0
      modeloResultado[tam]["t"+nomeMetodo] = 0
    modeloResultado[tam]["%"] = 0
  resultados = copy.deepcopy(modeloResultado)

  for tam in tamanhosTora:
      precosTora = geraVetorAleatorio(tam)
      for nomeMetodo, metodoMedicao in rodCutters.items():
        params = [metodoMedicao, precosTora, tam]
        resultadoExperimento = realizarExperimento(*params)
        resultados[tam]["v"+nomeMetodo] = resultadoExperimento["valor"]
        resultados[tam]["t"+nomeMetodo] = resultadoExperimento["tempo"]
      resultados[tam]["%"] = (resultados[tam]["vGreedy"] / resultados[tam]["vDP"]) * 100
  imprimirResultados(resultados)
  print(resultados)
  return (resultados)
