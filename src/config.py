"""
CanaOptimizer - Configurações do Sistema
Arquivo de configuração para conexão com banco de dados e parâmetros gerais
"""

# === CONFIGURAÇÕES DO BANCO DE DADOS ORACLE ===
# IMPORTANTE: Altere com suas credenciais
DATABASE_CONFIG = {
    'user': 'seu_usuario',          # Substitua pelo seu usuário Oracle
    'password': 'sua_senha',         # Substitua pela sua senha
    'dsn': 'localhost:1521/XEPDB1'   # Substitua pelo seu DSN (host:porta/service_name)
}

# === CONFIGURAÇÕES DE ARQUIVOS ===
CONFIG_ARQUIVOS = {
    'diretorio_exports': 'data/exports',
    'encoding': 'utf-8',
    'formato_data': '%d/%m/%Y %H:%M:%S'
}

# === PARÂMETROS DE NEGÓCIO ===
PARAMETROS_COLHEITA = {
    'perda_meta': 5.0,              # Meta de perda ideal (%)
    'perda_alerta': 10.0,           # Limite de alerta de perda (%)
    'perda_critica': 15.0,          # Perda crítica (%)
    'preco_tonelada': 120.00,       # Preço médio da tonelada de cana (R$)
    'produtividade_media': 100.0,   # Produtividade média (t/ha)
}

# === TIPOS DE CANA (TUPLA - IMUTÁVEL) ===
TIPOS_CANA = (
    'SP81-3250',
    'RB867515',
    'RB966928',
    'CTC4',
    'CTC9',
    'IACSP95-5000',
    'Outro'
)

# === MARCAS DE COLHEITADEIRAS (TUPLA - IMUTÁVEL) ===
MARCAS_COLHEITADEIRAS = (
    'Case IH',
    'John Deere',
    'New Holland',
    'Valtra',
    'Massey Ferguson',
    'Outra'
)

# === CONDIÇÕES CLIMÁTICAS (TUPLA - IMUTÁVEL) ===
CONDICOES_CLIMATICAS = (
    'Ensolarado',
    'Parcialmente Nublado',
    'Nublado',
    'Garoa',
    'Chuva Leve',
    'Chuva Forte'
)

# === CONFIGURAÇÕES DE ARQUIVO ===
CONFIG_ARQUIVOS = {
    'diretorio_exports': 'data/exports/',
    'formato_data': '%d/%m/%Y %H:%M:%S',
    'encoding': 'utf-8'
}

# === MENSAGENS DO SISTEMA ===
MENSAGENS = {
    'sucesso_cadastro': '✅ Cadastro realizado com sucesso!',
    'erro_cadastro': '❌ Erro ao realizar cadastro.',
    'sucesso_atualizacao': '✅ Atualização realizada com sucesso!',
    'erro_atualizacao': '❌ Erro ao atualizar registro.',
    'sucesso_exclusao': '✅ Exclusão realizada com sucesso!',
    'erro_exclusao': '❌ Erro ao excluir registro.',
    'erro_conexao': '❌ Erro de conexão com o banco de dados.',
    'entrada_invalida': '⚠️  Entrada inválida. Tente novamente.',
    'registro_nao_encontrado': '⚠️  Registro não encontrado.',
}

# === VERSÃO DO SISTEMA ===
VERSAO_SISTEMA = '1.0.0'
NOME_SISTEMA = 'CanaOptimizer'