# Muitos professores preferem adotar modelos diferentes de provas quando dão aulas para turmas muito grandes.
# Por essa razão, a escola de inglês JoWell Sant’ana, em que todas as turmas são compostas por 50 alunos,
# solicitou que você criasse um sistema capaz de atender ao seguinte requisito:
# o professor deve digitar primeiro as notas dos 25 alunos que têm número ímpar na chamada(1, 3, 5..., 47, 49)
# e depois as notas dos 25 alunos que têm número par(2, 4, 6..., 48, 50).
#  O sistema deve calcular e exibir a média de cada uma das metades da sala e informar, ao final, qual delas teve a maior nota.
# Há ainda um pedido especial do mantenedor: para que os professores não se confundam, ao digitar cada uma das notas deve ser exibida uma mensagem no seguinte padrão:
# VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES(ou ímpares, quando for o caso).
# POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO x.


print("\n \n ")
print("Olá, Seja bem vindo!")
print("\n \n ")

pares = []
impares = []


print("----------VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS IMPARES----------")

for y in range(1, 50, 2):
    impares.append(input(f"POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {y}: "))


print("----------VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES----------")

for i in range(2, 52, 2):
    pares.append(input(f"POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {i}: "))

print("----------------------------------MEDIA--------------------------------------------")


totalPar = 0
mediaPar = 0
for z in range(0, 25, 1):

    totalPar += float(pares[z])

mediaPar = totalPar / 25

print(f"A média dos alunos que tem o número par é de: {mediaPar:.2f}")


totalImpar = 0
mediaImpar = 0
for h in range(0, 25, 1):

    totalImpar += float(impares[h])

mediaImpar = totalImpar / 25

print(f"A média dos alunos que tem o número impar é de: {mediaImpar:.2f}")


print("\n \n ")

print("----------------------------------RESULTADO--------------------------------------------")

if mediaImpar > mediaPar:
    print("A média dos alunos impares é maior do que a média dos alunos pares ")
elif mediaPar > mediaImpar:
    print("A média dos alunos pares é maior do que a média dos alunos impares ")
else:
    print("A média dos alunos impares e a média dos alunos pares são as mesmas ")


print("\n \n ")
