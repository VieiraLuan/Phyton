print("Saldão da Alegria, aqui o seu bolso sorri hahaha")


totalCompra = float(input("Digite o total da compra"))


formaPagamento = int(input("Digite 1-Cartão 2-Boleto "))

if formaPagamento == 1:
    print(f"Sem desconto {totalCompra:.2f}")
    qtdParcelas = int(input("Digite a quantidade de parcelas"))
    valorParcela = totalCompra / qtdParcelas
    print(f"O cliente irá pagar {qtdParcelas}x parcelas de {valorParcela:.2f}")
else:
    valorDescontado = totalCompra * 0.95
    print(f"Tem desconto, vai pagar apenas: R$ {valorDescontado:.2f}")
