#Verificador de Par ou Ímpar sem o uso de loops usando bitwise.

num = int(input("Digite um número: "))

b = num >> 1

b= b << 1

if b == num:
    print("O número é par.")

else:
    print("O número é ímpar.")
