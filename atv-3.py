def exibir_menu():
    print(f"\nMenu de Gerenciamento de Eventos")
    print("1. Adicionar um novo evento")
    print("2. Remover um evento")
    print("3. Sair")
    opcao = int(input(f"\nEscolha uma opção (1-3): "))
    return opcao

def exibir_eventos(eventos):
    if eventos:
        print(f"\nEventos agendados:")
        contador = 1
        for evento in eventos:
            print(f"{contador}. {evento}")
            contador += 1
    else:
        print(f"\nNenhum evento agendado.")

def adicionar_evento(eventos):
    novo_evento = input("\nDigite o nome do novo evento: ")
    eventos.append(novo_evento)
    print(f"\nEvento '{novo_evento}' adicionado com sucesso!")

def remover_evento(eventos):
    if not eventos:
        print(f"\nNão há eventos para remover.")
        return
    exibir_eventos(eventos)
    posicao = int(input(f"\nQual a posição do evento a remover? "))
    
    # Verificando a posição
    if posicao > 0:
        try:
            evento_removido = eventos[posicao - 1]  # Ajustando para zero-index
            eventos.remove(evento_removido)
            print(f"\nEvento '{evento_removido}' removido com sucesso!")
        except IndexError:
            print(f"\nPosição inválida.")
    else:
        print(f"\nPosição inválida.")

def main():
    eventos = ["Reunião com a equipe", "Almoço com cliente", "Consulta médica"]
    
    while True:
        exibir_eventos(eventos)
        opcao = exibir_menu()

        if opcao == 1:
            adicionar_evento(eventos)
        elif opcao == 2:
            remover_evento(eventos)
        elif opcao == 3:
            print(f"\nSaindo do programa...")
            break
        else:
            print(f"\nOpção inválida! Tente novamente.")

main()
