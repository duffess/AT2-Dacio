# PS5
import requests  # importa o requests
from bs4 import BeautifulSoup  # importa o BeautifulSoup
import pandas as pd  # importa o pandas

url = "https://pt.wikipedia.org/wiki/Lista_de_jogos_para_PlayStation_5"  # url da pagina da Wikipedia sobre jogos para PS5
response = requests.get(url)  # faz uma requisicao HTTP GET para a url e guarda na variavel response
conteudo = response.content.decode("utf-8")  # obtem o conteudo da resposta e decodifica usando utf-8
soup = BeautifulSoup(conteudo, 'html.parser')  # cria um objeto BeautifulSoup para fazer o parsing do html

# seleciona a primeira tabela com a classe 'sortable'
table = soup.find('table', {'class': 'sortable'})

if table:  # se a tabela foi encontrada
    data = []  # cria uma lista vazia para armazenar os dados
    rows = table.find_all('tr')  # encontra todas as linhas da tabela
    for row in rows:  # para cada linha na tabela
        cols = row.find_all(['th', 'td'])  # encontra todas as colunas na linha
        cols = [cell.get_text(strip=True) for cell in cols]  # obtem o texto de cada coluna, removendo espacos extras
        data.append(cols)  # adiciona os dados da linha na lista data

    df = pd.DataFrame(data)  # cria um DataFrame com os dados
    df.columns = df.iloc[0]  # define a primeira linha como cabecalho
    df = df[1:]  # remove a primeira linha do DataFrame
    df.columns = [f"col_{i}" for i in range(len(df.columns))]  # renomeia as colunas
    df = df.dropna(how='all')  # remove linhas que sao completamente nulas
    df.reset_index(drop=True, inplace=True)  # reseta os indices do DataFrame
    df = df.drop_duplicates()  # remove linhas duplicadas
    df.fillna('VALOR-VAZIO', inplace=True)  # preenche valores nulos com 'VALOR-VAZIO'
else:
    print('Tabela nao encontrada')  # se a tabela nao foi encontrada, imprime mensagem

dirCSV = "../AT2/Mini-Projeto1/PS5/dataframe.csv"  # define o caminho do arquivo csv
df.to_csv(dirCSV, encoding='utf-8', index=False)  # salva o DataFrame em um arquivo csv

dirJSON = "../AT2/Mini-Projeto1/PS5/dataframe.json"  # define o caminho do arquivo json
df.to_json(dirJSON, index=False)  # salva o DataFrame em um arquivo json

dirXLSX = "../AT2/Mini-Projeto1/PS5/dataframe.xlsx"  # define o caminho do arquivo xlsx
df.to_excel(dirXLSX, index=False)  # salva o DataFrame em um arquivo xlsx

print(df)  # imprime o DataFrame
