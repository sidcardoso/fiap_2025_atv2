"""
CanaOptimizer - Manipulação de Arquivos
Funções para leitura e escrita de arquivos texto e JSON
Demonstra: MANIPULAÇÃO DE ARQUIVOS (texto e JSON)
"""

import json
import os
from datetime import datetime
from config import CONFIG_ARQUIVOS


def salvar_relatorio_texto(nome_arquivo: str, conteudo: str) -> tuple:
    """
    Salva relatório em arquivo texto
    
    Args:
        nome_arquivo (str): Nome do arquivo
        conteudo (str): Conteúdo do relatório
        
    Returns:
        tuple: (sucesso: bool, caminho_arquivo: str, mensagem: str)
    """
    try:
        # Garantir que o diretório existe
        diretorio = CONFIG_ARQUIVOS['diretorio_exports']
        os.makedirs(diretorio, exist_ok=True)
        
        # Adicionar timestamp ao nome
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        nome_completo = f"{nome_arquivo}_{timestamp}.txt"
        caminho_completo = os.path.join(diretorio, nome_completo)
        
        # Salvar arquivo
        with open(caminho_completo, 'w', encoding=CONFIG_ARQUIVOS['encoding']) as arquivo:
            arquivo.write(conteudo)
        
        return (True, caminho_completo, "✅ Relatório salvo com sucesso!")
    
    except Exception as e:
        return (False, "", f"❌ Erro ao salvar relatório: {str(e)}")


def ler_relatorio_texto(caminho_arquivo: str) -> tuple:
    """
    Lê relatório de arquivo texto
    
    Args:
        caminho_arquivo (str): Caminho do arquivo
        
    Returns:
        tuple: (sucesso: bool, conteudo: str, mensagem: str)
    """
    try:
        with open(caminho_arquivo, 'r', encoding=CONFIG_ARQUIVOS['encoding']) as arquivo:
            conteudo = arquivo.read()
        
        return (True, conteudo, "")
    
    except FileNotFoundError:
        return (False, "", "❌ Arquivo não encontrado!")
    except Exception as e:
        return (False, "", f"❌ Erro ao ler arquivo: {str(e)}")


def salvar_dados_json(nome_arquivo: str, dados: dict) -> tuple:
    """
    Salva dados em arquivo JSON
    
    Args:
        nome_arquivo (str): Nome do arquivo
        dados (dict): Dicionário com dados a salvar
        
    Returns:
        tuple: (sucesso: bool, caminho_arquivo: str, mensagem: str)
    """
    try:
        # Garantir que o diretório existe
        diretorio = CONFIG_ARQUIVOS['diretorio_exports']
        os.makedirs(diretorio, exist_ok=True)
        
        # Adicionar timestamp ao nome
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        nome_completo = f"{nome_arquivo}_{timestamp}.json"
        caminho_completo = os.path.join(diretorio, nome_completo)
        
        # Salvar arquivo JSON
        with open(caminho_completo, 'w', encoding=CONFIG_ARQUIVOS['encoding']) as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
        
        return (True, caminho_completo, "✅ Dados JSON salvos com sucesso!")
    
    except Exception as e:
        return (False, "", f"❌ Erro ao salvar JSON: {str(e)}")


def ler_dados_json(caminho_arquivo: str) -> tuple:
    """
    Lê dados de arquivo JSON
    
    Args:
        caminho_arquivo (str): Caminho do arquivo
        
    Returns:
        tuple: (sucesso: bool, dados: dict, mensagem: str)
    """
    try:
        with open(caminho_arquivo, 'r', encoding=CONFIG_ARQUIVOS['encoding']) as arquivo:
            dados = json.load(arquivo)
        
        return (True, dados, "")
    
    except FileNotFoundError:
        return (False, {}, "❌ Arquivo JSON não encontrado!")
    except json.JSONDecodeError:
        return (False, {}, "❌ Erro ao decodificar JSON!")
    except Exception as e:
        return (False, {}, f"❌ Erro ao ler JSON: {str(e)}")


