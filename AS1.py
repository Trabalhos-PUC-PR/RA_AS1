#1)Uma P.A. (progressão aritmética) fica determinada pela sua razão (r) e pelo primeiro termo(a1). 
# Escreva um Algoritmo e, posteriormente, uma app em Python que seja capaz de determinar qualquer termo de uma P.A., dado a razão e o primeiro termo, que serão lidos do teclado.

#2)Considere que o número de uma placa de veículo é composto por quatro algarismos. Construa um Algoritmo e, posteriormente, uma app em Python que leia este número e apresente o 
#algarismo correspondente à casa das centenas.

#3)Escreva um Algoritmo que leia dois números reais e imprima a média aritmética entre esses dois valores com a seguinte mensagem “MEDIA” antes do resultado.

#4)Certo dia o professor de Johann FriederichCarl Gauss (aos 10 anos de idade) mandou que os alunos somassem os números de 1 a 100. 
# Imediatamente Gauss achou a resposta –5050 –aparentemente sem cálculos. Supõe-se que aí, Gauss, houvesse descoberto a fórmula de uma soma de uma progressão aritmética. 
# Construa uma Algoritmo e, posteriormente, uma appem Python para realizar a soma de uma P.A. de ntermos, com o primeiro a1 e o último an, sendo n, a1 e anlidos do teclado

escolha = int(input("Escolha a atividade (1-4):"))
if(escolha>4 or escolha<1):
    exit("Atividade não existente")
else:
    if(escolha==1):
        numeroInicial = int(input("Digite o valor inicial:"))
        razao = int(input("Digite a razão da PA:"))
        posicao = int(input("Digite a posição do numero:"))
        numeroProcurado = numeroInicial + (posicao - 1) * razao
        print("Seu número é:",numeroProcurado)
    if(escolha==2):
        numeroum = int(input("Digite um Número Inteiro de 4 digitos pra placa do seu carro: "))
        numerodois = numeroum/1000
        if(numerodois>=1):
            print ("O digito das centenas é: ", (numeroum//100)%10)
    if(escolha==3):
        numeroum = int(input("Digite o primeiro valor: "))
        numerodois = int(input("Digite o segundo valor: "))
        media = (numeroum + numerodois)/2
        print("MEDIA:", media)
    if(escolha==4):
        numeroum = int(input("Digite o primeiro termo da PA: "))
        numerodois = int(input("Digite o 'ultimo' termo da PA: "))
        posicao = int(input("Digite até qual posição a soma será realizada: "))
        soma = ((numeroum+numerodois)*posicao)/2
        print("A Soma da PA é",soma)
exit()
