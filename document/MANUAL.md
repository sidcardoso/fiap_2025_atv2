# 📚 Manual do Sistema CanaOptimizer

## 🎯 Visão Geral

O **CanaOptimizer** é um sistema desenvolvido em Python para monitoramento e análise de perdas na colheita mecanizada de cana-de-açúcar. O sistema permite:

- ✅ Registrar dados de colheitas
- ✅ Calcular perdas em toneladas e valores financeiros
- ✅ Gerar relatórios e estatísticas
- ✅ Exportar dados em JSON
- ✅ Simular cenários de redução de perdas

---

## 🔧 Instalação e Configuração

### Pré-requisitos

- Python 3.8 ou superior
- Biblioteca `oracledb` (para conexão com Oracle Database - opcional)

### Instalação

1. **Clone ou extraia o projeto**
```bash
cd c:\pessoal\fiap\entrega2\entrega3
```

2. **Instale dependências (opcional)**
```bash
pip install oracledb
```

3. **Configure banco de dados (opcional)**
   - Edite o arquivo `config.py`
   - Atualize credenciais em `DATABASE_CONFIG`

### Executar o Sistema

```bash
python main.py
```

---

## 📂 Estrutura do Projeto

```
entrega3/
├── main.py                    # Aplicação principal
├── config.py                  # Configurações e constantes
├── README.md                  # Documentação do problema
├── docs/
│   └── MANUAL.md             # Este manual
├── modules/
│   ├── validations.py        # Funções de validação
│   ├── calculations.py       # Cálculos matemáticos
│   └── colheita_manager.py   # Gerenciador de colheitas
├── utils/
│   └── file_handler.py       # Manipulação de arquivos
├── database/
│   ├── connection.py         # Conexão Oracle (planejado)
│   ├── queries.py            # Consultas SQL (planejado)
│   └── setup.sql             # Scripts SQL (planejado)
└── data/
    └── exports/              # Arquivos exportados
```

---

## 🎮 Como Usar

### Menu Principal

Ao iniciar o sistema, você verá o menu principal:

```
📋 MENU PRINCIPAL
1️⃣  - Registrar Nova Colheita
2️⃣  - Consultar Colheitas
3️⃣  - Atualizar Colheita
4️⃣  - Remover Colheita
5️⃣  - Relatórios e Estatísticas
6️⃣  - Exportar Dados
7️⃣  - Calcular Simulações
8️⃣  - Gerenciar Arquivos
0️⃣  - Sair
```

### 1️⃣ Registrar Nova Colheita

Permite registrar dados de uma colheita realizada:

**Informações solicitadas:**
- Nome da fazenda
- Área colhida (hectares)
- Tipo de cana (ex: RB867515, CTC4)
- Produtividade esperada (t/ha)
- Percentual de perda observado (%)
- Preço da tonelada (R$)
- Marca da colheitadeira
- Velocidade de operação (km/h)
- Condição climática
- Data da colheita
- Observações adicionais

**Exemplo de uso:**
```
Nome da fazenda: Fazenda São João
Área colhida: 50
Produtividade: 95
Tipo de cana: 2 (RB867515)
Perda: 4.5
Preço: 120
Colheitadeira: 2 (John Deere)
Velocidade: 5.5
Clima: 1 (Ensolarado)
```

O sistema calcula automaticamente:
- Toneladas perdidas
- Perda financeira
- Eficiência da colheita
- Classificação do nível de perda

### 2️⃣ Consultar Colheitas

Permite visualizar colheitas registradas com 4 opções:

**2.1 - Listar todas**
- Exibe todas as colheitas registradas

**2.2 - Buscar por fazenda**
- Filtra colheitas de uma fazenda específica

**2.3 - Filtrar por classificação**
- Filtra por: Ótima, Boa, Regular, Alta ou Crítica

**2.4 - Buscar por ID**
- Busca uma colheita específica pelo ID

**Informações exibidas:**
```
🆔 ID: 1 | 🌾 Fazenda: Fazenda São João
📅 Data: 15/05/2024 | 📏 Área: 50.00 ha
🌱 Tipo: RB867515 | 📊 Produtividade: 95.00 t/ha
⚠️  Perda: 4.50% (21.38 t)
💰 Perda financeira: R$ 2,565.00
✅ Eficiência: 95.50% | 📊 Classificação: Ótima
🚜 Colheitadeira: John Deere | ⚡ 5.5 km/h
🌤️  Clima: Ensolarado
```

### 5️⃣ Relatórios e Estatísticas

