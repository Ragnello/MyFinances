import dash
from dash.dependencies import Input, Output
from dash import dash_table
from dash.dash_table.Format import Group
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

from app import app

# =========  Layout  =========== #
layout = dbc.Col([
    dbc.Row([
        html.Legend('Tabela de Despesas'),
        html.Div(id='tabela-despesas', className='dbbc')
    ]),

    dbc.Row([
        dbc.Col([
            dcc.Graph(id='bar-graph', style={'margin-right': '20px'})
        ], width=9),
        
        dbc.Col([
            dbc.Card(
                dbc.CardBody([
                    html.H4("Despesas"),
                    html.Legend("R$ 4400", id="valor_despesa_card", style={'font-size': '60px'}),
                    html.H6("Total de despesas"),
                ], style={'text-align': 'center', 'padding-top': '30px'})
            )
        ], width=3)
    ])

], style={'padding': '10px'})

# =========  Callbacks  =========== #

# Tabela
@app.callback(
    
    Output('tabela-despesas', 'children'),
    Input('store-despesas', 'data')
)
def tabela_despesas(data):
    df = pd.DataFrame(data)
    df['Data'] = pd.to_datetime(df['Data']).dt.date
    df = df.fillna('-')
    df.sort_values(by='Data', ascending=False)
    
    tabela = dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns])
    
    return tabela

# Gráfico
@app.callback(
    
    Output('bar-graph', 'figure'),
    Input('store-despesas', 'data')
)
def graph_despesas(data):
    df = pd.DataFrame(data)
    df_grouped = df.groupby("Categoria").sum()[['Valor']].reset_index()
    
    graph = px.bar(df_grouped, x='Categoria', y='Valor', title="Despesas Gerais")
    graph.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    
    return graph

# Card de despesas
@app.callback(
    Output('valor_despesa_card', 'children'),
    Input('store-despesas', 'data')
)
def card_despesas(data):
    df = pd.DataFrame(data)
    valor = df['Valor'].sum()
    return f"R$ {valor:.2f}"