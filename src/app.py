"""
CanaOptimizer - Sistema de Monitoramento de Perdas na Colheita de Cana
Aplicação Principal com Menu Interativo

Demonstra:
- Funções com passagem de parâmetros
- Estruturas de dados: listas, tuplas e dicionários
- Manipulação de arquivos texto e JSON
- Integração de todos os módulos
"""

import os
from datetime import datetime
from config import (
    TIPOS_CANA, 
    MARCAS_COLHEITADEIRAS, 
    CONDICOES_CLIMATICAS,
    PARAMETROS_COLHEITA
)
from modules.validations import (
    validar_numero_positivo,
    validar_percentual,
    validar_texto_nao_vazio,
    validar_opcao_menu,
    validar_escolha_lista,
    confirmar_acao,
    obter_entrada_valida
)
from modules.calculations import (
    calcular_perda_toneladas,
    calcular_perda_financeira_completa,
    calcular_economia_potencial,
    projetar_economia_anual
)
from modules.colheita_manager import ColheitaManager
from utils.file_handler import (
    salvar_relatorio_texto,
    salvar_dados_json,
    exportar_colheitas_json,
    listar_arquivos_exportados,
    gerar_cabecalho_relatorio,
    gerar_rodape_relatorio,
    formatar_tamanho_arquivo
)


