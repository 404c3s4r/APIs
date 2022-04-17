import requests
import json

def requisicao_HTTP_JSON(dress):
    try:

        requisicao = requests.get(dress)

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


def listagem_paises(listagem_paises):
	for cada in listagem_paises:
		print(cada['name'])

def populacao(pais="Brazil"):
	paises = requisicao_HTTP_JSON(f"https://restcountries.com/v3.1/name//{pais}")

	if paises:
		parsing_pais = parsing(paises)
	if parsing_pais:
		for pais in parsing_pais:
			print(f"{pais['name']}: {pais['population']}")
	else:
		print("pais não encontrado")

def moedas(pais="Brazil"):
	moedas = requisicao_HTTP_JSON(f"https://restcountries.com/v3.1/name//{pais}")
	if moedas:
		parsing_moedas = parsing(moedas)
		if parsing_moedas:
			for cada in parsing_moedas:
				print(f"{pais['name']}: {pais['currencies']}")
		else:
			print("Pais não encontrado")




url = input("Digite uma url: ")



if __name__ == "__main__":
	objeto_python = requisicao_HTTP_JSON(url)
	if objeto_python:
		done_parsing = parsing(objeto_python)

		if done_parsing:
			listagem_paises(done_parsing)
			print(contagem(done_parsing))
while True:
	pais_select = input("Escolha um pais: ")
	populacao(pais_select)
	moedas(pais_select)
