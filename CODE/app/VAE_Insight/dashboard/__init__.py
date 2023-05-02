import numpy as np
import pandas as pd
import dash
from dash import dcc
from dash import html
from dash import dash_table
from .layout import html_layout
from .data import create_dataframe
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
from flask import render_template_string




def init_dashboard(server):
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix='/dashapp/'
    )

    df = create_dataframe()
    corr_df = df.corr()

    dash_app.index_string = html_layout

    dash_app.layout = html.Div([

        html.Div([   
            html.H3("Correlation between features"),
            dcc.Dropdown(
                options=df.columns[:21].tolist(),
                value=['AGE_YRS', 'SEX', 'ER_VISIT', 'HOSPITAL', 'HOSPDAYS','CUR_ILL_num', 'HISTORY_num'],
                multi=True,
                id="select-features-heatmap",
            ),
            dcc.Dropdown(
                options=df.columns[21:].tolist(),
                value=["Pain", "Urticaria", "Pyrexia", "Erythema", "Injection site swelling", "Injection site pain"],
                multi=True,
                id="select-adverse-affects-heatmap",
            ),
            dcc.Graph(id="heatmap")
        ]),

        html.Div([
            html.H3("Flow from features to adverse affects"),    
            dcc.Dropdown(
                options=df.columns[:21].tolist(),
                value=["SEX", "ER_VISIT"],
                multi=True,
                id="select-features",
            ),
            dcc.Dropdown(
                options=df.columns[21:].tolist(),
                value=["Pain", "Urticaria"],
                multi=True,
                id="select-adverse-affects",
            ),
            dcc.Graph(id="sankey-diagram")
        ])
    ])

    @dash_app.callback(
        Output("heatmap", "figure"),
        Input("select-features-heatmap", "value"),
        Input("select-adverse-affects-heatmap", "value")
    )
    def update_heatmap(features, adverse_affects):
        if features is None or adverse_affects is None:
            return {}
        else:
            sub_df = df[features+adverse_affects]
            corr_df = sub_df.corr()
            fig = px.imshow(corr_df)
            fig.update_layout(transition_duration=500)
            return fig

    @dash_app.callback(
        Output("sankey-diagram", "figure"),
        Input("select-features", "value"),
        Input("select-adverse-affects", "value")
    )
    def update_sankey_diagram(features, adverse_affects):
        if features is None or adverse_affects is None:
            return {}
        else:
            whole_features = []
            for feature in features:
                val = df[feature].unique().tolist()
                print(val)
                for v in val:
                    f_v = feature + "=" + str(v)
                    whole_features.append(f_v)
            whole_affects = []
            for affect in adverse_affects:
                val = df[affect].unique().tolist()
                print(val)
                for v in val:
                    a_v = affect + "=" + str(v)
                    whole_affects.append(a_v)
            print(whole_features)
            print(whole_affects)
            node = dict(label=whole_features + whole_affects)
            link = dict(source=[], target=[], value=[])
            for i,f in enumerate(whole_features):
                for j,a in enumerate(whole_affects):
                    sub_df = df[(df[f.split("=")[0]] == int(f.split("=")[1])) & (df[a.split("=")[0]] == int(a.split("=")[1]))]
                    print(sub_df.shape)
                    link["source"].append(i)
                    link["target"].append(len(whole_features) + j)
                    link["value"].append(sub_df.shape[0])
            fig = go.Figure(data=[go.Sankey(node=node, link=link)])
            fig.update_layout(transition_duration=500)
            return fig

    return dash_app.server
            