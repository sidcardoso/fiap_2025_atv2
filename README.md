# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width="40%" height="40%"></a>
</p>

<br>

# CanaOptimizer - Sistema de Monitoramento de Colheita

## Sidney de Lirio Cardoso - RM567808

**FarmTech Solutions**

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/seu-linkedin">Sidney de Lirio Cardoso (RM: 567808)</a>

## 👩‍🏫 Professores:

### Tutor(a) 

### Coordenador(a)

---

## 📜 Descrição

O **CanaOptimizer** é um sistema desenvolvido em Python para enfrentar um dos maiores desafios do agronegócio brasileiro: as perdas na colheita mecanizada de cana-de-açúcar.

### 🎯 O Problema

No Brasil, a colheita mecanizada de cana-de-açúcar enfrenta um desafio crítico: **perdas de até 15% da produção**, resultando em **prejuízos estimados em R$ 20 milhões anuais** apenas no estado de São Paulo. Essas perdas ocorrem devido a diversos fatores:

- Calibração inadequada das colheitadeiras
- Velocidade de operação incorreta
- Condições climáticas adversas
- Falta de monitoramento em tempo real
- Ausência de dados históricos para análise

### 💡 A Solução

O CanaOptimizer é um sistema computacional completo que permite:

✅ **Registro detalhado** de operações de colheita com todos os parâmetros relevantes  
✅ **Cálculos automáticos** de perdas em toneladas e valores financeiros  
✅ **Classificação inteligente** do nível de perdas (Ótima, Boa, Aceitável, Ruim, Crítica)  
✅ **Geração de relatórios** formatados em texto e exportação em JSON  
✅ **Simulações** de cenários para redução de perdas  
✅ **Integração com banco de dados Oracle** para persistência de dados  
✅ **Estatísticas e comparações** entre diferentes colheitas  

### 🎯 Objetivos do Projeto

1. **Reduzir perdas**: Fornecer dados precisos para otimização das operações
2. **Economizar recursos**: Calcular economia potencial com melhorias
3. **Apoiar decisões**: Gerar relatórios para gestores e operadores
4. **Criar histórico**: Manter banco de dados para análise temporal
5. **Simular cenários**: Projetar resultados de diferentes estratégias

---

## 📁 Estrutura de pastas

```
fiap_2025_atv2/
├── .github/                    # Configurações GitHub
├── assets/                     # Imagens e recursos
│   └── logo-fiap.png
├── config/                     # Arquivos de configuração
│   └── config.py              # Configurações do sistema
├── document/                   # Documentação do projeto
│   ├── CHECKLIST.md           # Checklist completo
│   ├── MANUAL.md              # Manual de uso
│   └── README_PROJETO.md      # Documentação técnica
├── scripts/                    # Scripts auxiliares
│   └── setup_database.sql     # Script SQL de setup
├── src/                        # Código fonte
│   ├── app.py                 # Aplicação principal (ENTREGA)
│   ├── main.py                # Menu interativo completo
│   ├── exemplos.py            # Demonstrações
│   ├── modules/               # Módulos Python
│   │   ├── validations.py     # Validações
│   │   ├── calculations.py    # Cálculos
│   │   └── colheita_manager.py # Gerenciador
│   ├── utils/                 # Utilitários
│   │   └── file_handler.py    # Manipulação de arquivos
│   ├── database/              # Integração BD
│   │   ├── connection.py      # Conexão Oracle
│   │   ├── crud.py            # Operações CRUD
│   │   └── exemplo_uso.py     # Exemplos BD
│   └── data/                  # Dados e exports
│       └── exports/           # Arquivos exportados
├── .gitignore                 # Arquivos ignorados
└── README.md                  # Este arquivo
```

### 📂 Descrição das Pastas

- **`.github`**: Configurações específicas do GitHub para gerenciar e automatizar processos
- **`assets`**: Imagens, logos e recursos visuais do projeto
- **`config`**: Arquivos de configuração (constantes, parâmetros, credenciais)
- **`document`**: Toda a documentação do projeto (manuais, checklists, guias)
- **`scripts`**: Scripts auxiliares para setup, deploy e tarefas específicas
- **`src`**: Todo o código fonte desenvolvido nas diferentes fases do projeto

---

## 🎓 Conceitos Demonstrados

Este projeto demonstra **todos** os conceitos exigidos pela disciplina:

### ✅ 1. Funções com Passagem de Parâmetros (21 funções)

