#Busca caractere duplicado em string.

x=y=0
s= input("Digite a String")

while x < len(s) -1 :
	y=x+1
	while y < len(s):
		if s[x] == s[y]:
			print(s[x], "existe nas pos.", x + 1, "e", y + 1)
		y = y + 1
	x = x + 1
print ("FIM")