Gera análises detalhadas dos dados:

**5.1 - Estatísticas Gerais**
- Total de colheitas
- Área total colhida
- Perda média percentual
- Toneladas perdidas (total)
- Perda financeira total
- Eficiência média

**5.2 - Ranking de Fazendas**
- Ranking por eficiência
- Perda média por fazenda
- Número de colheitas

**5.3 - Análise por Tipo de Cana**
- Quantidade de colheitas por tipo
- Área total por tipo
- Perda média por tipo

**5.4 - Gerar Relatório Completo (TXT)**
- Gera arquivo texto com análise completa
- Salvo em `data/exports/`
- Inclui timestamp no nome

### 6️⃣ Exportar Dados

Exporta todas as colheitas para arquivo JSON:

**Estrutura do JSON:**
```json
{
  "metadata": {
    "data_exportacao": "20/05/2024 14:30:00",
    "total_registros": 10,
    "sistema": "CanaOptimizer"
  },
  "colheitas": [
    {
      "id": 1,
      "fazenda": "Fazenda São João",
      "area_hectares": 50.0,
      "tipo_cana": "RB867515",
      "percentual_perda": 4.5,
      "toneladas_perdidas": 21.38,
      "perda_financeira": 2565.00,
      ...
    }
  ]
}
```

### 7️⃣ Calcular Simulações

Realiza cálculos e projeções:

**7.1 - Simular perda em toneladas**
- Calcula perda em toneladas
- Baseado em área, produtividade e % de perda

**7.2 - Simular perda financeira**
- Calcula impacto financeiro
- Multiplica toneladas perdidas pelo preço

**7.3 - Calcular economia potencial**
- Simula economia ao reduzir perda
- Compara perda atual vs. perda alvo

**7.4 - Projetar economia anual**
- Projeta economia para múltiplas safras
- Considera número de safras por ano

**Exemplo:**
```
📊 DADOS PARA SIMULAÇÃO
Área: 100
Produtividade: 100
Perda atual: 15
Preço: 120
Perda alvo: 5
Safras/ano: 2

📊 RESULTADOS
💰 Economia projetada anual: R$ 240,000.00
📊 Com 2 safra(s) por ano
```

### 8️⃣ Gerenciar Arquivos

Lista arquivos exportados:
- Nome do arquivo
- Tipo (TXT ou JSON)
- Tamanho
- Data de modificação
- Caminho completo

---

## 🧮 Cálculos Realizados

### Perda em Toneladas
```
Toneladas Perdidas = Área × Produtividade × (Perda% / 100)
```

### Perda Financeira
```
Perda Financeira = Toneladas Perdidas × Preço por Tonelada
```

### Toneladas Colhidas
```
Toneladas Colhidas = (Área × Produtividade) - Toneladas Perdidas
```

### Eficiência da Colheita
```
Eficiência = 100 - Perda%
```

### Economia Potencial
```
Economia = (Perda Atual - Perda Meta) × Área × Produtividade × Preço / 100
```

### Projeção Anual
```
Economia Anual = Economia Potencial × Número de Safras por Ano
```

---

## 📊 Classificação de Perdas

| Perda (%)      | Classificação | Cor  |
|----------------|---------------|------|
| 0% - 5%        | Ótima         | 🟢   |
| 5% - 8%        | Boa           | 🟡   |
| 8% - 12%       | Regular       | 🟠   |
| 12% - 15%      | Alta          | 🔴   |
| Acima de 15%   | Crítica       | 🔴🔴 |

---

## 🔍 Validações Implementadas

O sistema valida todas as entradas:

- ✅ Números positivos (área, produtividade, velocidade)
- ✅ Percentuais (0-100%)
- ✅ Textos não vazios (nomes de fazendas)
- ✅ Opções de menu
- ✅ Escolhas de listas

**Exemplos de mensagens de erro:**
```
❌ O valor deve ser um número positivo!
❌ O percentual deve estar entre 0 e 100!
❌ O campo não pode estar vazio!
❌ Opção inválida! Tente novamente.
```

---

## 📦 Estruturas de Dados

### Tuplas (Imutáveis)
Usadas para constantes do negócio:
```python
TIPOS_CANA = ('SP81-3250', 'RB867515', 'RB966928', 'CTC4', 'CTC9', ...)
MARCAS_COLHEITADEIRAS = ('Case IH', 'John Deere', 'New Holland', ...)
CONDICOES_CLIMATICAS = ('Ensolarado', 'Nublado', 'Chuva Leve', ...)
```

