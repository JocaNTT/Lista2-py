def main():
    notas = []
    
    while True:
        nota = float(input("Digite a nota do aluno (ou 0 para terminar): "))
        
        if nota == 0:
            break
        else:
            notas.append(nota)

    if not notas:
        print("Nenhuma nota foi inserida.")
        return

    contador = 0
    for nota in notas:
        if nota > 7:
            contador += 1
    
    print(f"Quantidade de alunos com nota acima de 7: {contador}")

main()