import random

def lancar_moeda():
    opcoes = ['Cara', 'Coroa']
    
    resultados = []
    
    while True:
        resultado = random.choice(opcoes)
        
        print(f"O resultado do lançamento foi: {resultado}")
        
        resultados.append(resultado)
        
        continuar = input("Deseja lançar a moeda novamente? (s/n): ").lower()
        
        if continuar != 's':
            break
    
    print("\nLista de resultados:")
    print(resultados)

lancar_moeda()