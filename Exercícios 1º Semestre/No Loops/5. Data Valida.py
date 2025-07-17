#Verificador de data válida sem o uso de loops.

dd=[00,31,28,31,30,31,30,31,31,30,31,30,31]
ind_erro=dia=mes=ano= 0


dia = input("Digite o dia: ")
mes = input("Digite o mês: ")
ano = input("Digite o ano: ")

if dia.isdigit() and mes.isdigit() and ano.isdigit():
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)

else:
    dia=mes=ano= 0
    ind_erro= 1


if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    dd[2] = 29

else:
    dd[2] = 28


if dia < 1 or ano < 1 or mes < 1 or mes > 12:
    ind_erro = 1

if ind_erro == 0:
    if dia > dd[mes]:
        ind_erro = 1

if ind_erro == 1:
    print("Data inválida.")
else:
    print(f"{dia:02d}/{mes:02d}/{ano:04d} é uma data válida.")