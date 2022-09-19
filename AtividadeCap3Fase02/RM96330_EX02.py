# Os alunos da sua turma fizeram uma votação para escolher qual dia da semana é o melhor para a realização das lives.
# Desenvolva um programa em que o usuário informe a quantidade de votos que cada um dos 5 dias da semana
#  (segunda-feira, terça-feira, quarta-feira, quinta-feira e sexta-feira)
#  obtiveram, verifique e exiba qual dia foi o escolhido.


print("\n \n ")
print("Olá, Seja bem vindo!")
print("\n \n ")

controle = 0

while controle < 5:
    print("Informe a quantidade de votos para cada dia da semana: ")
    print("\n  ")

    segunda = int(input("Informe a quantidade de votos para segunda-feira: "))
    controle += 1
    terca = int(input("Informe a quantidade de votos para terca-feira: "))
    controle += 1
    quarta = int(input("Informe a quantidade de votos para quarta-feira: "))
    controle += 1
    quinta = int(input("Informe a quantidade de votos para quinta-feira: "))
    controle += 1
    sexta = int(input("Informe a quantidade de votos para sexta-feira: "))
    controle += 1
    print("\n \n ")

print("--------------------------------resultado---------------------------------")
print("\n \n ")

# segunda
if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    print(
        f"O melhor dia para realizar as lives é segunda, o dia teve {segunda} votos")
elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
    print(
        f"O melhor dia para realizar as lives é terça, o dia teve {terca} votos")
elif quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta:
    print(
        f"O melhor dia para realizar as lives é quarta, o dia teve {quarta} votos")
elif quinta > segunda and quinta > terca and quinta > quarta and quinta > sexta:
    print(
        f"O melhor dia para realizar as lives é quinta, o dia teve {quinta} votos")
elif sexta > segunda and sexta > terca and sexta > quarta and sexta > quinta:
    print(
        f"O melhor dia para realizar as lives é sexta, o dia teve {sexta} votos")
elif segunda == terca or segunda == quarta or segunda == quinta or segunda == sexta or terca == segunda or terca == quarta or terca == quinta or terca == sexta or quarta == segunda or quarta == terca or quarta == quinta or quarta == sexta or quinta == segunda or quinta == terca or quinta == quarta or quinta == sexta or sexta == segunda or sexta == terca or sexta == quarta or sexta == quinta:
    print(
        "Existe um empate, realize novamente a votação!!! ")

print("\n \n ")
