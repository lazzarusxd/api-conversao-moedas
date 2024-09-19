# API - Conversor de Moedas

## Descrição

Esta API permite a conversão de valores entre diferentes moedas, como USD para BRL.

## Funcionalidades

- Conversão de uma moeda de origem para várias moedas de destino.
- Suporte a múltiplas moedas.
- Respostas rápidas e precisas com base em taxas de câmbio atualizadas.

## Estrutura do Projeto

```plaintext
api-conversor-moedas/
├── api/
│   ├── v1/
│   │   ├── endpoints/
│   │   │   ├── responses/
│   │   │   │   └── conversor_responses.py
│   │   │   └── conversor.py
│   │   └── api.py
│   ├── v2/
│   │   ├── endpoints/
│   │   │   ├── responses/
│   │   │   │   └── conversor_responses.py
│   │   │   └── conversor.py
│   │   └── api.py
├── schemas/
│   └── conversor_schemas.py
├── services/
│   └── conversor_moedas.py
├── main.py
└── pyproject.toml
```


## Como Usar

1- Clone este repositório:
   ```bash
   git clone https://github.com/lazzarusxd/api-conversor-moedas.git
   ```

2- Navegue até o diretório do projeto:
   ```bash
   cd api-conversor-moedas
   ```

3- Instale as dependências usando Poetry:
   ```bash
   poetry install
   ```

4- Execute a API:
   ```bash
   uvicorn main:app --host localhost --port 8000 --reload
   ```

## Endpoints

### **Conversão via Query - api/v1**:

- ***moeda_origem***: Código da moeda de origem. Deve ter 3 letras maiúsculas.
- ***moedas_conversao***: Lista de códigos de moedas para conversão. Deve ser uma string com códigos separados por vírgula, com 3 letras maiúsculas cada.
- ***valor***: Valor a ser convertido. Deve ser um número maior que 0.

**Exemplo:**

```plaintext
GET /api/v1/conversor?moeda_origem=USD&moedas_conversao=JPY,EUR&valor=210
```

### **Conversão via Body - api/v2**:

- ***moeda_origem***: Código da moeda de origem. Deve ter 3 letras maiúsculas.
- ***moedas_conversao***: Lista de códigos de moedas para conversão. Cada código de moeda deve ter 3 letras maiúsculas.
- ***valor***: Valor a ser convertido. Deve ser um número maior que 0.

**Exemplo:**

```plaintext
POST /api/v2/conversor
```

### Exemplo de Body:

```plaintext
{
    "moeda_origem": "USD",
    "moedas_conversao": ["JPY", "EUR"],
    "valor": 210
}
```

## Contato:

João Lázaro - joaolazarofera@gmail.com

Link do projeto - https://github.com/lazzarusxd/api-conversor-moedas
