# 🤖 RPA Consulta de Beneficiários

Automação em Python para consultar dados de beneficiários de programas sociais (Auxílio Brasil, Bolsa Família e Auxílio Emergencial) via APIs do Portal da Transparência.

---

## 🚀 Pré-requisitos
- Python 3.7+** instalado  
- Chrome/Firefox** (para outras automações, se desejar)  
- Conta Gov.br (nível Prata ou Ouro)** para obter a chave de API  

---

## 🔑 Obter sua chave de API

1. Acesse o Portal da Transparência: https://portaldatransparencia.gov.br/api-de-dados/cadastrar-email  
2. Faça login com sua conta **Gov.br**.  
3. Cadastre seu e‑mail e aguarde a chave chegar por e‑mail (pode levar alguns minutos).  
4. Ao receber, copie o valor da **“Chave-API-Dados”**.

---

## 📋 Configuração do projeto

1. **Clone este repositório** (ou baixe os arquivos):
   ```bash
   git clone https://github.com/fellipeafonseca/api-consulta-beneficiario.git
   cd api-consulta-beneficiario

2. Crie o arquivo .env na raiz com este conteúdo:
   ```env
   API_KEY=sua_chave_api_aqui
   NIS=12345678900
   CPF=12345678900
   MES_ANO=202201

- API_KEY → chave recebida do Portal da Transparência
- NIS → seu NIS de teste
- CPF → seu CPF de teste
- MES_ANO → mês e ano no formato AAAAMM (ex: 202201)

3. Instale as dependências:
    ```bash
   pip install -r requirements.txt

## ▶️ Como rodar
1. Dentro da pasta do projeto, execute:
   ```bash
    python consulta_api.py

Isso fará três consultas:

1. Auxílio Brasil por NIS

2. Bolsa Família por CPF/NIS

3. Auxílio Emergencial por CPF/NIS

Você verá no console o JSON retornado (ou mensagens de erro em caso de falha).

![image](https://github.com/user-attachments/assets/b8bab1d1-c574-4127-b272-a11496e5174c)


## 🔧 Detalhes Técnicos
1. **Retry automático: até 3 tentativas em caso de falha de conexão ou resposta não-200.

2. **Logging: cronologia das tentativas e erros (nível INFO, WARNING e ERROR).

3. **Timeout de 10s em cada requisição para evitar travamento.


## 📚 Referências
- Documentação geral das APIs: https://api.portaldatransparencia.gov.br/swagger-ui.html

- Exemplos de uso: https://portaldatransparencia.gov.br/pagina-interna/603579-api-de-dados-exemplos-de-uso
