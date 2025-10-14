import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

"""
CanaOptimizer - Exemplo de Uso do Banco de Dados Oracle
Demonstra operações CRUD (Create, Read, Update, Delete)

IMPORTANTE: Para executar este exemplo:
1. Configure suas credenciais em config.py
2. Execute o script setup.sql no Oracle SQL Developer ou SQLPlus
3. Instale o driver: pip install oracledb
"""

from src.database.connection import obter_conexao
from src.database.crud import ColheitaCRUD
from datetime import datetime


def exemplo_completo_crud():
    """Demonstra todas as operações CRUD"""
    
    print("=" * 80)
    print("🌾 CANAOPTIMIZER - EXEMPLO DE BANCO DE DADOS ORACLE")
    print("=" * 80)
    
    # ========== 1. CONECTAR ==========
    print("\n📌 PASSO 1: Conectando ao banco Oracle...")
    print("-" * 80)
    
    conexao = obter_conexao()
    sucesso, mensagem = conexao.conectar()
    print(mensagem)
    
    if not sucesso:
        print("\n❌ Não foi possível conectar ao banco de dados!")
        print("   Verifique as configurações em config.py")
        print("   Certifique-se de que o Oracle está rodando")
        return
    
    # Criar objeto CRUD
    crud = ColheitaCRUD(conexao)
    
    try:
        # ========== 2. CREATE - Inserir nova colheita ==========
        print("\n📌 PASSO 2: Inserindo nova colheita (CREATE)...")
        print("-" * 80)
        
        nova_colheita = {
            'fazenda': 'Fazenda Teste Python',
            'area_hectares': 80.0,
            'tipo_cana': 'RB867515',
            'produtividade': 100.0,
            'percentual_perda': 5.5,
            'preco_tonelada': 120.0,
            'colheitadeira': 'John Deere',
            'velocidade': 5.8,
            'condicao_clima': 'Ensolarado',
            'data_colheita': datetime.now().strftime('%d/%m/%Y'),
            'toneladas_colhidas': 7560.0,
            'toneladas_perdidas': 440.0,
            'perda_financeira': 52800.0,
            'eficiencia': 94.5,
            'classificacao': 'Boa',
            'observacoes': 'Colheita de teste via Python'
        }
        
        sucesso, novo_id, msg = crud.inserir_colheita(nova_colheita)
        print(msg)
        
        if sucesso:
            print(f"   📋 ID gerado: {novo_id}")
            id_teste = novo_id
        else:
            print("\n⚠️  Não foi possível prosseguir com os exemplos")
            return
        
        # ========== 3. READ - Buscar por ID ==========
        print("\n📌 PASSO 3: Buscando colheita por ID (READ)...")
        print("-" * 80)
        
        sucesso, colheita, msg = crud.buscar_por_id(id_teste)
        
        if sucesso:
            print("✅ Colheita encontrada:")
            print(f"   ID: {colheita['ID_COLHEITA']}")
            print(f"   Fazenda: {colheita['FAZENDA']}")
            print(f"   Área: {colheita['AREA_HECTARES']} ha")
            print(f"   Perda: {colheita['PERCENTUAL_PERDA']}%")
            print(f"   Classificação: {colheita['CLASSIFICACAO']}")
        else:
            print(msg)
        
        # ========== 4. READ - Listar todas ==========
        print("\n📌 PASSO 4: Listando todas as colheitas (READ)...")
        print("-" * 80)
        
        sucesso, colheitas, msg = crud.listar_todas(limite=5)
        
        if sucesso:
            print(f"✅ Total de colheitas: {len(colheitas)}")
            print("\n📋 Últimas 5 colheitas:")
            for col in colheitas:
                print(f"   • ID {col['ID_COLHEITA']}: {col['FAZENDA']} - "
                      f"Perda {col['PERCENTUAL_PERDA']}% ({col['CLASSIFICACAO']})")
        else:
            print(msg)
        
        # ========== 5. READ - Buscar por fazenda ==========
        print("\n📌 PASSO 5: Buscando por nome da fazenda (READ com filtro)...")
        print("-" * 80)
        
        sucesso, colheitas, msg = crud.buscar_por_fazenda("Teste")
        
        if sucesso:
            print(f"✅ Encontradas {len(colheitas)} colheita(s) com 'Teste' no nome:")
            for col in colheitas:
                print(f"   • {col['FAZENDA']} - Perda {col['PERCENTUAL_PERDA']}%")
        else:
            print(msg)
        
        # ========== 6. READ - Buscar por classificação ==========
        print("\n📌 PASSO 6: Buscando por classificação (READ com filtro)...")
        print("-" * 80)
        
        sucesso, colheitas, msg = crud.buscar_por_classificacao("Ótima")
        
        if sucesso:
            print(f"✅ Colheitas com classificação 'Ótima': {len(colheitas)}")
            for col in colheitas[:3]:  # Mostrar apenas 3
                print(f"   • {col['FAZENDA']} - Perda {col['PERCENTUAL_PERDA']}%")
        else:
            print(msg)
        
        # ========== 7. UPDATE - Atualizar colheita ==========
        print("\n📌 PASSO 7: Atualizando colheita (UPDATE)...")
        print("-" * 80)
        
        dados_atualizacao = {
            'percentual_perda': 4.8,
            'observacoes': 'Atualizado via Python - perda reduzida!',
            'classificacao': 'Ótima'
        }
        
        sucesso, msg = crud.atualizar_colheita(id_teste, dados_atualizacao)
        print(msg)
        
        if sucesso:
            # Buscar novamente para confirmar
            sucesso2, colheita_atualizada, _ = crud.buscar_por_id(id_teste)
            if sucesso2:
                print(f"   📊 Nova perda: {colheita_atualizada['PERCENTUAL_PERDA']}%")
                print(f"   📝 Observações: {colheita_atualizada['OBSERVACOES']}")
        
        # ========== 8. READ - Estatísticas ==========
        print("\n📌 PASSO 8: Obtendo estatísticas gerais (READ agregado)...")
        print("-" * 80)
        
        sucesso, stats, msg = crud.obter_estatisticas()
        
        if sucesso:
            print("✅ Estatísticas Gerais:")
            print(f"   📊 Total de colheitas: {stats['TOTAL_COLHEITAS']}")
            print(f"   📐 Área total: {stats['AREA_TOTAL']:.2f} ha")
            print(f"   📉 Perda média: {stats['PERDA_MEDIA']:.2f}%")
            print(f"   ⬇️  Perda mínima: {stats['PERDA_MINIMA']:.2f}%")
            print(f"   ⬆️  Perda máxima: {stats['PERDA_MAXIMA']:.2f}%")
            print(f"   💰 Perda financeira total: R$ {stats['PERDA_FINANCEIRA_TOTAL']:,.2f}")
        else:
            print(msg)
        
        # ========== 9. DELETE - Excluir colheita ==========
        print("\n📌 PASSO 9: Excluindo colheita de teste (DELETE)...")
        print("-" * 80)
        
        # Perguntar se deseja excluir
        resposta = input("   ⚠️  Deseja realmente excluir a colheita de teste? (s/n): ")
        
        if resposta.lower() == 's':
            sucesso, msg = crud.excluir_colheita(id_teste)
            print(msg)
            
            if sucesso:
                # Tentar buscar para confirmar exclusão
                sucesso2, _, _ = crud.buscar_por_id(id_teste)
                if not sucesso2:
                    print("   ✅ Exclusão confirmada - registro não existe mais")
        else:
            print("   ℹ️  Exclusão cancelada - colheita mantida no banco")
    
    except Exception as e:
        print(f"\n❌ Erro durante execução: {str(e)}")
    
    finally:
        # ========== 10. DESCONECTAR ==========
        print("\n📌 PASSO 10: Desconectando...")
        print("-" * 80)
        
        sucesso, mensagem = conexao.desconectar()
        print(mensagem)
    
    # ========== RESUMO ==========
    print("\n" + "=" * 80)
    print("✅ RESUMO DAS OPERAÇÕES CRUD")
    print("=" * 80)
    print("\n1️⃣  CREATE  : Inserir nova colheita")
    print("2️⃣  READ    : Buscar por ID")
    print("3️⃣  READ    : Listar todas")
    print("4️⃣  READ    : Filtrar por fazenda")
    print("5️⃣  READ    : Filtrar por classificação")
    print("6️⃣  UPDATE  : Atualizar dados")
    print("7️⃣  READ    : Obter estatísticas")
    print("8️⃣  DELETE  : Excluir registro")
    print("\n💡 Todas as operações CRUD foram demonstradas com sucesso!")
    print("=" * 80)


