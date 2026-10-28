 # StockFlow

API de controle de estoque em desenvolvimento, criada como projeto
de portfólio com Python, FastAPI e SQLAlchemy.

## Funcionalidades disponíveis

- Cadastro de produtos com nome, código e preço.
- Validação dos dados recebidos.
- Código único por produto, com rejeição de duplicados.
- Listagem dos produtos cadastrados.
- Consulta de produto pelo identificador.
- Persistência em banco SQLite.

## Tecnologias

- Python
- FastAPI
- Pydantic
- SQLAlchemy
- SQLite
- Uvicorn

## Como executar no Windows

Os comandos abaixo devem ser executados no Prompt de Comando (CMD),
com Python e Git instalados.

### 1. Clonar o repositório

```bat
git clone https://github.com/JazzyJeff6/StockFlow.git
cd StockFlow
```

### 2. Criar e ativar o ambiente virtual

```bat
python -m venv .venv
.venv\Scripts\activate.bat
```

### 3. Instalar as dependências

```bat
python -m pip install -r requirements.txt
```

### 4. Iniciar a API

```bat
python -m uvicorn main:app --reload
```

Acesse a documentação interativa:

http://127.0.0.1:8000/docs

O banco `stockflow.db` e as tabelas são criados na inicialização.
Execute o comando a partir da pasta principal do projeto.

## Endpoints disponíveis

| Método | Endereço | Função |
|---|---|---|
| GET | `/` | Mensagem inicial |
| POST | `/produtos` | Cadastrar produto |
| GET | `/produtos` | Listar produtos |
| GET | `/produtos/{produto_id}` | Consultar produto por ID |

## Exemplo de cadastro

Envie para `POST /produtos`:

```json
{
  "nome": "Teclado USB",
  "codigo": "TEC-001",
  "preco": "89.90"
}
```

O identificador é gerado pelo banco e incluído na resposta.

## Próximas etapas

- Testes automatizados.
- Migrações do banco de dados.
- Registro de entradas e saídas de estoque.
- Controle de saldo e prevenção de estoque negativo.
- Autenticação e permissões.
- PostgreSQL e publicação online.

## Autor

Igor Delmasquio

GitHub: https://github.com/JazzyJeff6