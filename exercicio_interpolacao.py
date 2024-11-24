produto = input("Digite o produto a ser vendido:\n")
preco = float(input("Digite o valor do produto:\n"))
forma_pagamento = int(input(
    "Digite a forma de pagamento:\n"
    "1 - Cartão de crédito\n"
    "2 - Cartão de débito ou Pix\n"
    "3 - Dinheiro\n"
))

match forma_pagamento:
    case 1:
        desconto = 0.30  # 30% de desconto
        preco -= preco * desconto
        print(f"O produto é {produto}, e o valor total com desconto é de R$ {preco:.2f}")
    case 2:
        desconto_pix = 0.10  # 10% de desconto
        preco -= preco * desconto_pix
        print(f"O produto é {produto}, e o valor total com desconto é de R$ {preco:.2f}")
    case 3:
        desconto = 0.05  # 5% de desconto
        preco -= preco * desconto
        print(f"O produto {produto} sai ao valor com desconto de R$ {preco:.2f}")
    case _:
        print("Forma de pagamento inválida. Tente novamente.")
