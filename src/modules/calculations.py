"""
CanaOptimizer - Módulo de Cálculos
Funções para cálculos relacionados à colheita e perdas
Demonstra: SUBALGORITMOS (funções com passagem de parâmetros e retorno)
"""

from config import PARAMETROS_COLHEITA


def calcular_perda_toneladas(area_hectares: float, produtividade: float, 
                             percentual_perda: float) -> float:
    """
    Calcula a perda em toneladas
    
    Args:
        area_hectares (float): Área colhida em hectares
        produtividade (float): Produtividade em t/ha
        percentual_perda (float): Percentual de perda (0-100)
        
    Returns:
        float: Perda em toneladas
    """
    toneladas_total = area_hectares * produtividade
    perda_toneladas = toneladas_total * (percentual_perda / 100)
    return round(perda_toneladas, 2)


def calcular_perda_financeira(perda_toneladas: float, preco_tonelada: float = None) -> float:
    """
    Calcula a perda financeira em reais
    
    Args:
        perda_toneladas (float): Perda em toneladas
        preco_tonelada (float, optional): Preço da tonelada. Usa padrão se None.
        
    Returns:
        float: Perda em reais
    """
    if preco_tonelada is None:
        preco_tonelada = PARAMETROS_COLHEITA['preco_tonelada']
    
    perda_reais = perda_toneladas * preco_tonelada
    return round(perda_reais, 2)


def calcular_perda_financeira_completa(area_hectares: float, produtividade: float,
                                       percentual_perda: float, preco_tonelada: float = None) -> float:
    """
    Calcula perda financeira a partir dos parâmetros da colheita
    
    Args:
        area_hectares (float): Área em hectares
        produtividade (float): Produtividade em t/ha
        percentual_perda (float): Percentual de perda
        preco_tonelada (float, optional): Preço da tonelada
        
    Returns:
        float: Perda financeira em reais
    """
    toneladas_perdidas = calcular_perda_toneladas(area_hectares, produtividade, percentual_perda)
    return calcular_perda_financeira(toneladas_perdidas, preco_tonelada)


def calcular_toneladas_colhidas(area_hectares: float, produtividade: float, 
                                percentual_perda: float) -> float:
    """
    Calcula toneladas efetivamente colhidas (descontando perdas)
    
    Args:
        area_hectares (float): Área colhida em hectares
        produtividade (float): Produtividade em t/ha
        percentual_perda (float): Percentual de perda (0-100)
        
    Returns:
        float: Toneladas colhidas
    """
    toneladas_total = area_hectares * produtividade
    perda_toneladas = calcular_perda_toneladas(area_hectares, produtividade, percentual_perda)
    toneladas_colhidas = toneladas_total - perda_toneladas
    return round(toneladas_colhidas, 2)


def calcular_economia_potencial(area_hectares: float, produtividade: float,
                               perda_atual: float, perda_meta: float = None,
                               preco_tonelada: float = None) -> float:
    """
    Calcula economia potencial se atingir a meta de perda
    
    Args:
        area_hectares (float): Área em hectares
        produtividade (float): Produtividade em t/ha
        perda_atual (float): Perda atual em %
        perda_meta (float, optional): Meta de perda em %. Usa padrão se None.
        preco_tonelada (float, optional): Preço da tonelada
        
    Returns:
        float: Economia em reais
    """
    if perda_meta is None:
        perda_meta = PARAMETROS_COLHEITA['perda_meta']
    
    if perda_atual <= perda_meta:
        return 0.0  # Já está na meta ou melhor
    
    # Diferença de perda em percentual
    diferenca_perda = perda_atual - perda_meta
    
    # Calcular economia em toneladas e converter para reais
    toneladas_total = area_hectares * produtividade
    toneladas_economizadas = toneladas_total * (diferenca_perda / 100)
    
    if preco_tonelada is None:
        preco_tonelada = PARAMETROS_COLHEITA['preco_tonelada']
    
    economia = toneladas_economizadas * preco_tonelada
    return round(economia, 2)


def classificar_nivel_perda(percentual_perda: float) -> str:
    """
    Classifica o nível de perda
    
    Args:
        percentual_perda (float): Percentual de perda
        
    Returns:
        str: Classificação (Ótima, Boa, Regular, Alta, Crítica)
    """
    if percentual_perda <= 5.0:
        return "Ótima"
    elif percentual_perda <= 8.0:
        return "Boa"
    elif percentual_perda <= 12.0:
        return "Regular"
    elif percentual_perda <= 15.0:
        return "Alta"
    else:
        return "Crítica"


