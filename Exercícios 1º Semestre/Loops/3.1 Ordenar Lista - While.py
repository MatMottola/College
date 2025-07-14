#Ordena uma lista digitada, em ordem ascendente.

x1=x2=i=aux=0

L1 = [0] * 10

#[0,0,0,0,0,0,0,0,0,0]


while i < 10:
	L1[i] = int(input("Digite o Elemento {}: ".format(i+1)))
	i = i+1

while x1 < 9:
	x2 = x1 + 1
	while x2 < 10:
		if L1[x1] > L1 [x2]:
			aux = L1[x1]
			L1[x1] = L1[x2]
			L1[x2] = aux
		x2 = x2 + 1
	x1 = x1 + 1

print (L1)