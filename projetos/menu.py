def menu():
    opcao =input('''
    ==============================================
                   Filipe Topbarber
    O que você deseja fazer?:
    [1]marcar horário
    [2]listar horários marcados
    [3]desmarcar horário
    [4]sair
    ==============================================
    Escolha uma opção acima:               
    ''')
    return print(opcao)

def main():
    menu()

main()