def calcular_eficiencia_colheita(percentual_perda: float) -> float:
    """
    Calcula eficiência da colheita (inverso da perda)
    
    Args:
        percentual_perda (float): Percentual de perda
        
    Returns:
        float: Eficiência em % (0-100)
    """
    eficiencia = 100 - percentual_perda
    return round(max(0, eficiencia), 2)


def calcular_media_perdas(lista_perdas: list) -> dict:
    """
    Calcula estatísticas de perdas de uma lista
    
    Args:
        lista_perdas (list): Lista de percentuais de perda
        
    Returns:
        dict: Dicionário com estatísticas (média, min, max, total_registros)
    """
    if not lista_perdas:
        return {
            'media': 0,
            'minima': 0,
            'maxima': 0,
            'total_registros': 0
        }
    
    return {
        'media': round(sum(lista_perdas) / len(lista_perdas), 2),
        'minima': round(min(lista_perdas), 2),
        'maxima': round(max(lista_perdas), 2),
        'total_registros': len(lista_perdas)
    }


def projetar_economia_anual(area_total_hectares: float, produtividade: float,
                           perda_atual: float, perda_meta: float = None,
                           preco_tonelada: float = None, safras_ano: int = 1) -> float:
    """
    Projeta economia anual se atingir meta de perda
    
    Args:
        area_total_hectares (float): Área total da fazenda
        produtividade (float): Produtividade média em t/ha
        perda_atual (float): Perda atual em %
        perda_meta (float, optional): Meta de perda. Usa padrão se None.
        preco_tonelada (float, optional): Preço da tonelada
        safras_ano (int): Número de safras por ano
        
    Returns:
        float: Economia projetada anual em reais
    """
    economia_por_safra = calcular_economia_potencial(
        area_total_hectares, 
        produtividade, 
        perda_atual, 
        perda_meta, 
        preco_tonelada
    )
    
    economia_anual = economia_por_safra * safras_ano
    return round(economia_anual, 2)
    economia_percentual = ((economia_ton / perda_atual_ton) * 100) if perda_atual_ton > 0 else 0
    
    return {
        'perda_atual_toneladas': round(perda_atual_ton, 2),
        'perda_atual_reais': round(perda_atual_reais, 2),
        'perda_meta_toneladas': round(perda_meta_ton, 2),
        'perda_meta_reais': round(perda_meta_reais, 2),
        'economia_toneladas': round(economia_ton, 2),
        'economia_reais': round(economia_reais, 2),
        'economia_percentual': round(economia_percentual, 2)
    }


def comparar_colheitas(colheita1: dict, colheita2: dict) -> dict:
    """
    Compara duas colheitas e retorna diferenças
    
    Args:
        colheita1 (dict): Dados da primeira colheita
        colheita2 (dict): Dados da segunda colheita
        
    Returns:
        dict: Comparação entre colheitas
    """
    diferenca_perda = colheita2['percentual_perda'] - colheita1['percentual_perda']
    diferenca_toneladas = colheita2['toneladas'] - colheita1['toneladas']
    
    melhorou = diferenca_perda < 0
    
    return {
        'diferenca_perda_percentual': round(diferenca_perda, 2),
        'diferenca_toneladas': round(diferenca_toneladas, 2),
        'melhorou': melhorou,
        'variacao_descricao': 'Melhorou' if melhorou else 'Piorou'
    }


def calcular_tempo_colheita(area_hectares: float, velocidade_kmh: float,
                           largura_corte_metros: float) -> float:
    """
    Estima tempo necessário para colheita
    
    Args:
        area_hectares (float): Área a ser colhida
        velocidade_kmh (float): Velocidade média da máquina
        largura_corte_metros (float): Largura de corte da colheitadeira
        
    Returns:
        float: Tempo estimado em horas
    """
    # Converter hectares para metros quadrados
    area_m2 = area_hectares * 10000
    
    # Converter largura de corte para km
    largura_corte_km = largura_corte_metros / 1000
    
    # Calcular distância a percorrer
    distancia_km = area_m2 / (largura_corte_metros * 1000)
    
    # Calcular tempo
    tempo_horas = distancia_km / velocidade_kmh if velocidade_kmh > 0 else 0
    
    return round(tempo_horas, 2)