# Constantes para as opções do menu
ADICIONAR_TAREFA = 1
VISUALIZAR_TAREFAS = 2
MARCAR_TAREFA_COMO_CONCLUIDA = 3
REMOVER_TAREFA = 4
ENCERRAR_PROGRAMA = 5

def exibir_menu():
    """Exibe o menu de opções."""
    # Imprime as opções do menu
    print("\nBem-vindo ao Gerenciador de Tarefas!")
    print(f"{ADICIONAR_TAREFA}. Adicionar uma nova tarefa")
    print(f"{VISUALIZAR_TAREFAS}. Visualizar todas as tarefas")
    print(f"{MARCAR_TAREFA_COMO_CONCLUIDA}. Marcar uma tarefa como concluída")
    print(f"{REMOVER_TAREFA}. Marcar uma tarefa como removida")
    print(f"{ENCERRAR_PROGRAMA}. Sair do programa")

def adicionar_tarefa(tarefas):
    """Adiciona uma nova tarefa."""
    # Solicita ao usuário a nova tarefa
    tarefa = input("Insira a nova tarefa que deseja adicionar: ")
    # Verifica se a tarefa já existe
    if tarefa not in tarefas:
        # Adiciona a tarefa
        tarefas[tarefa] = {"concluida": False, "removida": False}
        print("Tarefa adicionada com sucesso!")
    else:
        print("Esta tarefa já existe na sua lista.")

def visualizar_tarefas(tarefas):
    """Visualiza todas as tarefas."""
    # Verifica se existem tarefas
    if tarefas:
        print("Aqui estão todas as suas tarefas:")
        # Imprime todas as tarefas e seus status
        for i, (tarefa, info) in enumerate(tarefas.items(), start=1):
            status = []
            if info["concluida"]:
                status.append("(concluída)")
            if info["removida"]:
                status.append("(removida)")
            print(f"{i}. {tarefa} {' '.join(status)}")
    else:
        print("Sua lista de tarefas está vazia.")

def marcar_tarefa_como_concluida(tarefas):
    """Marca uma tarefa como concluída."""
    # Solicita ao usuário a tarefa a ser concluída
    tarefa_concluida = input("Insira a tarefa que deseja marcar como concluída: ")
    # Verifica se a tarefa existe
    if tarefa_concluida in tarefas:
        # Verifica o status da tarefa
        if tarefas[tarefa_concluida]["concluida"]:
            print("Esta tarefa já foi marcada como concluída.")
        elif tarefas[tarefa_concluida]["removida"]:
            print("Esta tarefa foi removida e não pode ser marcada como concluída.")
        else:
            # Marca a tarefa como concluída
            tarefas[tarefa_concluida]["concluida"] = True
            print("Tarefa marcada como concluída com sucesso!")
    else:
        print("Tarefa não encontrada. Por favor, insira uma tarefa válida.")

def remover_tarefa(tarefas):
    """Marca uma tarefa como removida."""
    # Solicita ao usuário a tarefa a ser removida
    tarefa_removida = input("Insira a tarefa que deseja marcar como removida: ")
    # Verifica se a tarefa existe
    if tarefa_removida in tarefas:
        # Verifica o status da tarefa
        if tarefas[tarefa_removida]["removida"]:
            print("Esta tarefa já foi marcada como removida.")
        elif tarefas[tarefa_removida]["concluida"]:
            print("Esta tarefa foi concluída e não pode ser marcada como removida.")
        else:
            # Marca a tarefa como removida
            tarefas[tarefa_removida]["removida"] = True
            print("Tarefa marcada como removida com sucesso!")
    else:
        print("Tarefa não encontrada. Por favor, insira uma tarefa válida.")

def encerrar_programa():
    """Encerra o programa."""
    # Imprime a mensagem de encerramento
    print("O programa está sendo encerrado. Obrigado por usar o Gerenciador de Tarefas!")

def main():
    """Função principal que executa o programa."""
    # Inicializa a lista de tarefas
    tarefas = {}

    # Loop principal do programa
    while True:
        # Exibe o menu
        exibir_menu()
        try:
            # Solicita ao usuário a opção do menu
            opcao = int(input("Escolha uma opção do menu: "))

            # Executa a opção escolhida
            if opcao == ADICIONAR_TAREFA:
                adicionar_tarefa(tarefas)
            elif opcao == VISUALIZAR_TAREFAS:
                visualizar_tarefas(tarefas)
            elif opcao == MARCAR_TAREFA_COMO_CONCLUIDA:
                marcar_tarefa_como_concluida(tarefas)
            elif opcao == REMOVER_TAREFA:
                remover_tarefa(tarefas)
            elif opcao == ENCERRAR_PROGRAMA:
                encerrar_programa()
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida do menu.")
        except ValueError:
            print("Por favor, insira um número para escolher a opção.")

# Executa a função principal se o script for executado diretamente
if __name__ == "__main__":
    main()