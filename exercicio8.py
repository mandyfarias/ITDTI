count = 0
resp = "s"
while resp == "s":
    num = float(input("Informe o números:"))
    soma = soma + num
    count += 1
    resp = str(input("Deseja continuar? (s/n)"))

media = soma / count
print(f"A média dos números informados foi: {media}")