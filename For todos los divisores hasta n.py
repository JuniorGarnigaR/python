lista_numeros = []
lista_divisores = []
division = 0
lista_divisores2 = []
valor = True
limite = int(input("Ingrese un número: \n\t"))
k = 0

print(f"Los divisores de 1 hasta {limite} \n\t")

for i in range(limite+1):

	if i == 0:
		continue
	lista_numeros.append(i)


for k in range(limite):
	k+=1

	for j in range(k):
		j+=1
		division = k/j
		if valor == (division in lista_numeros):
			lista_divisores.append(division)

	if len(lista_divisores) == 2:
		print(f"Los divisores de {j} son: {lista_divisores} \n\tEs un número primo \n")
	else:
		print(f"Los divisores de {j} son: {lista_divisores} \n\tEs un número mixto \n")
	lista_divisores.clear()