def listar_arquivos_exportados() -> list:
    """
    Lista todos os arquivos exportados
    
    Returns:
        list: Lista de dicionários com informações dos arquivos
    """
    arquivos_info = []
    
    try:
        diretorio = CONFIG_ARQUIVOS['diretorio_exports']
        
        # Criar diretório se não existir
        os.makedirs(diretorio, exist_ok=True)
        
        # Listar arquivos
        for arquivo in os.listdir(diretorio):
            caminho_completo = os.path.join(diretorio, arquivo)
            
            if os.path.isfile(caminho_completo):
                # Obter informações do arquivo
                tamanho = os.path.getsize(caminho_completo)
                data_modificacao = datetime.fromtimestamp(os.path.getmtime(caminho_completo))
                extensao = os.path.splitext(arquivo)[1]
                
                arquivos_info.append({
                    'nome': arquivo,
                    'caminho': caminho_completo,
                    'tamanho_bytes': tamanho,
                    'data_modificacao': data_modificacao.strftime(CONFIG_ARQUIVOS['formato_data']),
                    'tipo': extensao[1:].upper() if extensao else 'Desconhecido'
                })
        
        # Ordenar por data de modificação (mais recente primeiro)
        arquivos_info.sort(key=lambda x: x['data_modificacao'], reverse=True)
        
    except Exception as e:
        print(f"⚠️  Erro ao listar arquivos: {str(e)}")
    
    return arquivos_info


def exportar_colheitas_json(lista_colheitas: list, nome_arquivo: str = "colheitas") -> tuple:
    """
    Exporta lista de colheitas para JSON
    
    Args:
        lista_colheitas (list): Lista de dicionários com dados de colheitas
        nome_arquivo (str): Nome base do arquivo
        
    Returns:
        tuple: (sucesso: bool, caminho: str, mensagem: str)
    """
    dados_export = {
        'metadata': {
            'data_exportacao': datetime.now().strftime(CONFIG_ARQUIVOS['formato_data']),
            'total_registros': len(lista_colheitas),
            'sistema': 'CanaOptimizer'
        },
        'colheitas': lista_colheitas
    }
    
    return salvar_dados_json(nome_arquivo, dados_export)


def gerar_cabecalho_relatorio(titulo: str) -> str:
    """
    Gera cabeçalho padrão para relatórios
    
    Args:
        titulo (str): Título do relatório
        
    Returns:
        str: Cabeçalho formatado
    """
    largura = 80
    linha = "=" * largura
    data_hora = datetime.now().strftime(CONFIG_ARQUIVOS['formato_data'])
    
    cabecalho = f"""
{linha}
{titulo.center(largura)}
{linha}
Data/Hora: {data_hora}
Sistema: CanaOptimizer v1.0
{linha}
"""
    return cabecalho


def gerar_rodape_relatorio() -> str:
    """
    Gera rodapé padrão para relatórios
    
    Returns:
        str: Rodapé formatado
    """
    largura = 80
    linha = "=" * largura
    
    rodape = f"""
{linha}
Relatório gerado automaticamente pelo CanaOptimizer
FIAP - Computational Thinking with Python
{linha}
"""
    return rodape


def salvar_configuracao_sistema(configuracoes: dict) -> tuple:
    """
    Salva configurações do sistema em JSON
    
    Args:
        configuracoes (dict): Dicionário com configurações
        
    Returns:
        tuple: (sucesso: bool, mensagem: str)
    """
    try:
        caminho = 'data/config.json'
        os.makedirs(os.path.dirname(caminho), exist_ok=True)
        
        with open(caminho, 'w', encoding='utf-8') as arquivo:
            json.dump(configuracoes, arquivo, indent=4, ensure_ascii=False)
        
        return (True, "✅ Configurações salvas!")
    
    except Exception as e:
        return (False, f"❌ Erro ao salvar configurações: {str(e)}")


def carregar_configuracao_sistema() -> tuple:
    """
    Carrega configurações do sistema do JSON
    
    Returns:
        tuple: (sucesso: bool, configuracoes: dict, mensagem: str)
    """
    try:
        caminho = 'data/config.json'
        
        if not os.path.exists(caminho):
            # Retornar configurações padrão
            config_padrao = {
                'preco_tonelada': 120.00,
                'perda_meta': 5.0,
                'produtividade_media': 100.0
            }
            return (True, config_padrao, "⚠️  Usando configurações padrão")
        
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            configuracoes = json.load(arquivo)
        
        return (True, configuracoes, "")
    
    except Exception as e:
        return (False, {}, f"❌ Erro ao carregar configurações: {str(e)}")


def formatar_tamanho_arquivo(tamanho_bytes: int) -> str:
    """
    Formata tamanho do arquivo em formato legível
    
    Args:
        tamanho_bytes (int): Tamanho em bytes
        
    Returns:
        str: Tamanho formatado (ex: "1.5 KB")
    """
    for unidade in ['B', 'KB', 'MB', 'GB']:
        if tamanho_bytes < 1024.0:
            return f"{tamanho_bytes:.1f} {unidade}"
        tamanho_bytes /= 1024.0
    return f"{tamanho_bytes:.1f} TB"