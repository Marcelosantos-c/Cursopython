# Controle de Inventário Básico

def mostrar_menu():
    print("\n==== MENU ====")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Listar inventário")
    print("4. Sair")


def adicionar_item(inventario):
    nome = input("Digite o nome do item: ")
    quantidade = input("Digite a quantidade: ")

    if not quantidade.isdigit():
        print("Quantidade inválida! Digite apenas números.")
        return

    quantidade = int(quantidade)

    inventario.append({"nome": nome, "quantidade": quantidade})
    print(f"Item '{nome}' adicionado com sucesso!")


def remover_item(inventario):
    nome = input("Digite o nome do item a ser removido: ")

    for item in inventario:
        if item["nome"].lower() == nome.lower():
            inventario.remove(item)
            print(f"Item '{nome}' removido com sucesso!")
            return
    print(f"Item '{nome}' não encontrado no inventário.")


def listar_inventario(inventario):
    if not inventario:
        print("O inventário está vazio.")
    else:
        print("\n--- Inventário ---")
        for i, item in enumerate(inventario, start=1):
            print(f"{i}. {item['nome']} - Quantidade: {item['quantidade']}")


def main():
    inventario = []
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_item(inventario)
        elif opcao == "2":
            remover_item(inventario)
        elif opcao == "3":
            listar_inventario(inventario)
        elif opcao == "4":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()



                            
                            
                
        
        
        
        