**Validações** (`modules/validations.py`):
- `validar_numero_positivo(valor_str, nome_campo)` - Valida números positivos
- `validar_percentual(valor_str, nome_campo)` - Valida percentuais 0-100
- `validar_texto_nao_vazio(texto, nome_campo)` - Valida strings
- `validar_opcao_menu(opcao_str, min_opcao, max_opcao)` - Valida opções
- E mais 6 funções...

**Cálculos** (`modules/calculations.py`):
- `calcular_perda_toneladas(area, produtividade, percentual)` - Calcula perdas
- `calcular_perda_financeira(perda_toneladas, preco)` - Calcula valores
- `calcular_eficiencia_colheita(percentual_perda)` - Calcula eficiência
- `classificar_nivel_perda(percentual_perda)` - Classifica perdas
- E mais 7 funções...

### ✅ 2. Estruturas de Dados

**Tuplas** (dados imutáveis em `config/config.py`):
```python
TIPOS_CANA = ('SP81-3250', 'RB867515', 'RB966928', 'CTC4', 'CTC9')
MARCAS_COLHEITADEIRAS = ('Case IH', 'John Deere', 'New Holland', 'Valtra')
CONDICOES_CLIMATICAS = ('Ensolarado', 'Nublado', 'Chuvoso', 'Seco')
```

**Listas** (coleções dinâmicas em `modules/colheita_manager.py`):
```python
self.colheitas = []  # Lista de colheitas
self.colheitas.append(nova_colheita)  # Adicionar
self.colheitas.remove(colheita)  # Remover
```

**Dicionários** (dados estruturados):
```python
colheita = {
    'id': 1,
    'fazenda': 'São João',
    'area_hectares': 50.0,
    'percentual_perda': 4.5,
    'classificacao': 'Ótima'
}
```

### ✅ 3. Manipulação de Arquivos

**Arquivos Texto** (`.txt` em `utils/file_handler.py`):
- Salvar relatórios formatados
- Ler relatórios salvos
- Gerar cabeçalhos e rodapés

**Arquivos JSON** (`.json`):
- Exportar dados estruturados
- Importar configurações
- Salvar backups de colheitas

### ✅ 4. Integração com Banco de Dados Oracle

**Conexão** (`database/connection.py`):
- Classe `OracleConnection` para gerenciar conexões
- Métodos para executar queries
- Controle de transações (commit/rollback)

**CRUD Completo** (`database/crud.py`):
- **CREATE**: `inserir_colheita(colheita)`
- **READ**: `buscar_por_id()`, `listar_todas()`, `buscar_por_fazenda()`
- **UPDATE**: `atualizar_colheita(id, dados)`
- **DELETE**: `excluir_colheita(id)`
- **STATS**: `obter_estatisticas()`

**Schema SQL** (`scripts/setup_database.sql`):
- Tabela `COLHEITAS` com 19 campos
- Sequences e triggers para auto-incremento
- Views para estatísticas e rankings
- Índices para performance

---

## 🔧 Como executar o código

### 📋 Pré-requisitos