def limpar_tela():
    """Limpa a tela do terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')


def pausar():
    """Pausa e aguarda tecla"""
    input("\n⏸️  Pressione ENTER para continuar...")


def exibir_logo():
    """Exibe logo do sistema"""
    print("=" * 80)
    print(" 🌾 CANAOPTIMIZER - SISTEMA DE MONITORAMENTO DE COLHEITA".center(80))
    print(" Reduza perdas e aumente lucros na colheita de cana-de-açúcar!".center(80))
    print("=" * 80)


def menu_principal():
    """Exibe menu principal"""
    print("\n📋 MENU PRINCIPAL")
    print("-" * 80)
    print("1️⃣  - Registrar Nova Colheita")
    print("2️⃣  - Consultar Colheitas")
    print("3️⃣  - Atualizar Colheita")
    print("4️⃣  - Remover Colheita")
    print("5️⃣  - Relatórios e Estatísticas")
    print("6️⃣  - Exportar Dados")
    print("7️⃣  - Calcular Simulações")
    print("8️⃣  - Gerenciar Arquivos")
    print("0️⃣  - Sair")
    print("-" * 80)


def escolher_da_lista(titulo: str, opcoes: tuple, permitir_outro: bool = True) -> str:
    """
    Exibe lista de opções e permite escolha
    
    Args:
        titulo (str): Título da lista
        opcoes (tuple): Tupla com opções
        permitir_outro (bool): Se permite digitar outra opção
        
    Returns:
        str: Opção escolhida
    """
    print(f"\n{titulo}")
    print("-" * 40)
    
    for i, opcao in enumerate(opcoes, 1):
        print(f"{i} - {opcao}")
    
    if permitir_outro:
        print(f"{len(opcoes) + 1} - Outro (digitar)")
    
    while True:
        entrada = input("\nEscolha uma opção: ").strip()
        valido, numero, _ = validar_numero_positivo(entrada, "opção")
        
        if valido and 1 <= numero <= len(opcoes):
            return opcoes[int(numero) - 1]
        elif permitir_outro and valido and numero == len(opcoes) + 1:
            outro = input("Digite a opção: ").strip()
            if outro:
                return outro
        
        print("❌ Opção inválida! Tente novamente.")


def registrar_nova_colheita(manager: ColheitaManager):
    """
    Registra nova colheita no sistema
    
    Args:
        manager (ColheitaManager): Gerenciador de colheitas
    """
    limpar_tela()
    exibir_logo()
    print("\n📝 REGISTRAR NOVA COLHEITA")
    print("=" * 80)
    
    try:
        # Coletar dados da colheita
        print("\n1️⃣  Identificação da Fazenda")
        fazenda = obter_entrada_valida(
            "Nome da fazenda: ",
            validar_texto_nao_vazio
        )
        
        print("\n2️⃣  Dados da Área")
        area = obter_entrada_valida(
            "Área colhida (hectares): ",
            validar_numero_positivo
        )
        
        produtividade = obter_entrada_valida(
            "Produtividade esperada (toneladas/hectare): ",
            validar_numero_positivo
        )
        
        print("\n3️⃣  Tipo de Cana")
        tipo_cana = escolher_da_lista("Selecione o tipo de cana:", TIPOS_CANA)
        
        print("\n4️⃣  Perda Observada")
        perda = obter_entrada_valida(
            "Percentual de perda observado (%): ",
            validar_percentual
        )
        
        print("\n5️⃣  Valor Financeiro")
        preco = obter_entrada_valida(
            f"Preço da tonelada (R$) [padrão: {PARAMETROS_COLHEITA['preco_tonelada']:.2f}]: ",
            validar_numero_positivo,
            opcional=True,
            valor_padrao=PARAMETROS_COLHEITA['preco_tonelada']
        )
        
        print("\n6️⃣  Equipamento Utilizado")
        colheitadeira = escolher_da_lista(
            "Marca da colheitadeira:", 
            MARCAS_COLHEITADEIRAS
        )
        
        velocidade = obter_entrada_valida(
            "Velocidade de operação (km/h): ",
            validar_numero_positivo
        )
        
        print("\n7️⃣  Condições da Colheita")
        condicao = escolher_da_lista(
            "Condição climática:", 
            CONDICOES_CLIMATICAS,
            permitir_outro=False
        )
        
        data_colheita = input("\nData da colheita (DD/MM/YYYY) [hoje]: ").strip()
        if not data_colheita:
            data_colheita = datetime.now().strftime('%d/%m/%Y')
        
        observacoes = input("\nObservações adicionais (opcional): ").strip()
        
        # Criar dicionário com dados
        dados_colheita = {
            'fazenda': fazenda,
            'area_hectares': area,
            'tipo_cana': tipo_cana,
            'produtividade': produtividade,
            'percentual_perda': perda,
            'preco_tonelada': preco,
            'colheitadeira': colheitadeira,
            'velocidade': velocidade,
            'condicao_clima': condicao,
            'data_colheita': data_colheita,
            'observacoes': observacoes
        }
        
        # Exibir resumo
        print("\n" + "=" * 80)
        print("📊 RESUMO DA COLHEITA")
        print("=" * 80)
        
        toneladas_perdidas = calcular_perda_toneladas(area, produtividade, perda)
        perda_financeira = calcular_perda_financeira_completa(area, produtividade, perda, preco)
        
        print(f"🌾 Fazenda: {fazenda}")
        print(f"📏 Área: {area:.2f} ha")
        print(f"📊 Produtividade: {produtividade:.2f} t/ha")
        print(f"🌱 Tipo de Cana: {tipo_cana}")
        print(f"⚠️  Perda: {perda:.2f}%")
        print(f"📦 Toneladas perdidas: {toneladas_perdidas:.2f} t")
        print(f"💰 Perda financeira: R$ {perda_financeira:,.2f}")
        print(f"🚜 Colheitadeira: {colheitadeira}")
        print(f"⚡ Velocidade: {velocidade:.1f} km/h")
        print(f"🌤️  Clima: {condicao}")
        print(f"📅 Data: {data_colheita}")
        print("=" * 80)
        
        # Confirmar
        if confirmar_acao("Confirmar registro?"):
            sucesso, id_colheita, mensagem = manager.adicionar_colheita(dados_colheita)
            print(f"\n{mensagem}")
            if sucesso:
                print(f"🆔 ID da colheita: {id_colheita}")
        else:
            print("\n❌ Registro cancelado!")
    
    except KeyboardInterrupt:
        print("\n\n❌ Registro cancelado!")
    except Exception as e:
        print(f"\n❌ Erro ao registrar colheita: {str(e)}")
    
    pausar()


def consultar_colheitas(manager: ColheitaManager):
    """
    Consulta e exibe colheitas registradas
    
    Args:
        manager (ColheitaManager): Gerenciador de colheitas
    """
    limpar_tela()
    exibir_logo()
    print("\n🔍 CONSULTAR COLHEITAS")
    print("=" * 80)
    
    print("\n1 - Listar todas")
    print("2 - Buscar por fazenda")
    print("3 - Filtrar por classificação")
    print("4 - Buscar por ID")
    print("0 - Voltar")
    
    opcao = input("\nEscolha: ").strip()
    
    colheitas = []
    
    if opcao == '1':
        colheitas = manager.listar_todas()
    elif opcao == '2':
        fazenda = input("\nNome da fazenda: ").strip()
        colheitas = manager.listar_por_fazenda(fazenda)
    elif opcao == '3':
        print("\nClassificações: Ótima, Boa, Regular, Alta, Crítica")
        classificacao = input("Classificação: ").strip().title()
        colheitas = manager.listar_por_classificacao(classificacao)
    elif opcao == '4':
        id_str = input("\nID da colheita: ").strip()
        valido, id_num, _ = validar_numero_positivo(id_str, "ID")
        if valido:
            colheita = manager.buscar_por_id(int(id_num))
            if colheita:
                colheitas = [colheita]
            else:
                print("\n❌ Colheita não encontrada!")
    elif opcao == '0':
        return
    
    if colheitas:
        print(f"\n📋 {len(colheitas)} COLHEITA(S) ENCONTRADA(S)")
        print("=" * 80)
        
        for c in colheitas:
            print(f"\n🆔 ID: {c['id']} | 🌾 Fazenda: {c['fazenda']}")
            print(f"📅 Data: {c['data_colheita']} | 📏 Área: {c['area_hectares']:.2f} ha")
            print(f"🌱 Tipo: {c['tipo_cana']} | 📊 Produtividade: {c['produtividade']:.2f} t/ha")
            print(f"⚠️  Perda: {c['percentual_perda']:.2f}% ({c['toneladas_perdidas']:.2f} t)")
            print(f"💰 Perda financeira: R$ {c['perda_financeira']:,.2f}")
            print(f"✅ Eficiência: {c['eficiencia']:.2f}% | 📊 Classificação: {c['classificacao']}")
            print(f"🚜 Colheitadeira: {c['colheitadeira']} | ⚡ {c['velocidade']:.1f} km/h")
            print(f"🌤️  Clima: {c['condicao_clima']}")
            if c['observacoes']:
                print(f"📝 Obs: {c['observacoes']}")
            print("-" * 80)
    else:
        print("\n📭 Nenhuma colheita encontrada!")
    
    pausar()


def gerar_relatorios(manager: ColheitaManager):
    """
    Gera relatórios e estatísticas
    
    Args:
        manager (ColheitaManager): Gerenciador de colheitas
    """
    limpar_tela()
    exibir_logo()
    print("\n📊 RELATÓRIOS E ESTATÍSTICAS")
    print("=" * 80)
    
    print("\n1 - Estatísticas Gerais")
    print("2 - Ranking de Fazendas")
    print("3 - Análise por Tipo de Cana")
    print("4 - Gerar Relatório Completo (TXT)")
    print("0 - Voltar")
    
    opcao = input("\nEscolha: ").strip()
    
    if opcao == '1':
        stats = manager.obter_estatisticas()
        print("\n📊 ESTATÍSTICAS GERAIS")
        print("=" * 80)
        print(f"📋 Total de colheitas: {stats['total_colheitas']}")
        print(f"📏 Área total: {stats['area_total']:.2f} ha")
        print(f"⚠️  Perda média: {stats['perda_media']:.2f}%")
        print(f"📦 Toneladas perdidas: {stats['toneladas_perdidas_total']:.2f} t")
        print(f"💰 Perda financeira total: R$ {stats['perda_total_financeira']:,.2f}")
        print(f"✅ Eficiência média: {stats['eficiencia_media']:.2f}%")
    
    elif opcao == '2':
        ranking = manager.obter_ranking_fazendas()
        print("\n🏆 RANKING DE FAZENDAS POR EFICIÊNCIA")
        print("=" * 80)
        for i, fazenda in enumerate(ranking, 1):
            print(f"{i}º - {fazenda['fazenda']}")
            print(f"    ✅ Eficiência: {fazenda['eficiencia_media']:.2f}%")
            print(f"    ⚠️  Perda média: {fazenda['perda_media']:.2f}%")
            print(f"    📋 Colheitas: {fazenda['colheitas']}")
            print("-" * 40)
    
    elif opcao == '3':
        totalizacao = manager.obter_totalizacao_por_tipo_cana()
        print("\n🌱 ANÁLISE POR TIPO DE CANA")
        print("=" * 80)
        for tipo, dados in totalizacao.items():
            print(f"\n🌾 {tipo}")
            print(f"   📋 Quantidade: {dados['quantidade']}")
            print(f"   📏 Área total: {dados['area_total']:.2f} ha")
            print(f"   ⚠️  Perda média: {dados['perda_media']:.2f}%")
            print("-" * 40)
    
    elif opcao == '4':
        # Gerar relatório completo
        relatorio = gerar_cabecalho_relatorio("RELATÓRIO COMPLETO DE COLHEITAS")
        
        stats = manager.obter_estatisticas()
        relatorio += "\n\n=== ESTATÍSTICAS GERAIS ===\n"
        relatorio += f"Total de colheitas: {stats['total_colheitas']}\n"
        relatorio += f"Área total: {stats['area_total']:.2f} ha\n"
        relatorio += f"Perda média: {stats['perda_media']:.2f}%\n"
        relatorio += f"Toneladas perdidas: {stats['toneladas_perdidas_total']:.2f} t\n"
        relatorio += f"Perda financeira: R$ {stats['perda_total_financeira']:,.2f}\n"
        relatorio += f"Eficiência média: {stats['eficiencia_media']:.2f}%\n"
        
        relatorio += "\n\n=== RANKING DE FAZENDAS ===\n"
        ranking = manager.obter_ranking_fazendas()
        for i, faz in enumerate(ranking, 1):
            relatorio += f"{i}º - {faz['fazenda']} - Eficiência: {faz['eficiencia_media']:.2f}%\n"
        
        relatorio += "\n\n=== DETALHAMENTO DE COLHEITAS ===\n"
        for c in manager.listar_todas():
            relatorio += f"\nID: {c['id']} | Fazenda: {c['fazenda']}\n"
            relatorio += f"Data: {c['data_colheita']} | Área: {c['area_hectares']:.2f} ha\n"
            relatorio += f"Perda: {c['percentual_perda']:.2f}% | Classificação: {c['classificacao']}\n"
            relatorio += "-" * 80 + "\n"
        
        relatorio += gerar_rodape_relatorio()
        
        sucesso, caminho, mensagem = salvar_relatorio_texto("relatorio_completo", relatorio)
        print(f"\n{mensagem}")
        if sucesso:
            print(f"📁 Arquivo: {caminho}")
    
    pausar()


def exportar_dados(manager: ColheitaManager):
    """
    Exporta dados para JSON
    
    Args:
        manager (ColheitaManager): Gerenciador de colheitas
    """
    limpar_tela()
    exibir_logo()
    print("\n💾 EXPORTAR DADOS")
    print("=" * 80)
    
    colheitas = manager.listar_todas()
    
    if not colheitas:
        print("\n📭 Nenhuma colheita para exportar!")
        pausar()
        return
    
    print(f"\n📋 {len(colheitas)} colheita(s) registrada(s)")
    
    if confirmar_acao("Exportar para JSON?"):
        sucesso, caminho, mensagem = exportar_colheitas_json(colheitas)
        print(f"\n{mensagem}")
        if sucesso:
            print(f"📁 Arquivo: {caminho}")
    
    pausar()


def calcular_simulacoes():
    """Realiza cálculos e simulações"""
    limpar_tela()
    exibir_logo()
    print("\n🧮 CALCULAR SIMULAÇÕES")
    print("=" * 80)
    
    print("\n1 - Simular perda em toneladas")
    print("2 - Simular perda financeira")
    print("3 - Calcular economia potencial")
    print("4 - Projetar economia anual")
    print("0 - Voltar")
    
    opcao = input("\nEscolha: ").strip()
    
    try:
        if opcao in ['1', '2', '3', '4']:
            print("\n📊 DADOS PARA SIMULAÇÃO")
            area = obter_entrada_valida(
                "Área (hectares): ",
                validar_numero_positivo
            )
            produtividade = obter_entrada_valida(
                "Produtividade (t/ha): ",
                validar_numero_positivo
            )
            perda_atual = obter_entrada_valida(
                "Perda atual (%): ",
                validar_percentual
            )
            preco = obter_entrada_valida(
                f"Preço/tonelada (R$) [{PARAMETROS_COLHEITA['preco_tonelada']:.2f}]: ",
                validar_numero_positivo,
                opcional=True,
                valor_padrao=PARAMETROS_COLHEITA['preco_tonelada']
            )
            
            print("\n" + "=" * 80)
            print("📊 RESULTADOS")
            print("=" * 80)
            
            if opcao == '1':
                toneladas = calcular_perda_toneladas(area, produtividade, perda_atual)
                print(f"\n📦 Perda em toneladas: {toneladas:.2f} t")
            
            elif opcao == '2':
                perda_fin = calcular_perda_financeira_completa(area, produtividade, perda_atual, preco)
                print(f"\n💰 Perda financeira: R$ {perda_fin:,.2f}")
            
            elif opcao == '3':
                perda_meta = obter_entrada_valida(
                    f"Perda alvo (%) [{PARAMETROS_COLHEITA['perda_meta']:.1f}]: ",
                    validar_percentual,
                    opcional=True,
                    valor_padrao=PARAMETROS_COLHEITA['perda_meta']
                )
                economia = calcular_economia_potencial(
                    area, produtividade, perda_atual, perda_meta, preco
                )
                print(f"\n💰 Economia potencial: R$ {economia:,.2f}")
                print(f"📉 Reduzindo de {perda_atual:.2f}% para {perda_meta:.2f}%")
            
            elif opcao == '4':
                safras_ano = obter_entrada_valida(
                    "Número de safras por ano: ",
                    validar_numero_positivo
                )
                perda_meta = obter_entrada_valida(
                    f"Perda alvo (%) [{PARAMETROS_COLHEITA['perda_meta']:.1f}]: ",
                    validar_percentual,
                    opcional=True,
                    valor_padrao=PARAMETROS_COLHEITA['perda_meta']
                )
                economia_anual = projetar_economia_anual(
                    area, produtividade, perda_atual, perda_meta, preco, int(safras_ano)
                )
                print(f"\n💰 Economia projetada anual: R$ {economia_anual:,.2f}")
                print(f"📊 Com {int(safras_ano)} safra(s) por ano")
    
    except Exception as e:
        print(f"\n❌ Erro: {str(e)}")
    
    pausar()


def gerenciar_arquivos():
    """Gerencia arquivos exportados"""
    limpar_tela()
    exibir_logo()
    print("\n📁 GERENCIAR ARQUIVOS EXPORTADOS")
    print("=" * 80)
    
    arquivos = listar_arquivos_exportados()
    
    if not arquivos:
        print("\n📭 Nenhum arquivo exportado encontrado!")
    else:
        print(f"\n📋 {len(arquivos)} arquivo(s) encontrado(s):")
        print("-" * 80)
        for arq in arquivos:
            tamanho = formatar_tamanho_arquivo(arq['tamanho_bytes'])
            print(f"\n📄 {arq['nome']}")
            print(f"   📊 Tipo: {arq['tipo']}")
            print(f"   💾 Tamanho: {tamanho}")
            print(f"   📅 Modificado: {arq['data_modificacao']}")
            print(f"   📁 Caminho: {arq['caminho']}")
    
    pausar()


def main():
    """Função principal do sistema"""
    # Criar gerenciador de colheitas
    manager = ColheitaManager()
    
    # Adicionar dados de exemplo (opcional)
    if len(manager.listar_todas()) == 0:
        print("🔄 Adicionando dados de exemplo...")
        exemplos = [
            {
                'fazenda': 'Fazenda São João',
                'area_hectares': 50.0,
                'tipo_cana': 'RB867515',
                'produtividade': 95.0,
                'percentual_perda': 4.5,
                'preco_tonelada': 120.00,
                'colheitadeira': 'John Deere',
                'velocidade': 5.5,
                'condicao_clima': 'Ensolarado',
                'data_colheita': '15/05/2024',
                'observacoes': 'Colheita em condições ideais'
            },
            {
                'fazenda': 'Fazenda Santa Clara',
                'area_hectares': 75.0,
                'tipo_cana': 'CTC4',
                'produtividade': 110.0,
                'percentual_perda': 12.0,
                'preco_tonelada': 120.00,
                'colheitadeira': 'Case IH',
                'velocidade': 7.0,
                'condicao_clima': 'Chuva Leve',
                'data_colheita': '16/05/2024',
                'observacoes': 'Chuva atrasou operação'
            }
        ]
        for exemplo in exemplos:
            manager.adicionar_colheita(exemplo)
    
    # Loop principal
    while True:
        try:
            limpar_tela()
            exibir_logo()
            menu_principal()
            
            opcao = input("\n👉 Escolha uma opção: ").strip()
            
            if opcao == '1':
                registrar_nova_colheita(manager)
            elif opcao == '2':
                consultar_colheitas(manager)
            elif opcao == '3':
                print("\n🔧 Atualização em desenvolvimento...")
                pausar()
            elif opcao == '4':
                print("\n🗑️  Remoção em desenvolvimento...")
                pausar()
            elif opcao == '5':
                gerar_relatorios(manager)
            elif opcao == '6':
                exportar_dados(manager)
            elif opcao == '7':
                calcular_simulacoes()
            elif opcao == '8':
                gerenciar_arquivos()
            elif opcao == '0':
                limpar_tela()
                exibir_logo()
                print("\n👋 Obrigado por usar o CanaOptimizer!")
                print("🌾 Até a próxima safra!\n")
                break
            else:
                print("\n❌ Opção inválida!")
                pausar()
        
        except KeyboardInterrupt:
            limpar_tela()
            print("\n\n⚠️  Sistema interrompido pelo usuário!")
            if confirmar_acao("Deseja realmente sair?"):
                print("\n👋 Até logo!\n")
                break
        except Exception as e:
            print(f"\n❌ Erro inesperado: {str(e)}")
            pausar()


if __name__ == "__main__":
    main()
