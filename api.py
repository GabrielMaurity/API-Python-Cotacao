import requests 
import json

# Moedas que serão convertidas
moedas = 'USD-BRL,EUR-BRL'

# Link da consulta
url = f'https://economia.awesomeapi.com.br/json/last/{moedas}'

try:
    # Requisição GET
    response = requests.get(url)
    
    # Verifique se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Converta a resposta para JSON
        dados = response.json()
        
        # Exemplo de como acessar os dados de cada moeda
        usd_brl = dados.get('USDBRL', {})
        eur_brl = dados.get('EURBRL', {})
        
        print("Dados USD-BRL:", usd_brl)
        print("Dados EUR-BRL:", eur_brl)
    else:
        print(f"Erro ao fazer a requisição: {response.status_code}")
        print(response.text)
except requests.exceptions.RequestException as e:
    print(f"Ocorreu um erro ao fazer a requisição: {e}")