#Ordenar três números inteiros em ordem crescente sem o uso de loops.

n1=n2=n3=aux=0

n1=int(input("Digite o primeiro número: "))
n2=int(input("Digite o segundo número: "))  
n3=int(input("Digite o terceiro número: "))

if n1>n2:
    aux = n1
    n1 = n2
    n2 = aux

if n1>n3:
    aux = n1
    n1 = n3
    n3 = aux

if n2>n3:
    aux = n2
    n2 = n3
    n3 = aux

print("Os números em ordem crescente são: ", n1, n2, n3)