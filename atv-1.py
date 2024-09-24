def ler_lista():
    lista = []
    print("Digite os números um por um (pressione Enter sem digitar nada para encerrar):")
    while True:
        entrada = input("Digite um número: ")
        if entrada == '':
            break
        # Tenta converter a entrada em um número inteiro(pesquisei sobre)
        try:
            numero = int(entrada)
            lista.append(numero)
        except:
            print("Entrada inválida. Por favor, insira um número.")
    return lista

def intersecao(lista1, lista2):
    comum = []
    for num in lista1:
        if num in lista2 and num not in comum:
            comum.append(num)
    return comum

def main():
    print("Digite os números da primeira lista:")
    lista1 = ler_lista()
    print("Digite os números da segunda lista:")
    lista2 = ler_lista()
    
    comuns = intersecao(lista1, lista2)
    
    if comuns:
        print("Números comuns em ambas as listas:", comuns)
    else:
        print("Não há números comuns entre as listas.")

main()