tipoCliente = input("digite premium gold padrao")

if tipoCliente == "premium":

    print("cliente premium")
else:

    if tipoCliente == "gold":
        print("cliente gold")

    else:
        print("cliente padrao")

pesoMala = float(input("digite peso da mala"))

limite = 100

if pesoMala > limite and tipoCliente == "premium":
    print("Pode passar")
else:
    if pesoMala > limite and tipoCliente == "gold":
        print("Pode passar")
    else:
        print("tem que pagar")
