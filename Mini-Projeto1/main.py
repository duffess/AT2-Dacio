#Codigo terminado e finalizado  as 18:55 do dia 12/06/2024 - FUNCIONANDO TUDO OK 0 ERROS
import requests # importacao do request 
from bs4 import BeautifulSoup # importacao do bs
import pandas as pd # importacao do pandas

urls = [
    "https://pt.wikipedia.org/wiki/Lista_de_jogos_para_PlayStation_5",
    "https://pt.wikipedia.org/wiki/Lista_de_jogos_para_PlayStation_4",
    "https://pt.wikipedia.org/wiki/Lista_de_jogos_para_Xbox_Series_X_e_Series_S",
    "https://pt.wikipedia.org/wiki/Lista_de_jogos_para_Xbox_360",
    "https://pt.wikipedia.org/wiki/Lista_de_jogos_para_Nintendo_Switch",

] # declaracao da url como link do wikipedia jogos para ps5

data = []; # lista das tabelas 

for url in urls: # itera sobre a lista de urls
    response = requests.get(url); # faz uma requisicao http ( get ) para a url da variavel url e guarda na variavel responde
    conteudo = response.content.decode("utf-8"); # puxa o conteudo do response, decodifica e e usa a codificacao utf-8 
    soup = BeautifulSoup(conteudo, 'html.parser');
    tables = soup.select('table', {'class': 'sortable'}) # procura a tabela com a class desejada

    if tables:
        for table in tables:  # itera sobre todas as tabelas encontradas
            rows = table.find_all('tr')  # encontra todas as linhas (tr) na tabela

            for row in rows:  # itera sobre a lista de linhas (rows)
                cols = row.find_all(['th', 'td'])  # encontra todas as células (th e td) em cada linha
                cols = [celula.get_text(strip=True) for celula in cols]  # limpa os textos das células
                data.append(cols)  # adiciona os textos limpos à lista data
    else:
        print('Erro: Tabela Nao encontrada')

df = pd.DataFrame(data); # transforma a lista de datas em um dataframe
df.columns = df.iloc[0]
df = df[1:]
df = df.dropna(how='all')
df.reset_index(drop=True, inplace=True) #reseta todos os indices do dataframe
df = df.drop_duplicates() # remove as linhas dupluicadas
dir = "../AT2/Mini-Projeto1/dataframe.csv"; # defini o caminho do arquivo que sera criado em uma variavel
df.to_csv(dir, encoding='utf-8') # cria o csv de acordo com a variavel acima

print(df);
