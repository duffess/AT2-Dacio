import pandas as pd  # importa o pandas
from datetime import datetime  # importa o datetime para manipulacao de datas

def is_valid_email(email):
    # verifica se o email possui um formato valido
    return pd.notna(email) and "@" in email and "." in email.split("@")[-1]

def correct_email(email):
    if "@example.com" not in email:
        # Verifica se o e-mail possui um domínio; caso não tenha, adiciona "@example.com"
        return email + "@example.com"
    elif "." not in email.split("@")[-1]:
        # Caso haja um domínio mas não haja extensão (.com, .net, etc.), adiciona ".com"
        email += ".com"
    return email

def is_valid_date(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def correct_date(date_string):
    try:
        date = datetime.strptime(date_string, "%Y-%m-%d")
        return date.strftime("%Y-%m-%d")
    except ValueError:
        return '2000-01-01'  # Valor padrão para datas inválidas

def clean_data(df):
    # Corrige e-mails inválidos
    df['email'] = df['email'].apply(lambda x: correct_email(x))
    
    # Corrige datas inválidas
    df['data_nascimento'] = df['data_nascimento'].apply(lambda x: correct_date(x) if is_valid_date(x) else '2000-01-01')

    # Remove linhas duplicadas baseadas em todas as colunas exceto 'id'
    df = df.drop_duplicates(subset=df.columns.difference(['id']), keep='first')

    # Remove colunas completamente vazias
    df = df.dropna(axis=1, how='all')
    
    return df


def leituraPrincipal():
    try:
        # leitura principal dos dados
        df1 = pd.read_csv('Mini-Projeto2/dadosAT.csv')  # le o arquivo csv
        df2 = pd.read_json('Mini-Projeto2/dadosAT.json')  # le o arquivo json
        df3 = pd.read_excel('Mini-Projeto2/dadosAT.xlsx')  # le o arquivo excel

        # limpeza e tratamento de dados
        df1 = clean_data(df1)
        df2 = clean_data(df2)
        df3 = clean_data(df3)
        
        # exibe os dataframes apos limpeza
        print('csv + csv + csv + csv + csv + csv + csv + csv + csv')
        print(df1)
        
        print('json + json + json + json + json + json + json + json + json')
        print(df2)
        
        print('xlsx + xlsx + xlsx + xlsx + xlsx + xlsx + xlsx + xlsx + xlsx')
        print(df3)

        # concatenacao dos tres dataframes
        dataframe_concatenado = pd.concat([df1, df2, df3], ignore_index=True)  # concatena os dataframes

        # remocao de duplicatas apos a concatenacao
        dataframe_concatenado = dataframe_concatenado.drop_duplicates(subset=dataframe_concatenado.columns.difference(['id']), keep='first')
        
        # salvamento em um unico arquivo excel
        arq_para_excel = '../AT2/Mini-Projeto2/dados-excel.xlsx'  # define o caminho do arquivo excel
        dataframe_concatenado.to_excel(arq_para_excel, index=False)  # salva o dataframe concatenado em um arquivo excel
        print('sucesso. arquivo para excel criado.')
    
    except Exception as e:
        # captura qualquer erro que ocorrer e exibe uma mensagem detalhada
        print(f'ocorreu um erro ao consolidar o arquivo: {e}')

# chama a funcao para executar o codigo
leituraPrincipal()
