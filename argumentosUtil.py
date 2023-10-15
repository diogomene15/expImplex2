# Diogo de Lima Menezes e Marcos Vinicius Medeiros
import sys


class Args:

  def __init__(self):
    self.inc = 0
    self.fim = 0
    self.stp = 0
    self.carregarArgs()

  def checarArg(self, argInteiro, errMsg):
    if (not argInteiro.isdigit() or int(argInteiro) <= 0):
      print(errMsg)
      exit()

  def carregarArgs(self):
    args = sys.argv[1:]
    if len(args) % 2 != 0:
      print("Número de argumentos inválido")
      exit()
    if ("--inc" in args):
      self.inc = args[args.index("--inc") + 1]
      self.checarArg(
        self.inc,
        "o tamanho inicial das toras deve ser um número inteiro > 0")
    else:
      self.inc = input("Insira o tamanho inicial das toras: ")
      self.checarArg(
        self.inc,
        "o tamanho inicial das toras deve ser um número inteiro > 0")

    if ("--fim" in args):
      self.fim = args[args.index("--fim") + 1]
      self.checarArg(
        self.fim,
        "o tamanho final das toras (fim) deve ser um número inteiro > 0")
    else:
      self.fim = input("Insira o tamanho final das toras: ")
      self.checarArg(
        self.fim,
        "o tamanho final das toras (fim) deve ser um número inteiro > 0")

    if ("--stp" in args):
      self.stp = args[args.index("--stp") + 1]
      self.checarArg(
        self.stp,
        "o tamanho de intervalo entre as toras (stp) deve ser um número inteiro > 0"
      )
    else:
      self.stp = input("Insira o tamanho de intervalo entre as toras: ")
      self.checarArg(
        self.stp,
        "o tamanho de intervalo entre as toras (stp) deve ser um número inteiro > 0"
      )
    self.inc = int(self.inc)
    self.fim = int(self.fim)
    self.stp = int(self.stp)
