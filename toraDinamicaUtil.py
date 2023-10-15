def toraDinamicaAux(precos, tamanhoTora, memento):
    res = -1
    if memento[tamanhoTora] >= 0:
        return memento[tamanhoTora]
    if tamanhoTora == 0:
        res = 0
    else:
        for i in range(1, tamanhoTora + 1):
            res = max(res, precos[i-1] + toraDinamicaAux(precos, tamanhoTora - i, memento))
    memento[tamanhoTora] = res
    return res

def toraDinamica(precos, tamanhoTora):
    memento = [-1] * (tamanhoTora + 1) # vetor de 'memória' de 0...tamanhoTora
    return toraDinamicaAux(precos, tamanhoTora, memento)



def toraGreedy(precos, tamanhoTora):
    vetorPesos = [-1] * (tamanhoTora)
    for i in range(0, tamanhoTora):
        precoTamAtual = precos[i]
        vetorPesos[i] = {
            "densidade": precoTamAtual / (i+1),
            "tamanho": i+1,
            "preco": precoTamAtual
          }
    vetorPesos.sort(key=lambda x: x["densidade"], reverse=True)
    restoTora = tamanhoTora
    valorTora = 0
    for item in vetorPesos:
        if item["tamanho"] <= restoTora:
            valorTora += item["preco"]
            restoTora -= item["tamanho"]
    return valorTora
            

rodCutters = {
  "DP": toraDinamica,
  "Greedy": toraGreedy,
}