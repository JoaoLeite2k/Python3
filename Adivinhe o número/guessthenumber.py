# Adivinhe o número
import random

venceu = False

fimdejogo = False

def escolherNumAleatorio():
	print("Número máximo de opções: ")
	numMax = int(input("-> "))
	print("Escolhendo um número aleatório entre 1 e {}...".format(numMax))

	nmrEscolhido = random.randrange(1, numMax)

	print(nmrEscolhido)
	return nmrEscolhido

def gameOn(nmrselecionado):

	tentativas = 5
	jogoOn = True


	while jogoOn:

		print("Você possui {} tentativas.".format(tentativas))
		print("Tenta adivinhar o número selecionado.")
		chute = int(input("->> "))

		tentativas -= 1

		if chute == nmrselecionado:
			print("Acertou, você venceu. \n")
			jogoOn = False

		elif tentativas == "0":
			jogoOn = False
			print("Você está sem mais tentativas, você perdeu. \n")

		else:
			print("Errou, tente outra vez. \n")


nmrselecionado = escolherNumAleatorio()

gameOn(nmrselecionado)

