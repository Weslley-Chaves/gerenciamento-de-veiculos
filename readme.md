
# Sistema de Gerenciamento de Veículos

Este projeto é uma aplicação de terminal em Python para cadastrar, listar, alterar informações e calcular a autonomia de veículos a partir do consumo de combustível e valor abastecido. O objetivo é fornecer uma ferramenta de fácil uso para gerenciar dados de veículos e realizar cálculos de distância baseados no consumo.

## Funcionalidades
*  **Cadastro de Veículos**: Adiciona um novo veículo com nome e consumo (km/l).
*  **Listagem de Veículos**: Exibe todos os veículos cadastrados com seus respectivos consumos.
*  **Alteração de Informações**: Permite alterar o nome e o consumo de um veículo existente.
*  **Cálculo de Distância**: Calcula a quilometragem que um veículo pode percorrer com base no valor abastecido e no preço do combustível.
*  **Sistema de Navegação**: Menu interativo com opções para o usuário navegar pelo sistema.

## Estrutura do Código

O código principal consiste nas seguintes funções:

* `limpar_terminal()`: Limpa o terminal para uma melhor visualização.
* `contagem_regressiva()`: Exibe uma contagem regressiva ao encerrar o programa.
* `entrada_float()` e `entrada_inteira()`: Lê e valida entradas numéricas do usuário, garantindo que os dados fornecidos sejam números.
* `nome_veiculo()`: Lê e valida o nome do veículo, limitando o tamanho a 50 caracteres.
* `choice()`: Função para obter confirmações simples (1 para sim, 2 para não).
* `cadastrar_veiculo()`, `listar_veiculos()`, `alterar_veiculo()`, `verificar_km()`: Funções principais para adicionar, exibir, alterar veículos e calcular a distância estimada.
* `menu()`: Exibe o menu principal do programa.
* `main()`: Função principal que inicia a execução do programa.

## Requisitos

Para rodar o código, é necessário:

* Python 3.x
* Biblioteca `os` e `time` (já incluídas nas versões padrão do Python)

## Como Usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd nome-do-repositorio
   ```

3. Execute o programa:
   ```bash
   python nome_do_arquivo.py
   ```

4. Siga as instruções no terminal para navegar pelo menu e utilizar as funcionalidades.

## Estrutura do Menu

*  **1 - CADASTRAR VEÍCULO**: Adiciona um novo veículo com o nome e consumo.
*  **2 - LISTAR VEÍCULOS**: Exibe todos os veículos cadastrados e seus consumos.
*  **3 - ALTERAR INFORMAÇÕES DE VEÍCULO**: Permite editar os dados de um veículo já cadastrado.
*  **4 - VERIFICAR KM**: Calcula quantos quilômetros o veículo pode percorrer com o valor de combustível especificado.
*  **5 - ENCERRAR PROGRAMA**: Finaliza a aplicação com uma contagem regressiva.

## Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do repositório.
2. Crie uma nova branch para suas modificações.
3. Envie um pull request.

## Licença

Este projeto é licenciado sob a MIT License. Veja o arquivo [LICENSE]() para mais detalhes.
