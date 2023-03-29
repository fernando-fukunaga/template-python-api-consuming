import requests
import json

class ListaDeRepositorios():
    
    def __init__(self,usuario):
        self.usuario = usuario

    def requisicao_api(self):
        response = requests.get('https://api.github.com/users/{}/repos'.format(self.usuario))
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code

    def imprime_repositorios(self):
        dados_api = self.requisicao_api()
        if type(dados_api) is not int:
            for i in range(len(dados_api)):
                print(dados_api[i]['name'])
        else:
            print(dados_api)

user = ListaDeRepositorios("fernando-fukunaga")
user.imprime_repositorios()