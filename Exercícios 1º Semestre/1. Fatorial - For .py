#Cálculo de fatorial.

num = int(input("Digite o num para calcular fatorial"))
fat = 1
for x in range(1, num+1):
	fat = fat * x
print("O fatorial de", num, "é", fat)
#Ou
#print("O fatorial de %2d é = %d" %(num, fat))