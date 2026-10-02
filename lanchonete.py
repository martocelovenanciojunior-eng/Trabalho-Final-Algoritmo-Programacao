nome = input("Qual o seu nome? ")
print(f"Olá, {nome}! Bem-vindo ao nosso sistema de atendimento.")

total = 0
continuar = 1
while continuar == 1:

    print("CARDÁPIO")
    print("1 - X-Burger - R$ 18.00")
    print("2 - X-Salada - R$ 20.00")
    print("3 - Batata Frita - R$ 12.00")
    print("4 - Refrigerante - R$ 7.00")
    print("5 - Suco - R$ 8.00")

    codigo = int(input("Digite o código do item que deseja pedir (1-5): "))

    if codigo == 1:
        produto = "X-Burger"
        preco = 18.00

    elif codigo == 2:
        produto = "X-Salada"
        preco = 20.00

    elif codigo == 3:
        produto = "Batata Frita"
        preco = 12.00

    elif codigo == 4:
        produto = "Refrigerante"
        preco = 7.00

    elif codigo == 5:
        produto = "Suco"
        preco = 8.00

    if codigo >= 1 and codigo <= 5:
        quantidade = int(input("Digite a quantidade desejada do produto escolhido: "))

        subtotal = preco * quantidade

        total = total + subtotal

        print(f"Subtotal: R$ {subtotal:.2f}")

    else:
        print("Código inválido.")

    continuar = int(input("Deseja adicionar mais itens ao pedido? (1 - sim, 2 - não): "))


print(f"Valor original da compra: R$ {total:.2f}")

if total < 50:
    percentual = 0
    valor_final = total

elif total < 100:
    percentual = 5
    valor_final = total * 0.95

else:
    percentual = 10
    valor_final = total * 0.90

valor_desconto = total - valor_final


pagamento = 0

while pagamento < 1 or pagamento > 3:
    print("FORMAS DE PAGAMENTO")
    print("1 - Dinheiro")
    print("2 - PIX")
    print("3 - Cartão")

    pagamento = int(input("Qual a forma de pagamento: "))

    if pagamento < 1 or pagamento > 3:
        print("Opção inválida. Tente novamente.")


if pagamento == 1:
    forma_pagamento = "Dinheiro"

elif pagamento == 2:
    forma_pagamento = "PIX"

else:
    forma_pagamento = "Cartão"


print("RESUMO DO PEDIDO")
print("Cliente:", nome)
print("Valor original: R$", ("%.2f" % total))
print("Desconto aplicado:", percentual, "%")
print("Valor do desconto: R$", ("%.2f" % valor_desconto))
print("Valor final: R$", ("%.2f" % valor_final))
print("Forma de pagamento:", forma_pagamento)