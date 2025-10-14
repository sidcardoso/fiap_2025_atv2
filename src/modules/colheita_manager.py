"""
CanaOptimizer - Gerenciador de Colheitas
Gerencia registros de colheita usando listas e dicionários
Demonstra: USO DE LISTAS e DICIONÁRIOS
"""

from datetime import datetime
from modules.calculations import (
    calcular_perda_toneladas,
    calcular_perda_financeira_completa,
    calcular_toneladas_colhidas,
    calcular_eficiencia_colheita,
    classificar_nivel_perda
)
from modules.validations import validar_numero_positivo, validar_percentual


class ColheitaManager:
    """Gerenciador de registros de colheita usando lista"""
    
    def __init__(self):
        """Inicializa lista de colheitas"""
        self.colheitas = []  # LISTA para armazenar colheitas
        self.proximo_id = 1
    
    def adicionar_colheita(self, dados_colheita: dict) -> tuple:
        """
        Adiciona nova colheita à lista
        
        Args:
            dados_colheita (dict): Dicionário com dados da colheita
            
        Returns:
            tuple: (sucesso: bool, id: int, mensagem: str)
        """
        try:
            # Criar DICIONÁRIO da colheita
            colheita = {
                'id': self.proximo_id,
                'fazenda': dados_colheita['fazenda'],
                'area_hectares': dados_colheita['area_hectares'],
                'tipo_cana': dados_colheita['tipo_cana'],
                'produtividade': dados_colheita['produtividade'],
                'percentual_perda': dados_colheita['percentual_perda'],
                'preco_tonelada': dados_colheita['preco_tonelada'],
                'colheitadeira': dados_colheita['colheitadeira'],
                'velocidade': dados_colheita['velocidade'],
                'condicao_clima': dados_colheita['condicao_clima'],
                'data_colheita': dados_colheita.get('data_colheita', 
                                                    datetime.now().strftime('%d/%m/%Y')),
                'observacoes': dados_colheita.get('observacoes', ''),
                # Calcular valores derivados
                'toneladas_colhidas': calcular_toneladas_colhidas(
                    dados_colheita['area_hectares'],
                    dados_colheita['produtividade'],
                    dados_colheita['percentual_perda']
                ),
                'toneladas_perdidas': calcular_perda_toneladas(
                    dados_colheita['area_hectares'],
                    dados_colheita['produtividade'],
                    dados_colheita['percentual_perda']
                ),
                'perda_financeira': calcular_perda_financeira_completa(
                    dados_colheita['area_hectares'],
                    dados_colheita['produtividade'],
                    dados_colheita['percentual_perda'],
                    dados_colheita['preco_tonelada']
                ),
                'eficiencia': calcular_eficiencia_colheita(dados_colheita['percentual_perda']),
                'classificacao': classificar_nivel_perda(dados_colheita['percentual_perda'])
            }
            
            # Adicionar à LISTA
            self.colheitas.append(colheita)
            self.proximo_id += 1
            
            return (True, colheita['id'], "✅ Colheita registrada com sucesso!")
        
        except Exception as e:
            return (False, 0, f"❌ Erro ao adicionar colheita: {str(e)}")
    
    def buscar_por_id(self, id_colheita: int) -> dict:
        """
        Busca colheita por ID na lista
        
        Args:
            id_colheita (int): ID da colheita
            
        Returns:
            dict: Dicionário da colheita ou None
        """
        for colheita in self.colheitas:
            if colheita['id'] == id_colheita:
                return colheita
        return None
    
    def listar_todas(self) -> list:
        """
        Retorna lista de todas as colheitas
        
        Returns:
            list: Lista de dicionários de colheitas
        """
        return self.colheitas.copy()
    
    def listar_por_fazenda(self, nome_fazenda: str) -> list:
        """
        Filtra colheitas por fazenda
        
        Args:
            nome_fazenda (str): Nome da fazenda
            
        Returns:
            list: Lista filtrada de colheitas
        """
        return [c for c in self.colheitas if c['fazenda'].lower() == nome_fazenda.lower()]
    
    def listar_por_classificacao(self, classificacao: str) -> list:
        """
        Filtra colheitas por classificação de perda
        
        Args:
            classificacao (str): 'Ótima', 'Boa', 'Regular', 'Alta' ou 'Crítica'
            
        Returns:
            list: Lista filtrada de colheitas
        """
        return [c for c in self.colheitas if c['classificacao'] == classificacao]
    
    def atualizar_colheita(self, id_colheita: int, dados_atualizados: dict) -> tuple:
        """
        Atualiza dados de uma colheita
        
        Args:
            id_colheita (int): ID da colheita
            dados_atualizados (dict): Campos a atualizar
            
        Returns:
            tuple: (sucesso: bool, mensagem: str)
        """
        colheita = self.buscar_por_id(id_colheita)
        
        if colheita is None:
            return (False, "❌ Colheita não encontrada!")
        
        try:
            # Atualizar campos permitidos
            campos_editaveis = ['observacoes', 'percentual_perda', 'velocidade']
            
            for campo, valor in dados_atualizados.items():
                if campo in campos_editaveis:
                    colheita[campo] = valor
            
            # Recalcular valores derivados se perda foi alterada
            if 'percentual_perda' in dados_atualizados:
                colheita['toneladas_perdidas'] = calcular_perda_toneladas(
                    colheita['area_hectares'],
                    colheita['produtividade'],
                    colheita['percentual_perda']
                )
                colheita['perda_financeira'] = calcular_perda_financeira_completa(
                    colheita['area_hectares'],
                    colheita['produtividade'],
                    colheita['percentual_perda'],
                    colheita['preco_tonelada']
                )
                colheita['toneladas_colhidas'] = calcular_toneladas_colhidas(
                    colheita['area_hectares'],
                    colheita['produtividade'],
                    colheita['percentual_perda']
                )
                colheita['eficiencia'] = calcular_eficiencia_colheita(colheita['percentual_perda'])
                colheita['classificacao'] = classificar_nivel_perda(colheita['percentual_perda'])
            
            return (True, "✅ Colheita atualizada!")
        
        except Exception as e:
            return (False, f"❌ Erro ao atualizar: {str(e)}")
    
    def remover_colheita(self, id_colheita: int) -> tuple:
        """
        Remove colheita da lista
        
        Args:
            id_colheita (int): ID da colheita
            
        Returns:
            tuple: (sucesso: bool, mensagem: str)
        """
        colheita = self.buscar_por_id(id_colheita)
        
        if colheita is None:
            return (False, "❌ Colheita não encontrada!")
        
        self.colheitas.remove(colheita)
        return (True, "✅ Colheita removida!")
    
    def obter_estatisticas(self) -> dict:
        """
        Calcula estatísticas gerais das colheitas
        
        Returns:
            dict: Dicionário com estatísticas
        """
        if not self.colheitas:
            return {
                'total_colheitas': 0,
                'area_total': 0.0,
                'perda_media': 0.0,
                'perda_total_financeira': 0.0,
                'toneladas_perdidas_total': 0.0,
                'eficiencia_media': 0.0
            }
        
        total = len(self.colheitas)
        area_total = sum(c['area_hectares'] for c in self.colheitas)
        perda_media = sum(c['percentual_perda'] for c in self.colheitas) / total
        perda_financeira_total = sum(c['perda_financeira'] for c in self.colheitas)
        toneladas_perdidas = sum(c['toneladas_perdidas'] for c in self.colheitas)
        eficiencia_media = sum(c['eficiencia'] for c in self.colheitas) / total
        
        return {
            'total_colheitas': total,
            'area_total': area_total,
            'perda_media': perda_media,
            'perda_total_financeira': perda_financeira_total,
            'toneladas_perdidas_total': toneladas_perdidas,
            'eficiencia_media': eficiencia_media
        }
    
    def obter_ranking_fazendas(self) -> list:
        """
        Retorna ranking de fazendas por eficiência
        
        Returns:
            list: Lista de dicionários com fazenda e eficiência média
        """
        # Dicionário para agrupar por fazenda
        fazendas_dict = {}
        
        for colheita in self.colheitas:
            fazenda = colheita['fazenda']
            
            if fazenda not in fazendas_dict:
                fazendas_dict[fazenda] = {
                    'fazenda': fazenda,
                    'total_colheitas': 0,
                    'soma_eficiencia': 0.0,
                    'soma_perda': 0.0
                }
            
            fazendas_dict[fazenda]['total_colheitas'] += 1
            fazendas_dict[fazenda]['soma_eficiencia'] += colheita['eficiencia']
            fazendas_dict[fazenda]['soma_perda'] += colheita['percentual_perda']
        
        # Calcular médias e criar lista
        ranking = []
        for dados in fazendas_dict.values():
            ranking.append({
                'fazenda': dados['fazenda'],
                'colheitas': dados['total_colheitas'],
                'eficiencia_media': dados['soma_eficiencia'] / dados['total_colheitas'],
                'perda_media': dados['soma_perda'] / dados['total_colheitas']
            })
        
        # Ordenar por eficiência (maior primeiro)
        ranking.sort(key=lambda x: x['eficiencia_media'], reverse=True)
        
        return ranking
    
    def obter_totalizacao_por_tipo_cana(self) -> dict:
        """
        Totaliza dados por tipo de cana
        
        Returns:
            dict: Dicionário com tipo de cana como chave
        """
        totalizacao = {}
        
        for colheita in self.colheitas:
            tipo = colheita['tipo_cana']
            
            if tipo not in totalizacao:
                totalizacao[tipo] = {
                    'quantidade': 0,
                    'area_total': 0.0,
                    'perda_media': 0.0,
                    'soma_perda': 0.0
                }
            
            totalizacao[tipo]['quantidade'] += 1
            totalizacao[tipo]['area_total'] += colheita['area_hectares']
            totalizacao[tipo]['soma_perda'] += colheita['percentual_perda']
        
        # Calcular médias
        for tipo in totalizacao:
            totalizacao[tipo]['perda_media'] = (
                totalizacao[tipo]['soma_perda'] / totalizacao[tipo]['quantidade']
            )
        
        return totalizacao
    
    def exportar_para_lista_simples(self) -> list:
        """
        Exporta colheitas como lista de listas (para CSV, etc)
        
        Returns:
            list: Lista de listas com dados
        """
        dados = []
        
        # Cabeçalho
        dados.append([
            'ID', 'Fazenda', 'Área (ha)', 'Tipo Cana', 'Produtividade',
            'Perda (%)', 'Perda (t)', 'Perda (R$)', 'Eficiência (%)',
            'Classificação', 'Data'
        ])
        
        # Dados
        for c in self.colheitas:
            dados.append([
                c['id'],
                c['fazenda'],
                c['area_hectares'],
                c['tipo_cana'],
                c['produtividade'],
                c['percentual_perda'],
                c['toneladas_perdidas'],
                c['perda_financeira'],
                c['eficiencia'],
                c['classificacao'],
                c['data_colheita']
            ])
        
        return dados
