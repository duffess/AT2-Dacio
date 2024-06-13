import pandas as pd
import os


def leituraPrincipal():

    try:
        df1 = pd.read_csv('Mini-Projeto2/dadosAT.csv');
        df2 = pd.read_json('Mini-Projeto2/dadosAT.json');
        df3 = pd.read_excel('Mini-Projeto2/dadosAT.xlsx');

        # Limpeza e tratamento de dados do DF1 ( CSV )
        # Erros visto por mim: Emails faltando @; Data de nascimento fora do padrao; Linhas duplicadas; etc...
        df1.loc[3, 'data_nascimento'] = '2000-03-30'
        df1.loc[4, 'email'] = 'luiz.pereira@example.com'
        df1.loc[8, 'email'] = 'maria.oliveira@example.com'
        df1.loc[1, 'email'] = 'maria.oliveira@example.com'
        df1 = df1.drop_duplicates();
        print('CSV + CSV + CSV + CSV + CSV + CSV + CSV + CSV + CSV')
        print(df1)

        # Limpeza e tratamento de dados do DF2 ( JSON )
        # Erros visto por mim: Duplicatas id 1 e 6, data de nascimento errada id 3 e 9 id 3 com barra e id 9 formato diferente, email errado id 2 o .com.
        df2.loc[2, 'data_nascimento'] = "1978-03-15"
        df2.loc[8, 'data_nascimento'] = "1999-11-05"
        df2.loc[1, 'email'] = "maria.oliveira@example.com"
        print('JSON + JSON + JSON + JSON + JSON + JSON + JSON + JSON + JSON')
        print(df2)

        # Limpeza e tratamento de dados do DF2 ( JSON )
        # Erros visto por mim: Data de nascimento errada linha 4,   0923)*@#()*#)@+ email da linha 2 incompleto
        df3.loc[1, 'email'] = "maria.oliveira@example.com"
        df3.loc[3, 'data_nascimento'] = "2002-03-30"
        df3 = df3.drop_duplicates();
        print('XLSX + XLSX + XLSX + XLSX + XLSX + XLSX + XLSX + XLSX + XLSX')
        print(df3)
        
        dataframe_concatenado = pd.concat([df1, df2, df3], ignore_index=True);

        arq_para_excel = '../AT2/Mini-Projeto2/dados-excel.xlsx';
        dataframe_concatenado.to_excel(arq_para_excel, index=False);
        print('Sucesso. Arquivo para excel criado.');
    except:
        print('Ocorreu um erro ao consolidar o arquivo.');

leituraPrincipal()



