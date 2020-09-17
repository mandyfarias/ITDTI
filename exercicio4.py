lista_elementos_1 = ['Douglas', 'Anderson', 'Libório', 'Maicon', 'Prefeito Géri']
lista_elementos_2  = ['Douglas', 'Maicon', 'Libório']

lista_final = (list(list(set(lista_elementos_1)-set(lista_elementos_2)) + list(set(lista_elementos_2)-set(lista_elementos_1))))

print(lista_final)