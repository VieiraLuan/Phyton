# Você foi procurado por um aluno do curso de Produção Multimídia do FIAP ON para desenvolver um trabalho em parceria:
# um serviço em que as pessoas possam usar um estúdio profissional para gravar seus vídeos para o YouTube com máxima qualidade.
# O serviço ganha dinheiro por meio de um sistema de assinaturas e de um bônus calculado por uma porcentagem sobre o faturamento que o canal do cliente obteve ao longo do ano.
# Sua tarefa é criar um algoritmo que receba o tipo de assinatura do cliente, o faturamento anual dele e que calcule e exiba qual o valor do bônus que o cliente deve pagar a vocês. A tabela abaixo mostra a porcentagem de acordo com cada nível de assinatura:

print("Olá, Seja bem vindo!")

controle = 1

while controle == 1:
    print("Os niveis de clientes são: \n \n  Basic, Silver, Gold e Platinum ")

    nivel = input(" \n Informe o tipo de assinatura: ").upper()
    faturamento = input("Informe o faturamento: ")

    if nivel == 'BASIC':
        bonus = float(faturamento) * 0.30
        print(f"O nível do cliente é {nivel} e ele deve pagar: R${bonus:.2f}")
        controle = 0
    elif nivel == 'SILVER':
        bonus = float(faturamento) * 0.20
        print(f"O nível do cliente é {nivel} e ele deve pagar: R${bonus:.2f}")
        controle = 0
    elif nivel == 'GOLD':
        bonus = float(faturamento) * 0.10
        print(f"O nível do cliente é {nivel} e ele deve pagar: R${bonus:.2f}")
        controle = 0
    elif nivel == 'PLATINUM':
        bonus = float(faturamento) * 0.05
        controle = 0
        print(f"O nível do cliente é {nivel} e ele deve pagar: R${bonus:.2f}")
    else:
        print("Digite um valor válido !!! Por favor informe o tipo de assinatura: ")


print("fim")
