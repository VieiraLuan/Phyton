print("Esse programa calcula a velocidade média de um patinete")
distancia = input("Qual foi a distância em metros percorrida pelo patinete? ")
tempo = input(
    "Quantos minutos o patinete demorou para percorrer essa distância? ")
velocidade_media = float(distancia) / float(tempo)
print(
    "O patinete atingiu uma velocidade media de {0:.2f}  km/hora".format(velocidade_media*0.06))
