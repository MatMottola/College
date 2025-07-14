#Ordenar lista com 15 elementos, em ordem crescente.

x1=x2=aux=0

L1 = [0] * 15

#[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]



for x1 in range(0,15):
	L1 [x1] = int(input("Digite o elemento"))
				#ou
	#L1[x1] = int(input("Digite o elemento {}: ".format(x1 + 1)))


for x1 in range (0,14):
	for x2 in range(x1+1,15):
		if L1[x1] > L1 [x2]:
			aux = L1[x1]
			L1[x1] = L1[x2]
			L1[x2] = aux

for x1 in range (0,15):
	print (L1[x1])