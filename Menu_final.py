import math
import subprocess
import sys

dados              =[]

def insumos_milho(area: float):
    litros_insumo_por_m2 =100
    tipo_insumo          ="Fertilizante"
    qnt_insumo           =area *float(litros_insumo_por_m2)
    return                qnt_insumo, tipo_insumo

def insumos_soja(area: float):
    litros_insumo_por_m2 =600
    tipo_insumo          ="Fosfato"
    qnt_insumo           = area *float(litros_insumo_por_m2)
    return                 qnt_insumo, tipo_insumo

def informar_dados():
    global dados
    print         ("Selecione o tipo de cultura: ")
    opcao = input ("Milho (1) ou Soja (2)? ").strip()
    match opcao.lower():
        case "1" | "milho" | "Milho":
            comprimento     =float(input("Um plantio de Milho irá necessitar um terreno retangular. \nQual o Comprimento de sua futura plantação de Milho? "))
            if comprimento <=0:
                print("Volte a nós quando possuir uma terra para plantio !!!")
                return
            
            largura     =float(input("Qual a Largura de sua futura plantação de Milho? "))
            if largura <=0:
                print("Volte a nós quando possuir uma terra para plantio !!!")
                return

            cultura ="Milho"
            area =comprimento * largura
            qnt_insumo, tipo_insumo =insumos_milho(area)
            

        case "2" | "soja" | "Soja":
            info_soja = input("Um plantio de Soja irá necessitar um terreno circular. \nQual informação do seu terreno o Sr./Sr.a tem? \n1- Diâmetro \n2- Circunferência \n").strip().lower()

            if info_soja in["diametro", "diâmetro", "1", "Diametro", "Diâmetro"]:
                d    =float(input("Digite o diâmetro: "))
                raio =d /2
            elif info_soja in ["circunferência", "circunferencia", "2", "Circunferência", "Circunferencia"]:
                c    =float(input("Digite a circunferência: "))
                raio =c /(2 * math.pi)
            else:
                print("Opção Inválida")
                return 

            cultura ="Soja"
            area =math.pi *(raio **2)
            qnt_insumo, tipo_insumo =insumos_soja(area)
            
            
        case _:
            print("Opção Inválida")
            return
        
    dados.append(cultura)
    dados.append(area)
    dados.append(tipo_insumo)
    dados.append(qnt_insumo)
    print(f"Os dados do seu plantio foram armazenados com sucesso!") 
    back_to_menu()

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
        opcao_menu =input("Digite a opção desejada: ").strip()

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
            area = math.pi *(raio **2)
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
            comprimento     =float(input("Um plantio de Milho irá necessitar um terreno retangular. \nQual o Comprimento de sua futura plantação de Milho? "))
            largura     =float(input("Qual a Largura de sua futura plantação de Milho? "))
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

def consultar_previsao_tempo():
    try:
        resultado = subprocess.run(['Rscript', 'previsao_do_tempo.r'], capture_output=True, text=True)
        print('== Previsão do Tempo ==')
        print(resultado.stdout)
    except FileNotFoundError:
        print('Erro: Certifique-se de que o arquivo "previsao_do_tempo.r" está no mesmo diretório.')


def menu():
    while True:
        print("\n1- Informar Dados \n2- Resgatar Dados \n3- Alterar Dados \n4- Deletar Dados \n5- Sair \n6- Consultar Previsão do Tempo\n")
        escolha =input("Escolha uma opção: ").strip()

        if escolha.lower() in ["1", "informar dados", "2", "resgatar dados", "3", "alterar dados", "4", "deletar dados", "5", "sair", "6" , "consultar previsão do tempo"]:
            match escolha.lower():
                case "1" | "informar dados":
                    informar_dados()
                case "2" | "resgatar dados":
                    resgatar_dados()
                case "3" | "alterar dados":
                    alterar_dados()
                case "4" | "deletar dados":
                    deletar_dados ()
                case "5" | "sair":
                    print         ("Saindo...")
                    sys.exit() 
                case "6" | "consultar previsão do tempo":
                    print         (" Consultando previsão do tempo...")
                    consultar_previsao_tempo()
                    return   
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

menu()
