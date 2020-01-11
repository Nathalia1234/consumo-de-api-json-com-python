#Código que consulta dados de uma página.

import requests   #Realiza o ato de fazer uma requisição web. 
import json         #Declarando biblioteca JSON para interpretador python buscar as funções.
import pandas   #Exporta os dados em excell 
import decimal  #A biblioteca serve para arredondar os valores, trocar pontos por virgula. 


#Foi pego o link da API no site Fixer.io 
url = "http://data.fixer.io/api/latest?access_key=4e4d3ae900de0cb7a7318573940eb9a7"
print("Acessando base de dados do Fixer.io...")

resposta  =  requests.get(url)
print(resposta)

#A função status_code sempre terá o código do acesso a página.
if resposta.status_code == 200:
    print("Acesso realizado com sucesso!")
    print("Buscando informações...")
    dados = resposta.json()  #Pegou os dados da página, atribuiu a variável dados.

    #foi criado variaveis e para cada variavel foi atribuido um cálculo especifico para conversão da moeda. 
    dolar_real = round(dados['rates']['BRL']/dados['rates']['USD'], 2)
    euro_real = round(dados['rates']['BRL']/dados['rates']['EUR'], 2)
    bitcoin_real = round(dados['rates']['BRL']/dados['rates']['BTC'], 2)

    #Cada variável criada acima foi concatenada aqui para mostrar o resultado de cada cálculo. 
    print('1 dollar vale',dolar_real, 'reais')
    print('1 euro vale',euro_real, 'reais')
    print('1 bitcoin vale', bitcoin_real, 'reais')

    print("Exportando resultado em tabela excell...")

    #A função DataFrame() são as informações da tela que nesse caso são as informações da tabela excell. 
    tela = pandas.DataFrame({'Moedas':['Dolar','Euro','Bitcoin'], 
                                                'Valores':[dolar_real,euro_real,bitcoin_real]})

    #to_csv  gera uma tabela do excell.
    tela.to_csv('valores.csv', index=False,  sep=";",  decimal=",")
    print("Arquivo exportado com sucesso!")
     
    
else: #Caso dê erro 
    print("Erro na base de dados.") #Será printado essa mensagem. 

    #A Biblioteca 'pip install json5' serve para estruturar o conteúdo em formato de JSON.
    #Para fazer uma requisição, irá precisar dessa biblioteca: --> pip install requests
    #A Biblioteca 'pip install pandas' serve para exportar dados em excell.