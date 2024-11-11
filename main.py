import os
import time

modelo_carro = []
consumo = []

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def contagem_regressiva():
    for tempo in range(5, 0, -1):
        print(f'Encerrando programa em {tempo} segundo(s).', end='\r')
        time.sleep(1)
    print(' ' * 50)  # Limpa a linha

def encerrar_programa():
    limpar_terminal()
    contagem_regressiva()
    print('PROGRAMA ENCERRADO.\n')
    exit()

def entrada_float(prompt):
    while True:
        entry = input(prompt)
        try:
            if ',' in entry:
                entry = entry.replace(',', '.')
            return float(entry)
        except ValueError:
            print('Digite apenas números válidos.')

def entrada_inteira(prompt):
    while True:
        entry = input(prompt)
        try:
            return int(entry)
        except ValueError:
            print("Digite um número inteiro válido.")

def nome_veiculo(prompt):
    while True:
        entry = input(prompt).strip()
        if not entry or len(entry) > 50:
            print('Nome inválido. Tente novamente.')
            continue
        return entry

def choice():
    while True:
        resposta = entrada_inteira("Digite 1 para SIM ou 2 para NÃO: ")
        if resposta in [1, 2]:
            return resposta
        print('Opção inválida. Tente novamente.')

def cadastrar_veiculo():
    limpar_terminal()
    modelo_carro.append(nome_veiculo('Nome do veículo: '))
    consumo.append(entrada_float('Consumo do veículo (km/l): '))
    print('\nVEÍCULO CADASTRADO COM SUCESSO.')
    return novo_veiculo()

def novo_veiculo():
    print('Deseja cadastrar um novo veículo?')
    if choice() == 1:
        return cadastrar_veiculo()
    else:
        return ao_finalizar()

def listar_veiculos():
    limpar_terminal()
    if not modelo_carro:
        print("Nenhum veículo cadastrado.")
        return ao_finalizar()
    else:
        for idx, modelo in enumerate(modelo_carro, start=1):
            print(f"Veículo {idx}: {modelo} - Consumo: {consumo[idx-1]:.2f} KM/L")
        return novo_veiculo()

def alterar_veiculo():
    limpar_terminal()
    if not modelo_carro:
        print("Nenhum veículo cadastrado.")
        return novo_veiculo()

    for idx, modelo in enumerate(modelo_carro, start=1):
        print(f"Veículo {idx}: {modelo} - Consumo: {consumo[idx-1]:.2f} KM/L")

    veiculo_idx = entrada_inteira("\nEscolha o número do veículo para alterar: ")
    if 1 <= veiculo_idx <= len(modelo_carro):
        modelo_carro[veiculo_idx - 1] = nome_veiculo("Novo nome do veículo: ")
        consumo[veiculo_idx - 1] = entrada_float("Novo consumo (KM/L): ")
        print("Veículo alterado com sucesso.")
    else:
        print("Índice inválido.")

    return ao_finalizar()

def verificar_km():
    limpar_terminal()
    if not modelo_carro:
        print("Nenhum veículo cadastrado.")
        return novo_veiculo()

    modelo_escolhido = entrada_inteira('Escolha um modelo de carro: ')
    if 1 <= modelo_escolhido <= len(modelo_carro):
        preco = entrada_float('Preço atual do combustível: R$ ')
        valor_abastecido = entrada_float('Valor total a ser abastecido: R$ ')
        litros_abastecidos = valor_abastecido / preco
        km_final = consumo[modelo_escolhido-1] * litros_abastecidos
        print(f'\nModelo: {modelo_carro[modelo_escolhido-1]}')
        print(f'Rodará aproximadamente: {km_final:.2f} quilômetros com {litros_abastecidos:.2f} litros de combustível.')
        print(f'Valor abastecido: R$ {valor_abastecido:.2f}')
    else:
        print('Índice fora do permitido. [TENTE NOVAMENTE]')

    return ao_finalizar()

def ao_finalizar():
    print("\nDeseja retornar ao menu principal? Caso rejeite, o programa será finalizado.")
    if choice() == 1:
        limpar_terminal()
        return menu()
    else:
        return encerrar_programa()

def menu():
    while True:
        print("Menu Principal\n")
        opcoes = [
            'CADASTRAR VEÍCULO',
            'LISTAR VEÍCULOS',
            'ALTERAR INFORMAÇÕES DE VEÍCULO CADASTRADO',
            'VERIFICAR KM',
            'ENCERRAR PROGRAMA'
        ]
        for idx, opcao in enumerate(opcoes, start=1):
            print(f"{idx} - {opcao}")

        resposta = entrada_inteira("\nEscolha uma opção: ")
        if resposta == 1:
            cadastrar_veiculo()
        elif resposta == 2:
            listar_veiculos()
        elif resposta == 3:
            alterar_veiculo()
        elif resposta == 4:
            verificar_km()
        elif resposta == 5:
            encerrar_programa()
        else:
            limpar_terminal()
            print("Opção inválida. Tente novamente.")

def main():
    menu()

main()

