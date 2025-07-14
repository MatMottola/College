valor = 0.0
desct = 0.0

valor = float(input("Informe o Valor: "))

if valor <= 1000.00:
        desct = valor * 0.05

else:
        if valor <= 2000.00:
            desct = valor * 0.07
        else:
               if valor <= 3000.00:
                   desct = valor * 0.18
               else:
                   desct = valor * 0.10


print("O valor do desconto é: ", desct)
print("O valor a pagar é: ", valor - desct)

