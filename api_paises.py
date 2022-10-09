import requests
import json


url = 'https://restcountries.com/v3.1/all'

def requisicao_HTTP_JSON(url):
    try:

        requisicao = requests.get(url)

        if requisicao.status_code == 200:
            return requisicao.text
        else:
            print(f'erro na requisição: {requisicao.status_code}')

    except Exception as error:
        print(error)


def parsing(objeto_python):
	try:
		return json.loads(objeto_python)

	except:
		print("Erro ao fazer parsing")

def contagem(all_paises):
	return len(all_paises)


def listagem_paises(listagem):
	for cada in listagem:
		print(cada['name']['common'])

def populacao(pais):
   
    paises = requisicao_HTTP_JSON(f'https://restcountries.com/v3.1/name//{pais}')
    p = parsing(paises)
    for cada in p:
        print(f"{cada['population']}")
        
if __name__=='__main__':
    texto = requisicao_HTTP_JSON(url)
    ParsingError = parsing(texto)
    if parsing:
        listagem_paises(parsing)
    
    while True:
        pais = input('país: ')
        populacao(pais)
