import requests
import json

class Endereco():

    def __init__(self,cep):
        self.cep = cep

    def chamar_api_cep(self):
        response = requests.get('https://viacep.com.br/ws/{}/json/'.format(self.cep))
        if response.status_code != 200:
            print('deu ruim mermão: {}'.format(response))
        else:
            jeison = response.json()
            print('Logradouro: {}\nBairro: {}\nCidade: {}\nEstado: {}'.format(jeison['logradouro'],jeison['bairro'],jeison['localidade'],jeison['uf']))

ncep = input('Digite um cep sem hífen: ')
endereco = Endereco(ncep)
endereco.chamar_api_cep()