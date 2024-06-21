import requests  # importa a biblioteca requests para fazer requisicoes HTTP
from bs4 import BeautifulSoup  # importa BeautifulSoup para fazer o parsing do HTML
import pandas as pd  # importa pandas para trabalhar com DataFrames

# url da pagina da Wikipedia sobre jogos para Xbox Series X e Series S
url = "https://pt.wikipedia.org/wiki/Lista_de_jogos_para_Xbox_Series_X_e_Series_S"

# faz uma requisicao HTTP GET para a url e guarda a resposta na variavel response
response = requests.get(url)

# obtem o conteudo da resposta e decodifica usando utf-8
conteudo = response.content.decode("utf-8")

# cria um objeto BeautifulSoup para fazer o parsing do HTML
soup = BeautifulSoup(conteudo, 'html.parser')

# seleciona a primeira tabela com a classe 'sortable'
table = soup.find('table', {'class': 'sortable'})

if table:  # se a tabela foi encontrada
    data = []  # cria uma lista vazia para armazenar os dados
    rows = table.find_all('tr')  # encontra todas as linhas da tabela
    for row in rows:  # para cada linha na tabela
        cols = row.find_all(['th', 'td'])  # encontra todas as colunas na linha
        cols = [cell.get_text(strip=True) for cell in cols]  # obtem o texto de cada coluna, removendo espacos extras
        data.append(cols)  # adiciona os dados da linha na lista data

    # cria um DataFrame com os dados obtidos da tabela
    df = pd.DataFrame(data)

    # define a primeira linha como cabecalho do DataFrame
    df.columns = df.iloc[0]

    # remove a primeira linha do DataFrame (cabecalho duplicado)
    df = df[1:]

    # renomeia as colunas para col_0, col_1, col_2, ...
    df.columns = [f"col_{i}" for i in range(len(df.columns))]

    # remove linhas que sao completamente nulas
    df = df.dropna(how='all')

    # reseta os indices do DataFrame apos remocao de linhas nulas
    df.reset_index(drop=True, inplace=True)

    # remove linhas duplicadas do DataFrame
    df = df.drop_duplicates()

    # preenche valores nulos com 'VALOR-VAZIO'
    df.fillna('VALOR-VAZIO', inplace=True)
else:
    print('Tabela nao encontrada')  # se a tabela nao foi encontrada, imprime mensagem

# diretorio e nome do arquivo CSV onde o DataFrame sera salvo
dirCSV = "../AT2/Mini-Projeto1/XBOXxs/dataframeXBOXSERIES.csv"

# salva o DataFrame em um arquivo CSV
df.to_csv(dirCSV, encoding='utf-8', index=False)

# diretorio e nome do arquivo JSON onde o DataFrame sera salvo
dirJSON = "../AT2/Mini-Projeto1/XBOXxs/dataframeXBOXSERIES.json"

# salva o DataFrame em um arquivo JSON
df.to_json(dirJSON, index=False)

# diretorio e nome do arquivo XLSX onde o DataFrame sera salvo
dirXLSX = "../AT2/Mini-Projeto1/XBOXxs/dataframeXBOXSERIES.xlsx"

# salva o DataFrame em um arquivo XLSX
df.to_excel(dirXLSX, index=False)

# imprime o DataFrame
print(df)
