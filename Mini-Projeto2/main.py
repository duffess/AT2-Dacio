import pandas as pd  # importa o pandas

def leituraPrincipal():
    try:
        # leitura principal dos dados
        df1 = pd.read_csv('Mini-Projeto2/dadosAT.csv')  # lê o arquivo CSV
        df2 = pd.read_json('Mini-Projeto2/dadosAT.json')  # lê o arquivo JSON
        df3 = pd.read_excel('Mini-Projeto2/dadosAT.xlsx')  # lê o arquivo Excel

        # Limpeza e tratamento de dados do DF1 (CSV)
        # Erros vistos: Emails faltando @, data de nascimento fora do padrão, linhas duplicadas, etc.
        df1.loc[3, 'data_nascimento'] = '2000-03-30'  # corrige a data de nascimento
        df1.loc[4, 'email'] = 'luiz.pereira@example.com'  # corrige o email
        df1.loc[8, 'email'] = 'maria.oliveira@example.com'  # corrige o email
        df1.loc[1, 'email'] = 'maria.oliveira@example.com'  # corrige o email
        df1 = df1.drop_duplicates(subset=df1.columns.difference(['id']), keep='first')  # remove linhas duplicadas, exceto pela coluna 'id'
        print('CSV + CSV + CSV + CSV + CSV + CSV + CSV + CSV + CSV')
        print(df1)

        # Limpeza e tratamento de dados do DF2 (JSON)
        # Erros vistos: Duplicatas id 1 e 6, data de nascimento errada id 3 e 9, email errado id 2
        df2.loc[2, 'data_nascimento'] = "1978-03-15"  # corrige a data de nascimento
        df2.loc[8, 'data_nascimento'] = "1999-11-05"  # corrige a data de nascimento
        df2.loc[1, 'email'] = "maria.oliveira@example.com"  # corrige o email
        df2 = df2.drop_duplicates(subset=df1.columns.difference(['id']), keep='first')  # remove linhas duplicadas, exceto pela coluna 'id'
        print('JSON + JSON + JSON + JSON + JSON + JSON + JSON + JSON + JSON')
        print(df2)

        # Limpeza e tratamento de dados do DF3 (XLSX)
        # Erros vistos: Data de nascimento errada na linha 4, email incompleto na linha 2
        df3.loc[1, 'email'] = "maria.oliveira@example.com"  # corrige o email
        df3.loc[3, 'data_nascimento'] = "2002-03-30"  # corrige a data de nascimento
        df3.loc[8, 'consoles'] = "PS4|Switch"  # corrige o campo 'consoles'
        df3 = df3.drop_duplicates(subset=df1.columns.difference(['id']), keep='first')  # remove linhas duplicadas, exceto pela coluna 'id'
        print('XLSX + XLSX + XLSX + XLSX + XLSX + XLSX + XLSX + XLSX + XLSX')
        print(df3)
        
        # concatenação dos três dataframes
        dataframe_concatenado = pd.concat([df1, df2, df3], ignore_index=True)  # concatena os dataframes

        # salvamento em um único arquivo Excel
        arq_para_excel = '../AT2/Mini-Projeto2/dados-excel.xlsx'  # define o caminho do arquivo Excel
        dataframe_concatenado.to_excel(arq_para_excel, index=False)  # salva o DataFrame concatenado em um arquivo Excel
        print('Sucesso. Arquivo para excel criado.')
    except:
        print('Ocorreu um erro ao consolidar o arquivo.')

leituraPrincipal()  # chama a função para executar o código
