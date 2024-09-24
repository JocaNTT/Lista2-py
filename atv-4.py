import random

def jogo_palavras():
    animais = ['leão', 'tigre', 'elefante', 'girafa', 'zebra', 'macaco', 'panda', 'hipopotamo', 'leopardo', 'canguru', 'urso', 'coelho', 'cavalo', 'pinguim', 'lobo']
    
    lista_palavras = animais
    
    lista_embaralhada = lista_palavras[:]
    random.shuffle(lista_embaralhada)
    
    print("A lista começa na posição 0 e vai até 14.")

    palavra_escolhida = random.choice(lista_embaralhada)

    posicao_correta = lista_embaralhada.index(palavra_escolhida)
    
    tentativas = 3
    
    while tentativas > 0:
        print(f"\nQual é a posição da palavra '{palavra_escolhida}' na lista?")
        resposta = int(input("Digite a posição (entre 0 e 14): "))
        
        if resposta == posicao_correta:
            print("Parabéns! Você acertou!")
            break
        else:
            tentativas -= 1
            if tentativas > 0:
                print(f"Você errou. Tentativas restantes: {tentativas}")
            else:
                print(f"\nVocê errou todas as tentativas. A posição correta era {posicao_correta}.")

    print("\nLista embaralhada:", lista_embaralhada)

jogo_palavras()