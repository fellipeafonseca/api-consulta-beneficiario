import os
import requests
import logging
from dotenv import load_dotenv
from time import sleep

# Carrega variáveis de ambiente
load_dotenv()
API_KEY = os.getenv("API_KEY")
NIS = os.getenv("NIS")
CPF = os.getenv("CPF")
MES_ANO = os.getenv("MES_ANO")

# Configura logging básico
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# Cabeçalhos comuns
HEADERS = {"chave-api-dados": API_KEY, "Accept": "application/json"}
RETRY_ATTEMPTS = 3
RETRY_DELAY = 2  # segundos


def _request_with_retry(url: str, params: dict) -> dict:
    for attempt in range(1, RETRY_ATTEMPTS + 1):
        try:
            logging.info(f"Tentativa {attempt} → {url} | params={params}")
            resp = requests.get(url, headers=HEADERS, params=params, timeout=10)
            if resp.ok:
                data = resp.json()
                logging.info(f'Status Code: {resp.status_code}')
                logging.info(f'{len(data)} resultado(s) encontrado(s):')
                return data
            logging.warning(f"Status Code: [{resp.status_code}] {resp.text}")
        except Exception as e:
            logging.error(f"Erro na requisição: {e}")
        if attempt < RETRY_ATTEMPTS:
            sleep(RETRY_DELAY)
    return {"erro": "falha nas tentativas de consulta"}


def auxilio_brasil_por_nis(nis: str, mes_ano: str) -> dict:
    url = "https://api.portaldatransparencia.gov.br/api-de-dados/auxilio-brasil-sacado-por-nis"
    return _request_with_retry(url, {"nis": nis, "anoMesCompetencia": mes_ano, "quantidade": 10})


def bolsa_familia_por_cpf_ou_nis(cpf_ou_nis: str,  mes_ano: str) -> dict:
    url = "https://api.portaldatransparencia.gov.br/api-de-dados/bolsa-familia-disponivel-por-cpf-ou-nis"
    return _request_with_retry(url, {"codigo": cpf_ou_nis,"anoMesCompetencia": mes_ano, "quantidade": 10})


def auxilio_emergencial_por_cpf_ou_nis(cpf_ou_nis: str) -> dict:
    url = "https://api.portaldatransparencia.gov.br/api-de-dados/auxilio-emergencial-por-cpf-ou-nis"
    return _request_with_retry(url, {"codigoBeneficiario": cpf_ou_nis,  "quantidade": 10})


if __name__ == "__main__":
    if not API_KEY or not NIS or not CPF or not MES_ANO:
        logging.error("Defina API_KEY, NIS, CPF e MES_ANO no .env antes de testar")
        exit(1)

    logging.info("→ Testando Auxílio Brasil")
    print(auxilio_brasil_por_nis(NIS, MES_ANO))

    logging.info("→ Testando Bolsa Família")
    print(bolsa_familia_por_cpf_ou_nis(CPF, MES_ANO))

    logging.info("→ Testando Auxílio Emergencial")
    print(auxilio_emergencial_por_cpf_ou_nis(CPF))
