import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

"""
CanaOptimizer - Operações CRUD no Banco de Dados Oracle
Demonstra: OPERAÇÕES CREATE, READ, UPDATE, DELETE
"""

from src.database.connection import OracleConnection
from datetime import datetime


class ColheitaCRUD:
    """Classe para operações CRUD de colheitas no banco Oracle"""
    
    def __init__(self, conexao: OracleConnection):
        """
        Inicializa CRUD com conexão existente
        
        Args:
            conexao (OracleConnection): Conexão ativa com Oracle
        """
        self.conexao = conexao
    
    # ========== CREATE ==========
    
    def inserir_colheita(self, colheita: dict) -> tuple:
        """
        Insere nova colheita no banco (CREATE)
        
        Args:
            colheita (dict): Dados da colheita
            
        Returns:
            tuple: (sucesso: bool, id: int, mensagem: str)
        """
        sql = """
            INSERT INTO COLHEITAS (
                FAZENDA, AREA_HECTARES, TIPO_CANA, PRODUTIVIDADE,
                PERCENTUAL_PERDA, PRECO_TONELADA, COLHEITADEIRA,
                VELOCIDADE, CONDICAO_CLIMA, DATA_COLHEITA,
                TONELADAS_COLHIDAS, TONELADAS_PERDIDAS,
                PERDA_FINANCEIRA, EFICIENCIA, CLASSIFICACAO, OBSERVACOES
            ) VALUES (
                :1, :2, :3, :4, :5, :6, :7, :8, :9, 
                TO_DATE(:10, 'DD/MM/YYYY'),
                :11, :12, :13, :14, :15, :16
            ) RETURNING ID_COLHEITA INTO :17
        """
        
        try:
            # Preparar parâmetros
            id_var = self.conexao.cursor.var(int)
            
            parametros = (
                colheita['fazenda'],
                colheita['area_hectares'],
                colheita['tipo_cana'],
                colheita['produtividade'],
                colheita['percentual_perda'],
                colheita['preco_tonelada'],
                colheita['colheitadeira'],
                colheita['velocidade'],
                colheita['condicao_clima'],
                colheita['data_colheita'],
                colheita['toneladas_colhidas'],
                colheita['toneladas_perdidas'],
                colheita['perda_financeira'],
                colheita['eficiencia'],
                colheita['classificacao'],
                colheita.get('observacoes', ''),
                id_var
            )
            
            # Executar
            sucesso, _, msg = self.conexao.executar_query(sql, parametros)
            
            if sucesso:
                self.conexao.commit()
                novo_id = id_var.getvalue()[0]
                return (True, novo_id, "✅ Colheita inserida com sucesso!")
            else:
                self.conexao.rollback()
                return (False, 0, msg)
        
        except Exception as e:
            self.conexao.rollback()
            return (False, 0, f"❌ Erro ao inserir: {str(e)}")
    
    # ========== READ ==========
    
    def buscar_por_id(self, id_colheita: int) -> tuple:
        """
        Busca colheita por ID (READ)
        
        Args:
            id_colheita (int): ID da colheita
            
        Returns:
            tuple: (sucesso: bool, colheita: dict, mensagem: str)
        """
        sql = """
            SELECT 
                ID_COLHEITA, FAZENDA, AREA_HECTARES, TIPO_CANA,
                PRODUTIVIDADE, PERCENTUAL_PERDA, PRECO_TONELADA,
                COLHEITADEIRA, VELOCIDADE, CONDICAO_CLIMA,
                TO_CHAR(DATA_COLHEITA, 'DD/MM/YYYY') AS DATA_COLHEITA,
                TONELADAS_COLHIDAS, TONELADAS_PERDIDAS,
                PERDA_FINANCEIRA, EFICIENCIA, CLASSIFICACAO, OBSERVACOES
            FROM COLHEITAS
            WHERE ID_COLHEITA = :1
        """
        
        sucesso, resultados, msg = self.conexao.executar_query(sql, (id_colheita,))
        
        if sucesso and len(resultados) > 0:
            return (True, resultados[0], "")
        elif sucesso:
            return (False, {}, "❌ Colheita não encontrada!")
        else:
            return (False, {}, msg)
    
    def listar_todas(self, limite: int = 100) -> tuple:
        """
        Lista todas as colheitas (READ)
        
        Args:
            limite (int): Número máximo de registros
            
        Returns:
            tuple: (sucesso: bool, colheitas: list, mensagem: str)
        """
        sql = """
            SELECT 
                ID_COLHEITA, FAZENDA, AREA_HECTARES, PERCENTUAL_PERDA,
                TONELADAS_PERDIDAS, PERDA_FINANCEIRA, CLASSIFICACAO,
                TO_CHAR(DATA_COLHEITA, 'DD/MM/YYYY') AS DATA_COLHEITA
            FROM COLHEITAS
            ORDER BY DATA_COLHEITA DESC, ID_COLHEITA DESC
            FETCH FIRST :1 ROWS ONLY
        """
        
        sucesso, resultados, msg = self.conexao.executar_query(sql, (limite,))
        
        if sucesso:
            return (True, resultados, "")
        else:
            return (False, [], msg)
    
    def buscar_por_fazenda(self, nome_fazenda: str) -> tuple:
        """
        Busca colheitas por nome da fazenda (READ com filtro)
        
        Args:
            nome_fazenda (str): Nome da fazenda
            
        Returns:
            tuple: (sucesso: bool, colheitas: list, mensagem: str)
        """
        sql = """
            SELECT 
                ID_COLHEITA, FAZENDA, AREA_HECTARES, PERCENTUAL_PERDA,
                CLASSIFICACAO, TO_CHAR(DATA_COLHEITA, 'DD/MM/YYYY') AS DATA_COLHEITA
            FROM COLHEITAS
            WHERE UPPER(FAZENDA) LIKE UPPER(:1)
            ORDER BY DATA_COLHEITA DESC
        """
        
        sucesso, resultados, msg = self.conexao.executar_query(
            sql, 
            (f'%{nome_fazenda}%',)
        )
        
        if sucesso:
            return (True, resultados, "")
        else:
            return (False, [], msg)
    
    def buscar_por_classificacao(self, classificacao: str) -> tuple:
        """
        Busca colheitas por classificação (READ com filtro)
        
        Args:
            classificacao (str): 'Ótima', 'Boa', 'Regular', 'Alta' ou 'Crítica'
            
        Returns:
            tuple: (sucesso: bool, colheitas: list, mensagem: str)
        """
        sql = """
            SELECT 
                ID_COLHEITA, FAZENDA, AREA_HECTARES, PERCENTUAL_PERDA,
                TONELADAS_PERDIDAS, CLASSIFICACAO
            FROM COLHEITAS
            WHERE CLASSIFICACAO = :1
            ORDER BY PERCENTUAL_PERDA
        """
        
        sucesso, resultados, msg = self.conexao.executar_query(sql, (classificacao,))
        
        if sucesso:
            return (True, resultados, "")
        else:
            return (False, [], msg)
    
    # ========== UPDATE ==========
    
    def atualizar_colheita(self, id_colheita: int, dados: dict) -> tuple:
        """
        Atualiza dados da colheita (UPDATE)
        
        Args:
            id_colheita (int): ID da colheita
            dados (dict): Campos a atualizar
            
        Returns:
            tuple: (sucesso: bool, mensagem: str)
        """
        # Campos permitidos para atualização
        campos_permitidos = {
            'percentual_perda': 'PERCENTUAL_PERDA',
            'velocidade': 'VELOCIDADE',
            'observacoes': 'OBSERVACOES',
            'toneladas_perdidas': 'TONELADAS_PERDIDAS',
            'perda_financeira': 'PERDA_FINANCEIRA',
            'eficiencia': 'EFICIENCIA',
            'classificacao': 'CLASSIFICACAO'
        }
        
        # Construir SET clause
        set_parts = []
        valores = []
        
        for campo_py, campo_sql in campos_permitidos.items():
            if campo_py in dados:
                set_parts.append(f"{campo_sql} = :{len(valores) + 1}")
                valores.append(dados[campo_py])
        
        if not set_parts:
            return (False, "❌ Nenhum campo válido para atualizar!")
        
        # Adicionar ID no final
        valores.append(id_colheita)
        
        sql = f"""
            UPDATE COLHEITAS 
            SET {', '.join(set_parts)}
            WHERE ID_COLHEITA = :{len(valores)}
        """
        
        try:
            sucesso, _, msg = self.conexao.executar_query(sql, tuple(valores))
            
            if sucesso:
                self.conexao.commit()
                return (True, "✅ Colheita atualizada com sucesso!")
            else:
                self.conexao.rollback()
                return (False, msg)
        
        except Exception as e:
            self.conexao.rollback()
            return (False, f"❌ Erro ao atualizar: {str(e)}")
    
    # ========== DELETE ==========
    
    def excluir_colheita(self, id_colheita: int) -> tuple:
        """
        Exclui colheita do banco (DELETE)
        
        Args:
            id_colheita (int): ID da colheita
            
        Returns:
            tuple: (sucesso: bool, mensagem: str)
        """
        sql = "DELETE FROM COLHEITAS WHERE ID_COLHEITA = :1"
        
        try:
            sucesso, _, msg = self.conexao.executar_query(sql, (id_colheita,))
            
            if sucesso:
                self.conexao.commit()
                return (True, "✅ Colheita excluída com sucesso!")
            else:
                self.conexao.rollback()
                return (False, msg)
        
        except Exception as e:
            self.conexao.rollback()
            return (False, f"❌ Erro ao excluir: {str(e)}")
    
    # ========== ESTATÍSTICAS ==========
    
    def obter_estatisticas(self) -> tuple:
        """
        Retorna estatísticas gerais das colheitas
        
        Returns:
            tuple: (sucesso: bool, stats: dict, mensagem: str)
        """
        sql = """
            SELECT 
                COUNT(*) AS TOTAL_COLHEITAS,
                SUM(AREA_HECTARES) AS AREA_TOTAL,
                AVG(PERCENTUAL_PERDA) AS PERDA_MEDIA,
                MIN(PERCENTUAL_PERDA) AS PERDA_MINIMA,
                MAX(PERCENTUAL_PERDA) AS PERDA_MAXIMA,
                SUM(TONELADAS_PERDIDAS) AS TONELADAS_PERDIDAS_TOTAL,
                SUM(PERDA_FINANCEIRA) AS PERDA_FINANCEIRA_TOTAL
            FROM COLHEITAS
        """
        
        sucesso, resultados, msg = self.conexao.executar_query(sql)
        
        if sucesso and len(resultados) > 0:
            return (True, resultados[0], "")
        else:
            return (False, {}, msg)
