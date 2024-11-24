#Crie um programa que peça ao usuário para digitar um número inteiro. 
# O programa deve usar try-except para garantir que o usuário digitou um valor válido. 
# Caso o valor não seja um número inteiro, exiba uma mensagem de erro e peça para o usuário tentar novamente.

#try :
  #  numero_int = int(input('Digite um número inteiro '))
  #  print('Sucesso')
#except:
#    print ("Valor não é um número inteiro")


#Desenvolva uma calculadora simples que peça dois números ao usuário e a operação desejada (adição, subtração, multiplicação ou divisão). 

try:
    num1 = int(input("Digite um número inteiro: "))
    num2 = int(input("Digite outro número inteiro: "))

    opcao = int(input(
        "Escolha a opção que deseja:\n"
        "1 - Soma\n"
        "2 - Subtração\n"
        "3 - Multiplicação\n"
        "4 - Divisão\n"
    ))

    match opcao:
        case 1:
            resultado = num1 + num2
            print(f"O resultado da soma entre {num1} e {num2} é {resultado}")
        case 2:
            resultado = num1 - num2
            print(f"O resultado da subtração entre {num1} e {num2} é {resultado}")
        case 3:
            resultado = num1 * num2
            print(f"O resultado da multiplicação entre {num1} e {num2} é {resultado}")
        case 4:
            try:
                resultado = num1 / num2
                print(f"O resultado da divisão entre {num1} e {num2} é {resultado:.2f}")
            except ZeroDivisionError:
                print("Erro: Não é possível dividir por zero.")
        case _:
            print("Opção inválida. Escolha um número entre 1 e 4.")
except ValueError:
    print("Erro: Certifique-se de digitar números inteiros.")
