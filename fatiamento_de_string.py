#nome = input("Digite seu nome \n")
#print(len(nome)) # cont a quantidade de caracteres


# apresenta em qual caractere está ocupado na posição do modulo
#nome1= 'Victoria'

#print(f" A letra do meio do nome {nome1} é" , nome1[5])


# EXERCICIO

nome = input("Digite seu nome \n")
idade = int(input("Digite sua idade \n"))

if nome and idade:
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é ", nome[::-1])

    if ' ' in nome:
        print("Seu nome contém espaços")
    else:
        print("Seu nome não contém espaços")

    print(f"Seu nome possui {len(nome)} letras")
    print(f" A primeira letra do seu {nome[0]} é")
    print(f" A última letra do seu {nome[-1]} é")
else:
    print("Você não preencheu o nome ou idade")


