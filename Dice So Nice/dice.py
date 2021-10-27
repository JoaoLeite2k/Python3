import random

def rolarDado(valor):
	print('')
	print("Rodando um D{}".format(valor))
	resultado = random.randrange(1, valor)
	print("-" * 14)
	print("Resultado: {}".format(resultado))
	print("-" * 14)


while True:
	print('')
	print("Qual tipo de dado você deseja rolar?")
	print("1. D4")
	print("2. D8")
	print("3. D12")
	print("4. D20")
	print("0. Sair")

	opc = int(input("->> "))

	if (opc == 1):
		valor = 4
		rolarDado(valor)

	elif (opc == 2):
		valor = 8
		rolarDado(valor)

	elif (opc == 3):
		valor = 12
		rolarDado(valor)

	elif (opc == 4):
		valor = 20
		rolarDado(valor)


	elif (opc == 0):
		print("Saindo...")
		break

	else:
		print("Opção inválida")