def exemplo_rapido():
    """Exemplo rápido sem interação"""
    
    print("\n🚀 TESTE RÁPIDO DE CONEXÃO")
    print("-" * 80)
    
    conexao = obter_conexao()
    sucesso, mensagem = conexao.conectar()
    print(mensagem)
    
    if sucesso:
        # Verificar conexão
        if conexao.verificar_conexao():
            print("✅ Conexão ativa e funcionando!")
            
            # Executar query simples
            sucesso_q, resultado, _ = conexao.executar_query(
                "SELECT COUNT(*) AS TOTAL FROM COLHEITAS"
            )
            
            if sucesso_q and len(resultado) > 0:
                print(f"📊 Total de colheitas no banco: {resultado[0]['TOTAL']}")
        
        conexao.desconectar()
    else:
        print("❌ Falha na conexão - verifique config.py")


if __name__ == "__main__":
    import sys
    
    print("\n" + "=" * 80)
    print("🌾 CANAOPTIMIZER - EXEMPLOS DE BANCO DE DADOS ORACLE".center(80))
    print("=" * 80)
    
    print("\nEscolha uma opção:")
    print("1 - Exemplo completo (CRUD interativo)")
    print("2 - Teste rápido de conexão")
    print("0 - Sair")
    
    try:
        opcao = input("\nOpção: ").strip()
        
        if opcao == "1":
            exemplo_completo_crud()
        elif opcao == "2":
            exemplo_rapido()
        elif opcao == "0":
            print("\n👋 Até logo!")
        else:
            print("\n⚠️  Opção inválida!")
    
    except KeyboardInterrupt:
        print("\n\n⚠️  Operação cancelada pelo usuário")
    except Exception as e:
        print(f"\n❌ Erro: {str(e)}")
