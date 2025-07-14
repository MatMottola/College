#Combinar 10 números 3 a 3.

N = [0] * 10

#[0,0,0,0,0,0,0,0,0,0]

for x in range (0,10):
	N[x] = int(input("Digite um num"))

for x1 in range (0,8):
	for x2 in range (x1 +1,9):
		for x3 in range (x2+1,10):
print(N[x1], "", N[x2], "", N[x3])