### Listas
Usadas para coleções dinâmicas:
```python
colheitas = []  # Lista de colheitas
colheitas.append(nova_colheita)  # Adicionar
colheitas.remove(colheita)       # Remover
```

### Dicionários
Usados para dados estruturados:
```python
colheita = {
    'id': 1,
    'fazenda': 'São João',
    'area_hectares': 50.0,
    'percentual_perda': 4.5,
    'toneladas_perdidas': 21.38
}
```

---

## 📝 Funções com Parâmetros

Todas as funções recebem parâmetros e retornam tuplas:

### Exemplo: Validação
```python
def validar_numero_positivo(valor_str: str, nome_campo: str) -> tuple:
    """
    Args:
        valor_str (str): String com número
        nome_campo (str): Nome do campo (para mensagens)
    
    Returns:
        tuple: (valido: bool, numero: float, mensagem: str)
    """
    ...
    return (True, numero, "")
```

### Exemplo: Cálculo
```python
def calcular_perda_toneladas(area: float, produtividade: float, 
                              percentual: float) -> float:
    """
    Args:
        area (float): Área em hectares
        produtividade (float): Toneladas por hectare
        percentual (float): Percentual de perda
    
    Returns:
        float: Toneladas perdidas
    """
    ...
    return toneladas_perdidas
```

---

## 📄 Manipulação de Arquivos

### Arquivos Texto (.txt)
```python
# Salvar
salvar_relatorio_texto("relatorio", conteudo)

# Ler
sucesso, conteudo, mensagem = ler_relatorio_texto(caminho)
```

### Arquivos JSON (.json)
```python
# Salvar
salvar_dados_json("dados", dicionario)

# Ler
sucesso, dados, mensagem = ler_dados_json(caminho)
```

**Localização:** Todos os arquivos são salvos em `data/exports/`

---

## 🎓 Conceitos Demonstrados

### ✅ Funções com Passagem de Parâmetros
- Todas as funções recebem parâmetros
- Parâmetros com tipo anotado (type hints)
- Retorno de valores e tuplas

### ✅ Estruturas de Dados
- **Listas:** Coleções dinâmicas de colheitas
- **Tuplas:** Constantes imutáveis (tipos de cana, marcas)
- **Dicionários:** Dados estruturados (colheitas, configurações)

### ✅ Manipulação de Arquivos
- **Texto:** Relatórios formatados (.txt)
- **JSON:** Exportação de dados estruturados

### ✅ Validação de Dados
- Funções de validação reutilizáveis
- Tratamento de exceções
- Mensagens de erro claras

### ✅ Cálculos Matemáticos
- Operações aritméticas
- Porcentagens
- Agregações (soma, média)
- Projeções

---

## 💡 Dicas de Uso

1. **Dados de Exemplo**
   - O sistema cria 2 colheitas de exemplo automaticamente
   - Útil para testar funcionalidades

2. **Atalhos**
   - CTRL+C para cancelar operação
   - ENTER para valores padrão (quando indicado)

3. **Relatórios**
   - Gere relatórios regularmente
   - Arquivos são salvos com timestamp único

4. **Exportação**
   - Exporte dados antes de fechar o sistema
   - JSONs podem ser importados em outras ferramentas

5. **Simulações**
   - Use simulações para planejar melhorias
   - Meta recomendada: 5% de perda

---

## 🐛 Troubleshooting

### Problema: "Módulo não encontrado"
**Solução:** Verifique se está no diretório correto
```bash
cd c:\pessoal\fiap\entrega2\entrega3
python main.py
```

### Problema: Erro ao salvar arquivo
**Solução:** Verifique permissões da pasta `data/exports/`

### Problema: Caracteres especiais incorretos
**Solução:** O sistema usa UTF-8. Configure terminal:
```bash
chcp 65001  # Windows
```

---

## 📞 Suporte

**Projeto:** CanaOptimizer  
**Curso:** FIAP - Computational Thinking with Python  
**Problema:** Redução de perdas na colheita mecanizada de cana-de-açúcar  
**Impacto:** 15% de perdas = R$ 20 milhões anuais (São Paulo)

---

## 🚀 Próximas Funcionalidades

- [ ] Integração com Oracle Database
- [ ] Gráficos e visualizações
- [ ] Análise preditiva com Machine Learning
- [ ] Dashboard web
- [ ] API REST
- [ ] Aplicativo mobile

---

## 📄 Licença

Projeto acadêmico - FIAP 2024

---

**Desenvolvido com 💚 para o agronegócio brasileiro**
