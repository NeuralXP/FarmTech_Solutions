import math
import subprocess
import sys
import pandas as pd   # Importação do pandas já no início

# Lista global para armazenar dados do plantio
dados = []

# Função para exportar os dados para CSV
def exportar_csv():
    global dados
    if not dados:
        print("Não há dados para exportar.")
        return
    # Verifica se a estrutura da lista está correta (múltiplo de 4)
    if len(dados) % 4 != 0:
        print("Estrutura de dados inválida.")
        return

    registros = []
    # Cada 4 elementos correspondem a um registro
    for i in range(0, len(dados), 4):
        registro = {
            "cultura": dados[i],
            "area": dados[i+1],
            "tipo_insumo": dados[i+2],
            "qnt_insumo": dados[i+3]
        }
        registros.append(registro)
    
    df = pd.DataFrame(registros)
    df.to_csv("dados_plantio.csv", index=False)
    print("Dados exportados com sucesso para 'dados_plantio.csv'")

# Funções para cálculos de insumos
def insumos_milho(area: float):
    litros_insumo_por_m2 = 100  # Quantidade de insumo por metro quadrado
    tipo_insumo = "Fertilizante"  # Tipo de insumo utilizado
    qnt_insumo = area * float(litros_insumo_por_m2)  # Cálculo da quantidade total de insumo
    return qnt_insumo, tipo_insumo

def insumos_soja(area: float):
    litros_insumo_por_m2 = 600  # Quantidade de insumo por metro quadrado
    tipo_insumo = "Fosfato"  # Tipo de insumo utilizado
    qnt_insumo = area * float(litros_insumo_por_m2)  # Cálculo da quantidade total de insumo
    return qnt_insumo, tipo_insumo

# Função para obter e armazenar os dados do plantio
def informar_dados():
    global dados
    print("Selecione o tipo de cultura: ")
    opcao = input("Milho (1) ou Soja (2)? ").strip()

    # Identificação da cultura e cálculo da área
    match opcao.lower():
        case "1" | "milho" | "Milho":
            comprimento = float(input("Um plantio de Milho irá necessitar um terreno retangular. \nQual o Comprimento de sua futura plantação de Milho? "))
            if comprimento <= 0:
                print("Volte a nós quando possuir uma terra para plantio !!!")
                return
            largura = float(input("Qual a Largura de sua futura plantação de Milho? "))
            if largura <= 0:
                print("Volte a nós quando possuir uma terra para plantio !!!")
                return
            cultura = "Milho"
            area = comprimento * largura
            qnt_insumo, tipo_insumo = insumos_milho(area)

        case "2" | "soja" | "Soja":
            info_soja = input("Um plantio de Soja irá necessitar um terreno circular. \nQual informação do seu terreno o Sr./Sr.a tem? \n1- Diâmetro \n2- Circunferência \n").strip().lower()

            # Cálculo do raio com base na entrada do usuário
            if info_soja in ["diametro", "diâmetro", "1", "Diametro", "Diâmetro"]:
                d = float(input("Digite o diâmetro: "))
                raio = d / 2
            elif info_soja in ["circunferência", "circunferencia", "2", "Circunferência", "Circunferencia"]:
                c = float(input("Digite a circunferência: "))
                raio = c / (2 * math.pi)
            else:
                print("Opção Inválida")
                return

            cultura = "Soja"
            area = math.pi * (raio ** 2)  # Área de um círculo: πr²
            qnt_insumo, tipo_insumo = insumos_soja(area)
            
        case _:
            print("Opção Inválida")
            return

    # Armazenamento dos dados coletados   
    dados.append(cultura)
    dados.append(area)
    dados.append(tipo_insumo)
    dados.append(qnt_insumo)
    print(f"Os dados do seu plantio foram armazenados com sucesso!")
    back_to_menu()

# Outras funções (resgatar_dados, alterar_dados, etc.)
def resgatar_dados():
    if dados:
        print(f"Dados do plantio: \nCultura: {dados[0]} \nArea: {dados[1]:.2f} m² \nTipo de insumo: {dados[2]} \nQuantidade de insumos: {dados[3]:.2f} litros/m² ")
    else:
        print("Nenhum dado armazenado ainda!")
    back_to_menu()

def alterar_dados():
    global dados
    if dados:
        print("Selecione o dado que deseja atualizar: \n1- Cultura \n2- Área \n3- Tipo de insumo \n4- Quantidade de insumos")
        opcao_menu = input("Digite a opção desejada: ").strip()
        if opcao_menu in ["1", "cultura", "Cultura"]:
            alterar_cultura()
        elif opcao_menu in ["2", "area", "área", "Area", "Área"]:
            alterar_area()
        elif opcao_menu in ["3", "tipo de insumo", "Tipo de insumo"]:
            alterar_tipo_insumo()
        elif opcao_menu in ["4", "quantidade de insumos", "Quantidade de insumos"]:
            alterar_qnt_insumos()
        else:
            print("Opção Inválida! Tente novamente.")
            alterar_dados()
    else:
        print("Não há dados para atualizar!")
    back_to_menu()

