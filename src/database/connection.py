"""
CanaOptimizer - Conexão com Banco de Dados Oracle
Demonstra: INTEGRAÇÃO COM BANCO DE DADOS ORACLE
"""

import oracledb
from config import DATABASE_CONFIG


class OracleConnection:
    """Gerencia conexão com banco de dados Oracle"""
    
    def __init__(self):
        """Inicializa conexão"""
        self.connection = None
        self.cursor = None
    
    def conectar(self) -> tuple:
        """
        Estabelece conexão com o banco de dados Oracle
        
        Returns:
            tuple: (sucesso: bool, mensagem: str)
        """
        try:
            # Conectar ao banco Oracle
            self.connection = oracledb.connect(
                user=DATABASE_CONFIG['user'],
                password=DATABASE_CONFIG['password'],
                dsn=DATABASE_CONFIG['dsn']
            )
            
            # Criar cursor
            self.cursor = self.connection.cursor()
            
            return (True, "✅ Conectado ao Oracle com sucesso!")
        
        except oracledb.Error as error:
            erro_str = str(error)
            if "ORA-01017" in erro_str:
                return (False, "❌ Usuário ou senha inválidos!")
            elif "ORA-12541" in erro_str or "ORA-12170" in erro_str:
                return (False, "❌ Não foi possível conectar ao servidor Oracle!")
            else:
                return (False, f"❌ Erro ao conectar: {erro_str}")
        
        except Exception as e:
            return (False, f"❌ Erro desconhecido: {str(e)}")
    
    def desconectar(self) -> tuple:
        """
        Fecha conexão com o banco de dados
        
        Returns:
            tuple: (sucesso: bool, mensagem: str)
        """
        try:
            if self.cursor:
                self.cursor.close()
            
            if self.connection:
                self.connection.close()
            
            return (True, "✅ Desconectado com sucesso!")
        
        except Exception as e:
            return (False, f"❌ Erro ao desconectar: {str(e)}")
    
    def commit(self):
        """Confirma transação"""
        if self.connection:
            self.connection.commit()
    
    def rollback(self):
        """Desfaz transação"""
        if self.connection:
            self.connection.rollback()
    
    def executar_query(self, sql: str, parametros: tuple = None) -> tuple:
        """
        Executa query SQL
        
        Args:
            sql (str): Query SQL
            parametros (tuple): Parâmetros da query
            
        Returns:
            tuple: (sucesso: bool, resultado: list, mensagem: str)
        """
        try:
            if not self.cursor:
                return (False, [], "❌ Cursor não disponível!")
            
            if parametros:
                self.cursor.execute(sql, parametros)
            else:
                self.cursor.execute(sql)
            
            # Se for SELECT, retornar resultados
            if sql.strip().upper().startswith('SELECT'):
                colunas = [desc[0] for desc in self.cursor.description]
                linhas = self.cursor.fetchall()
                
                # Converter para lista de dicionários
                resultados = []
                for linha in linhas:
                    resultado_dict = dict(zip(colunas, linha))
                    resultados.append(resultado_dict)
                
                return (True, resultados, "")
            
            # Se for INSERT/UPDATE/DELETE, retornar linhas afetadas
            else:
                linhas_afetadas = self.cursor.rowcount
                return (True, [], f"✅ {linhas_afetadas} linha(s) afetada(s)")
        
        except oracledb.Error as error:
            return (False, [], f"❌ Erro SQL: {str(error)}")
        
        except Exception as e:
            return (False, [], f"❌ Erro: {str(e)}")
    
    def verificar_conexao(self) -> bool:
        """
        Verifica se está conectado
        
        Returns:
            bool: True se conectado
        """
        try:
            if self.connection and self.cursor:
                self.cursor.execute("SELECT 1 FROM DUAL")
                return True
            return False
        except:
            return False


# Função auxiliar para facilitar uso
def obter_conexao() -> OracleConnection:
    """
    Retorna nova conexão Oracle
    
    Returns:
        OracleConnection: Objeto de conexão
    """
    return OracleConnection()
