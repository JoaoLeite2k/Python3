import random

gameOn = True
listaPalavras = []
contador = 1
letraAcertada = 0


while gameOn:
    print("Quantas palavras haverá na lista?")
    nmrDePalavras = int(input("-->> "))
    for i in range (nmrDePalavras):
        palavra = str(input("{}a palavra: ".format(contador)))
        contador +=1
        listaPalavras.append(palavra)
    print("\nLista criada")
    palavraAleatoria = random.choice(listaPalavras)
    print("Palavra selecionada: {}".format(palavraAleatoria))

    nmrTentativas = int(input("\nDigite o número de tentativas: "))

    while nmrTentativas != "0":
        letras = len(palavraAleatoria)
        print("Palavra selecionada, ela contem {} letras.\n".format(letras))

        #solicitar chute
        print("Chute uma letra.")
        chute = str(input("-->>"))

        for i in palavraAleatoria:
            if chute == i:
                print("Voce acertou a letra.")

                letraAcertada +=1

                if letraAcertada ==  letras:
                    print("Voce venceu o jogo!")

                    break

            else:
                print("Voce errou a letra.")
            nmrTentativas -=1


    gameOn = False