- **Python 3.12+** ([Download](https://www.python.org/downloads/))
- **Oracle Database 11g+** (opcional, para funcionalidades de BD)
- **Git** ([Download](https://git-scm.com/downloads))

### 📦 Bibliotecas Python Necessárias

```bash
pip install oracledb  # Para integração com Oracle (opcional)
```

> **Nota**: O sistema funciona **sem banco de dados** usando apenas listas em memória. O Oracle é opcional para persistência.

---

### 🚀 Instalação e Execução

#### **Fase 1: Clone o Repositório**

```bash
# Clone o projeto
git clone https://github.com/sidcardoso/fiap_2025_atv2.git

# Entre no diretório
cd fiap_2025_atv2
```

#### **Fase 2: Execute os Exemplos**

```bash
# Entre no diretório src
cd src

# Execute o arquivo de exemplos para validar instalação
python exemplos.py
```

**Saída esperada:**
```
================================================================================
🌾 CANAOPTIMIZER - EXEMPLOS DE USO
================================================================================

📌 Exemplo 1: Demonstrando TUPLAS (Dados Imutáveis)
   ✅ 3 tuplas carregadas
   ✅ 7 tipos de cana disponíveis

[... 8 exemplos executados com sucesso ...]
```

#### **Fase 3: Execute a Aplicação Principal**

```bash
# Execute a aplicação principal (ENTREGA)
python app.py

# Ou execute o menu completo com todas as funcionalidades
python main.py
```

**Menu interativo:**
```
================================================================================
🌾 SISTEMA DE MONITORAMENTO DE COLHEITA - CANAOPTIMIZER
================================================================================

📋 MENU PRINCIPAL
1 - Registrar Nova Colheita
2 - Consultar Colheitas
3 - Atualizar Colheita
4 - Remover Colheita
5 - Relatórios e Estatísticas
6 - Exportar Dados (JSON)
7 - Calcular Simulações
8 - Gerenciar Arquivos
0 - Sair

Digite sua opção:
```

#### **Fase 4: Configurar Banco de Dados Oracle (Opcional)**

1. **Instale o driver Oracle**:
```bash
pip install oracledb
```

2. **Configure as credenciais** em `config/config.py`:
```python
DATABASE_CONFIG = {
    'user': 'seu_usuario',
    'password': 'sua_senha',
    'dsn': 'localhost:1521/XE'
}
```

3. **Execute o script SQL**:
```sql
-- No SQL*Plus ou SQL Developer
@scripts/setup_database.sql
```

4. **Teste a conexão**:
```bash
cd src/database
python exemplo_uso.py
```

---

## 📊 Funcionalidades Principais

### 1️⃣ Registro de Colheitas
- Informações da fazenda e operador
- Dados da área e produtividade
- Configurações da colheitadeira
- Condições climáticas
- Cálculo automático de perdas

### 2️⃣ Consultas e Filtros
- Listar todas as colheitas
- Buscar por fazenda
- Filtrar por classificação
- Buscar por ID
- Ordenação e visualização detalhada

### 3️⃣ Relatórios
- Relatório completo de colheita individual
- Estatísticas gerais do sistema
- Comparação entre colheitas
- Exportação em texto e JSON

### 4️⃣ Simulações
- Projeção de economia com redução de perdas
- Cálculo de tempo de colheita
- Comparação de cenários
- Metas de melhoria

### 5️⃣ Persistência
- Salvamento em memória (listas)
- Exportação em JSON
- Integração com Oracle Database
- Backup e recuperação de dados

---

## 🗃 Histórico de lançamentos

* **1.0.0 - 14/10/2025**
    * Versão completa com todos os requisitos
    * 21 funções implementadas
    * Integração Oracle completa
    * Sistema de arquivos (JSON/TXT)
    * Documentação completa
    * Testes validados

* **0.5.0 - 13/10/2025**
    * Implementação do banco de dados Oracle
    * CRUD completo
    * Scripts SQL com views e triggers

* **0.4.0 - 12/10/2025**
    * Sistema de arquivos (JSON e TXT)
    * Exportação e importação de dados
    * Geração de relatórios

* **0.3.0 - 11/10/2025**
    * Classe ColheitaManager
    * Operações com listas e dicionários
    * Menu interativo

* **0.2.0 - 10/10/2025**
    * Funções de cálculos (11 funções)
    * Simulações e projeções

* **0.1.0 - 09/10/2025**
    * Estrutura inicial do projeto
    * Funções de validação (10 funções)
    * Tuplas de configuração

---

## 📈 Estatísticas do Projeto

- **17 arquivos** Python + SQL
- **50+ funções** implementadas
- **~2.500 linhas** de código
- **5 documentos** de apoio
- **21 funções** com parâmetros
- **100% dos requisitos** atendidos

---

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/sidcardoso/fiap_2025_atv2">CanaOptimizer</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">FIAP</a> is licensed under <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>

---

## 🎯 Resultados Esperados

Ao utilizar o CanaOptimizer, espera-se:

✅ **Redução de 3-5%** nas perdas de colheita  
✅ **Economia de R$ 1-3 milhões** por safra  
✅ **Aumento de 5-10%** na eficiência operacional  
✅ **Decisões baseadas em dados** reais e históricos  
✅ **Melhoria contínua** através de monitoramento  

---

## � Arquivos para Entrega

### Atividade 2 - Python e além

**Arquivos principais:**
- **`src/app.py`**: Aplicação Python principal resolvendo problema do agronegócio
- **`README.md`**: Este arquivo com descrição completa da solução

**Links diretos no GitHub:**
- Código Python: `https://github.com/sidcardoso/fiap_2025_atv2/blob/main/src/app.py`
- README: `https://github.com/sidcardoso/fiap_2025_atv2/blob/main/README.md`

---

## �📞 Contato

Para dúvidas, sugestões ou mais informações sobre o projeto:

- **Repositório**: [github.com/sidcardoso/fiap_2025_atv2](https://github.com/sidcardoso/fiap_2025_atv2)
- **FIAP**: [www.fiap.com.br](https://www.fiap.com.br)

---

<p align="center">
<b>Desenvolvido com 💚 por FarmTech Solutions - FIAP 2025</b>
</p>
