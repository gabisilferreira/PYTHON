#Crie um programa que solicite ao usuário seu nome e sua idade e exiba uma mensagem de saudação

nome= input("Escreva o seu nome: \n")
idade = int(input("Escreva sua idade \n"))

print(f'Olá, {nome}! Você tem {idade} anos')

#Peça ao usuário a largura e a altura de um retângulo e exiba o resultado no formato

numero = 9
print('Jogo de advinhação')

numero_advinhacao= int(input("Escolha um número de 1 ao 10 \n"))

if numero ==numero_advinhacao:
    print(f"Parabéns, você acertou! O número é {numero}")
elif numero> numero_advinhacao:
    print(f"Numero menor que o número surpresa. O número é {numero}")
else:
    print(f"Número maior que o número surpresa. O número é {numero}")


