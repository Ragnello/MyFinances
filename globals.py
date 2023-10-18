import os
import pandas as pd

if("df_receitas.csv" in os.listdir()) and ("df_despesas.csv" in os.listdir()):
    df_receitas = pd.read_csv("df_receitas.csv", index_col=0, parse_dates=True)
    df_despesas = pd.read_csv("df_despesas.csv", index_col=0, parse_dates=True)
    
else:
    data_structure = {'Valor': [],
        'Efetuado': [],
        'Fixo': [],
        'Data': [],
        'Categoria': [],
        'Descrição': []}
    df_receitas = pd.DataFrame(data_structure)
    df_despesas = pd.DataFrame(data_structure)
    df_receitas.to_csv("df_receitas.csv")
    df_despesas.to_csv("df_despesas.csv")
    
if("df_cat_receita.csv" in os.listdir()) and ("df_cat_despesa.csv" in os.listdir()):
    df_cat_receita = pd.read_csv("df_cat_receita.csv", index_col=0)
    df_cat_despesa = pd.read_csv("df_cat_despesa.csv", index_col=0)
    cat_receita = df_cat_receita.values.tolist()
    cat_despesa = df_cat_despesa.values.tolist()
    
else:
    cat_receita = {'Categoria': ["Salário", "Investimento", "Aula", "Serviço Clínica"]}
    cat_despesa = {'Categoria': ["Alimentação", "Aluguel", "Combustível", "Saúde", "Lazer"]}
    
    df_cat_receita = pd.DataFrame(cat_receita)
    df_cat_despesa = pd.DataFrame(cat_despesa)
    df_cat_receita.to_csv("df_cat_receita.csv")
    df_cat_despesa.to_csv("df_cat_despesa.csv")