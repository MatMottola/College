#Indica se o primeiro e último dígitos são iguais ou diferentes.

num = prim_digit = ult_digit = 0

num = int(input("Digite num maior que 9"))

ult_digit = num % 10

while num > 9:
	prim_digit = num // 10
	num = prim_digit

if prim_digit == ult_digit:
	print("O primeiro (", prim_digit, ") e o ultimo (", ult_digit, ") são iguais")
else:
	print("O primeiro (", prim_digit, ") e o ultimo (", ult_digit, ") são diferentes")

#OU

	#print("O primeiro ({}) e o último ({}) são iguais".format(prim_digit, ult_digit))
#else:
	#print("O primeiro ({}) e o último ({}) são diferentes".format(prim_digit, ult_digit))