#Calcula a data futura para uma quantidade de dias informada.

dd=[0,31,28,31,30,31,30,31,31,30,31,30,31]
dia=mes=ano=0

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mes: "))
ano = int(input("Digite o ano: "))
qt_dias = int(input ('digite qtde. de dias p/ avançar a data: '))
pdia, pmes, pano = dia, mes, ano
dia = dia + qt_dias

if ano % 4 == 0  and ano % 100 != 0 or ano % 400 == 0:
	dd[2] = 29
else:
	dd[2] = 28
while dia > dd[mes]:
	dia = dia - dd[mes]
	mes = mes + 1
	if mes > 12:
		mes = 1
		ano = ano + 1
		if ano % 4 == 0  and ano % 100 != 0 or ano % 400 == 0:
			dd[2] = 29
		else:
			dd[2] = 28 

print ("{} dias a partir de {}/{}/{} ".format (qt_dias,pdia,pmes,pano))
print (" Resulta na data {}/{}/{}".format (dia,mes,ano))