def alterar_cultura():
    global dados
    if dados[0] == "Milho":
        cultura = "Soja"
        print("O tipo de cultura atual é o Milho e será alterado para Soja!")
        print("Para a cultura de soja, será necessária uma área de plantio circular!")
        manter_area = input(f"Deseja manter a área atual de {dados[1]:.2f} m²? (s/n)").strip()
        if manter_area in ["s", "S"]:
            qnt_insumos, tipo_insumo = insumos_soja(dados[1])
        elif manter_area in ["n", "N"]:
            raio = float(input("Informe o raio da área de plantio: "))
            area = math.pi * (raio ** 2)
            qnt_insumos, tipo_insumo = insumos_soja(area)
            dados[1] = area
        else:
            print("Opção inválida")
            alterar_cultura()
    elif dados[0] == "Soja":
        cultura = "Milho"
        print("O tipo de cultura atual é o Soja e será alterado para Milho!")
        print("Para a cultura de milho, será necessária uma área de plantio retangular!")
        manter_area = input(f"Deseja manter a área atual de {dados[1]:.2f} m²? (s/n)").strip()
        if manter_area in ["s", "S"]:
            qnt_insumos, tipo_insumo = insumos_milho(dados[1])
        elif manter_area in ["n", "N"]:
            comprimento = float(input("Um plantio de Milho irá necessitar um terreno retangular. \nQual o Comprimento de sua futura plantação de Milho? "))
            largura = float(input("Qual a Largura de sua futura plantação de Milho? "))
            area = comprimento * largura
            qnt_insumos, tipo_insumo = insumos_milho(area)
            dados[1] = area
        else:
            print("Opção inválida")
            alterar_cultura()

    dados[0] = cultura
    dados[2] = tipo_insumo
    dados[3] = qnt_insumos
    print("Dados atualizados com sucesso!")
    back_to_menu()

def alterar_area():
    global dados
    if dados[0] == "Milho":
        comprimento = input("Informe o comprimento da área de plantio: ").strip()
        largura = input("Informe a largura da área de plantio: ").strip()
        area = float(comprimento) * float(largura)
        qnt_insumos, tipo_insumo = insumos_milho(area)
    elif dados[0] == "Soja":
        raio = input("Informe o raio da área de plantio: ").strip()
        area = math.pi * (float(raio) ** 2)
        qnt_insumos, tipo_insumo = insumos_soja(area)
    dados[1] = area
    dados[2] = tipo_insumo
    dados[3] = qnt_insumos
    print("Dados atualizados com sucesso!")
    back_to_menu()

def alterar_tipo_insumo():
    global dados
    if dados[0] == "Milho":
        print("O tipo de insumo atual é o Fertilizante e será alterado para Fosfato!")
        alterar_cultura()
    elif dados[0] == "Soja":
        print("O tipo de insumo atual é o Fosfato e será alterado para Fertilizante!")
        alterar_cultura()

def alterar_qnt_insumos():
    global dados
    qnt_insumos = float(input("Informe a quantidade de insumos utilizada em Litros: "))
    if dados[0] == "Milho":
        litros_insumos_por_m2 = 100
        area = qnt_insumos / litros_insumos_por_m2
    elif dados[0] == "Soja":
        litros_insumos_por_m2 = 600
        area = qnt_insumos / litros_insumos_por_m2
    dados[1] = area
    dados[3] = qnt_insumos
    print("Dados atualizados com sucesso!")
    back_to_menu()

def deletar_dados():
    global dados
    if dados:
        dados.clear()
        print("Todos os dados foram deletados!")
    else:
        print("Não há dados armazenados para deletar.")
    back_to_menu()

# Função para consultar a API e obter a previsão do tempo
def consultar_previsao_tempo():
    try:
        resultado = subprocess.run(['Rscript', 'previsao_do_tempo.r'], capture_output=True, text=True)
        print("== Previsão do Tempo ==")
        print(resultado.stdout)
    except FileNotFoundError:
        print('Erro: Certifique-se de que o arquivo "previsao_do_tempo.r" está no mesmo diretório.')

# Função para consultar as estatísticas básicas (invoca exportar_csv e executa o script R)
def consultar_estatisticas_basicas():
    exportar_csv()
    try:
        resultado = subprocess.run(['Rscript', 'estatisticas_basicas.r'], capture_output=True, text=True)
        print("== Estatísticas Básicas Calculadas pelo R ==")
        print(resultado.stdout)
    except FileNotFoundError:
        print('Erro: Certifique-se que o arquivo "estatisticas_basicas.r" está no mesmo diretório.')

# Função principal do menu de opções
def menu():
    while True:
        print("\n1- Informar Dados")
        print("2- Resgatar Dados")
        print("3- Alterar Dados")
        print("4- Deletar Dados")
        print("5- Sair")
        print("6- Consultar Previsão do Tempo")
        print("7- Consultar Estatísticas Básicas")
        escolha = input("Escolha uma opção: ").strip().lower()

        if escolha in ["1", "informar dados", "2", "resgatar dados", "3", "alterar dados",
                       "4", "deletar dados", "5", "sair", "6", "consultar previsão do tempo",
                       "7", "consultar estatísticas básicas", "consultar estatisticas básicas"]:
            match escolha:
                case "1" | "informar dados":
                    informar_dados()
                case "2" | "resgatar dados":
                    resgatar_dados()
                case "3" | "alterar dados":
                    alterar_dados()
                case "4" | "deletar dados":
                    deletar_dados()
                case "5" | "sair":
                    print("Saindo...")
                    sys.exit()
                case "6" | "consultar previsão do tempo":
                    print("Consultando previsão do tempo...")
                    consultar_previsao_tempo()
                case "7" | "consultar estatísticas básicas" | "consultar estatisticas básicas":
                    print("Consultando estatísticas básicas...")
                    consultar_estatisticas_basicas()
        else:
            print("Opção Inválida! Tente novamente.")

def back_to_menu():
    while True:
        voltar = input("Deseja voltar ao menu? (s/n) ").strip().lower()
        if voltar == "s":
            menu()
        elif voltar == "n":
            print("Saindo...")
            sys.exit()
        else:
            print("Opção inválida! Tente novamente.")
            continue

# Início do programa
menu()

