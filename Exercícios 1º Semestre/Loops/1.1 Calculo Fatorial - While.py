#Calcula o fatorial de um número digitado

num = int(input ("Digite número para calcular fatorial "))
fat = 1
ini = num

while num > 0:
	fat = fat * num
	num = num - 1
print("O fatorial de", ini, "é", fat)
#Ou
#print("O fatorial de %2d é = %d" %(ini, fat))