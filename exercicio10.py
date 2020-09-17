vitorias = input("Informe ao número de vitorias:")
empates = input("Informe ao número de empates:")
derrotas = input("Informe ao número de derrotas:")

peso_vitorias = 3
peso_empate = 1
peso_derrotas = 0
pontos = (vitorias * peso_vitorias) + (empates * peso_empate) + (derrotas * peso_derrotas)
partidas = vitorias + empates + derrotas
print(f"Seu time tem {pontos} pontos em {partidas} partidas.")