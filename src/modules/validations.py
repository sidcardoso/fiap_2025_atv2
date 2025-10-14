"""
CanaOptimizer - Módulo de Validações
Funções para validar entradas do usuário
Demonstra: SUBALGORITMOS (funções com passagem de parâmetros)
"""

def validar_numero_positivo(valor_str: str, nome_campo: str) -> tuple:
    """
    Valida se a entrada é um número positivo
    
    Args:
        valor_str (str): Valor digitado pelo usuário
        nome_campo (str): Nome do campo para mensagem de erro
        
    Returns:
        tuple: (sucesso: bool, valor: float, mensagem: str)
    """
    try:
        valor = float(valor_str)
        if valor <= 0:
            return (False, 0, f"⚠️  {nome_campo} deve ser maior que zero!")
        return (True, valor, "")
    except ValueError:
        return (False, 0, f"⚠️  {nome_campo} deve ser um número válido!")


def validar_percentual(valor_str: str, nome_campo: str) -> tuple:
    """
    Valida se a entrada é um percentual válido (0-100)
    
    Args:
        valor_str (str): Valor digitado pelo usuário
        nome_campo (str): Nome do campo para mensagem de erro
        
    Returns:
        tuple: (sucesso: bool, valor: float, mensagem: str)
    """
    try:
        valor = float(valor_str)
        if valor < 0 or valor > 100:
            return (False, 0, f"⚠️  {nome_campo} deve estar entre 0 e 100!")
        return (True, valor, "")
    except ValueError:
        return (False, 0, f"⚠️  {nome_campo} deve ser um número válido!")


def validar_texto_nao_vazio(texto: str, nome_campo: str) -> tuple:
    """
    Valida se o texto não está vazio
    
    Args:
        texto (str): Texto digitado pelo usuário
        nome_campo (str): Nome do campo para mensagem de erro
        
    Returns:
        tuple: (sucesso: bool, texto_limpo: str, mensagem: str)
    """
    texto_limpo = texto.strip()
    if not texto_limpo:
        return (False, "", f"⚠️  {nome_campo} não pode estar vazio!")
    return (True, texto_limpo, "")


def validar_opcao_menu(opcao_str: str, min_opcao: int, max_opcao: int) -> tuple:
    """
    Valida se a opção do menu é válida
    
    Args:
        opcao_str (str): Opção digitada pelo usuário
        min_opcao (int): Opção mínima válida
        max_opcao (int): Opção máxima válida
        
    Returns:
        tuple: (sucesso: bool, opcao: int, mensagem: str)
    """
    try:
        opcao = int(opcao_str)
        if opcao < min_opcao or opcao > max_opcao:
            return (False, 0, f"⚠️  Opção deve estar entre {min_opcao} e {max_opcao}!")
        return (True, opcao, "")
    except ValueError:
        return (False, 0, "⚠️  Opção deve ser um número inteiro!")


def validar_ano(ano_str: str) -> tuple:
    """
    Valida se o ano é válido
    
    Args:
        ano_str (str): Ano digitado pelo usuário
        
    Returns:
        tuple: (sucesso: bool, ano: int, mensagem: str)
    """
    try:
        ano = int(ano_str)
        if ano < 2000 or ano > 2100:
            return (False, 0, "⚠️  Ano deve estar entre 2000 e 2100!")
        return (True, ano, "")
    except ValueError:
        return (False, 0, "⚠️  Ano deve ser um número inteiro!")


def validar_cpf_simples(cpf: str) -> tuple:
    """
    Validação simples de CPF (apenas formato)
    
    Args:
        cpf (str): CPF digitado pelo usuário
        
    Returns:
        tuple: (sucesso: bool, cpf_limpo: str, mensagem: str)
    """
    # Remove caracteres não numéricos
    cpf_limpo = ''.join(filter(str.isdigit, cpf))
    
    if len(cpf_limpo) != 11:
        return (False, "", "⚠️  CPF deve conter 11 dígitos!")
    
    # Verifica se todos os dígitos são iguais (CPF inválido)
    if cpf_limpo == cpf_limpo[0] * 11:
        return (False, "", "⚠️  CPF inválido!")
    
    return (True, cpf_limpo, "")


def validar_escolha_lista(opcao_str: str, opcoes_disponiveis: tuple) -> tuple:
    """
    Valida se a escolha está na lista de opções disponíveis
    
    Args:
        opcao_str (str): Número da opção escolhida
        opcoes_disponiveis (tuple): Tupla com opções disponíveis
        
    Returns:
        tuple: (sucesso: bool, valor_escolhido: str, mensagem: str)
    """
    try:
        indice = int(opcao_str) - 1
        if indice < 0 or indice >= len(opcoes_disponiveis):
            return (False, "", f"⚠️  Escolha deve estar entre 1 e {len(opcoes_disponiveis)}!")
        return (True, opcoes_disponiveis[indice], "")
    except ValueError:
        return (False, "", "⚠️  Escolha deve ser um número inteiro!")


def validar_velocidade(velocidade_str: str) -> tuple:
    """
    Valida velocidade da colheitadeira (km/h)
    
    Args:
        velocidade_str (str): Velocidade digitada
        
    Returns:
        tuple: (sucesso: bool, velocidade: float, mensagem: str)
    """
    try:
        velocidade = float(velocidade_str)
        if velocidade < 0 or velocidade > 20:
            return (False, 0, "⚠️  Velocidade deve estar entre 0 e 20 km/h!")
        return (True, velocidade, "")
    except ValueError:
        return (False, 0, "⚠️  Velocidade deve ser um número válido!")


def confirmar_acao(mensagem: str) -> bool:
    """
    Solicita confirmação do usuário para uma ação
    
    Args:
        mensagem (str): Mensagem de confirmação
        
    Returns:
        bool: True se confirmado, False caso contrário
    """
    while True:
        resposta = input(f"\n{mensagem} (S/N): ").strip().upper()
        if resposta in ['S', 'SIM']:
            return True
        elif resposta in ['N', 'NAO', 'NÃO']:
            return False
        else:
            print("⚠️  Resposta inválida! Digite S para Sim ou N para Não.")


# === FUNÇÃO AUXILIAR PARA OBTER ENTRADA VÁLIDA ===
def obter_entrada_valida(mensagem: str, funcao_validacao, *args) -> any:
    """
    Solicita entrada do usuário até que seja válida
    
    Args:
        mensagem (str): Mensagem a exibir
        funcao_validacao: Função de validação a ser chamada
        *args: Argumentos adicionais para a função de validação
        
    Returns:
        any: Valor validado
    """
    while True:
        entrada = input(mensagem)
        sucesso, valor, msg_erro = funcao_validacao(entrada, *args)
        
        if sucesso:
            return valor
        else:
            print(msg_erro)