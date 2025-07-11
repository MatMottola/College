print("Exemplo de pesquisa binária")

      #1,2,3,4,5, 6, 7, 8, 9,10,11,12,13,14,15,16]  #Ordem em forma Humana
seq = [1,2,3,4,5,11,12,13,14,15,20,21,22,23,24,25]
      #0,1,2,3,4,5,  6, 7, 8, 9,10,11,12,13,14,15]  #Ordem em forma de computador
      

min = 0
max  = len(seq) - 1         #A lista começa do zero, então o último índice é o tamanho - 1
meio = 0 

num = int(input("Digite o número a ser pesquisado: "))
achou = 0

while min <= max and achou == 0:            
    meio = (min+max) // 2
    if num == seq[meio]:
        achou = 1
    else:
        if num < seq[meio]:
            max = meio - 1
        else:
            min = meio + 1

if achou == 1:
    print("Número encontrado na posição:", meio + 1)
else:
    print("Número", num, "não encontrado na sequência.")
print("Fim da pesquisa binária")