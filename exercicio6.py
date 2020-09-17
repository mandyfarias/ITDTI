seq_max = int(input("Quantas sequências deseja projetar? (Apenas números inteiros):"))
proximo = 0
anterior = 0
seq_atual = 0
while(seq_max > seq_atual):
    print(proximo)
    proximo = proximo + anterior
    anterior = proximo - anterior
    seq_atual = seq_atual + 1
    if (proximo == 0):
        proximo = proximo + 1