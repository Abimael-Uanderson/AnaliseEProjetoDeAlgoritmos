import math

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def compararX(ponto):
    return ponto.x

def compararY(ponto):
    return ponto.y

def distancia(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

def faixaMaisProxima(faixa, tamanho, d):
    faixa.sort(key=compararY)
    min_dist = d
    for i in range(tamanho):
        for j in range(i + 1, tamanho):
            if (faixa[j].y - faixa[i].y) < min_dist:
                dist = distancia(faixa[i], faixa[j])
                if dist < min_dist:
                    min_dist = dist
    return min_dist

def parMaisProximoRec(pontos, n):
    if n <= 3:
        min_dist = float('inf')
        for i in range(n):
            for j in range(i + 1, n):
                dist = distancia(pontos[i], pontos[j])
                if dist < min_dist:
                    min_dist = dist
        return min_dist

    meio = n // 2
    pontoMeio = pontos[meio]

    distEsquerda = parMaisProximoRec(pontos[:meio], meio)
    distDireita = parMaisProximoRec(pontos[meio:], n - meio)

    d = min(distEsquerda, distDireita)

    faixa = []
    for i in range(n):
        if abs(pontos[i].x - pontoMeio.x) < d:
            faixa.append(pontos[i])

    return min(d, faixaMaisProxima(faixa, len(faixa), d))

def parMaisProximo(pontos):
    pontos.sort(key=compararX)
    return parMaisProximoRec(pontos, len(pontos))

# Teste da função
pontos = [Ponto(2, 3), Ponto(12, 30), Ponto(40, 50), Ponto(5, 1), Ponto(12, 10), Ponto(3, 4)]
print(f"A menor distância é {parMaisProximo(pontos):.6f}")
