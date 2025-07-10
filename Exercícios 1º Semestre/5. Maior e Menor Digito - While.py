#Mostra o menor e o maior número digitado.

maior = num = 0
menor = 10000

while num != 9999:
	num = int(input("digite um numero entre 1 e 1000"))
	if num == 9999:
		break
	if num < 1 or num > 1000:
		print("Numero Invalido")
	else:
		if num < menor:
			menor = num
		if num > maior:
			maior = num

if menor == 10000:
	print("Nenhum digito válido inserido")
else:
	print("O Menor numero é:", menor)
	print("O Maior numero é:", maior)