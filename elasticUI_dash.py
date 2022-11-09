#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 20:06:20 2019

@author: ross
"""
import dash
#import dash_core_components as dcc
# import dash_html_components as html
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from elasticsearch import Elasticsearch
from pandas.io.json import json_normalize
import numpy as np

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
es = Elasticsearch('127.0.0.1', port=9200)


#input_group = dcc.Input(
#    id='input-1-submit',
#    placeholder='Enter a value...',
#    type='text',
#    value=''
#)

input_group = dbc.Input(
    id='input-1-submit',
    placeholder='Enter a value...',
    type='text',
    value=''
)

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                html.Br()
            ], justify="center"
        ),
        dbc.Row(
            [
                html.Br(),
                html.Div([ html.P(children=[html.B("Elastic")])], style={'font-family': 'Pacifico, cursive', 'font-size':'64'} ),
                html.Br()
            ], justify="center"
        ),
        dbc.Row(
            [
               #input_group
               dbc.Col(input_group, md=4)
            ], justify="center"
        ),
        html.Br(),
        dbc.Row(
            [
                #dbc.Col(input_group, md=4),
                html.Div(id='output-keypress')
            ],justify="center"
        ),
    ],
    fluid=True,
)
        

def text_style(text,search_term):
    if search_term in text:
        words = text.split(search_term)
    return html.Div([
             words[0],
             html.Mark(search_term, style={'color': 'red'}),
             words[1]
        ])

def generate_table(dataframe, search_term):
    rows = []
    for i in np.arange(dataframe.shape[0]):
        row = []
        for col in dataframe.columns:
            if  col== '_source.title':
                value = dataframe.iloc[i][col]
                text = text_style(value, search_term)
                row.append(html.Td(text))
            else:
                value = dataframe.iloc[i][col]
                row.append(html.Td(value))
        rows.append(html.Tr(row))
    
    table_header = [html.Tr([html.Th(col) for col in dataframe.columns])]
    table_body = [html.Tbody(rows)]
    table = dbc.Table(table_header + table_body, striped=True, bordered=True, hover=True)
    
    return dbc.Table(table)
        
@app.callback(
    Output("output-keypress", 'children'),
    [Input("input-1-submit", 'n_submit')],
    [State('input-1-submit', 'value')]
)
def update_output(ns1,input1):
    search_term = input1
    res = es.search(
        index="blog-sysadmins", 
        size=20, 
        body={
            "query": {
                "multi_match" : {
                    "query": search_term, 
                    "fields": [
                        "url", 
                        "title", 
                        "tags"
                    ] 
                }
            }
        }
    )

    df = json_normalize(res['hits']['hits'])
    
    #print (res)
    print (df)
    return generate_table(df,search_term)

    
if __name__ == "__main__":
    app.run_server(debug=True)
    #app.secret_key = 'mysecret'
    #app.run(host='127.0.0.1', port=8050)
