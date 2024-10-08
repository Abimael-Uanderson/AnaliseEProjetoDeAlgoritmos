# Número de times
tam = 16
pontos = [16, 8, 15, 15, 21, 14, 5, 0, 2, 9, 7, 5, 10, 12, 13, 14]
times = [
    "Argentina", "Peru", "Chile", "Canadá",
    "México", "Equador", "Venezuela", "Jamaica",
    "Estados Unidos", "Uruguai", "Panamá", "Bolívia",
    "Brasil", "Colômbia", "Paraguai", "Costa Rica"
]

# Ordenação dos times com base nos pontos
for i in range(tam):
    for j in range(i + 1, tam):
        if pontos[j] > pontos[i]:
            # Troca de pontos
            pontos[i], pontos[j] = pontos[j], pontos[i]
            # Troca de times
            times[i], times[j] = times[j], times[i]

# Impressão dos resultados
for i in range(tam):
    print(f"Time: {times[i]}")
    print(f"Pontos: {pontos[i]}\n")
