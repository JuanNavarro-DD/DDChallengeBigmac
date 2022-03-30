'''
 # @ Author: Juan Navarro
 # @ Create Time: 2022-03-28 23:24:49
 # @ Modified by: Juan Navarro
 # @ Modified time: 2022-03-28 23:24:53
 # @ Description:
 '''
import pandas as pd
import plotly.express as px  
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dash import Dash, dcc, html, Input, Output  


app = Dash(__name__)


url = 'https://raw.githubusercontent.com/TheEconomist/big-mac-data/master/output-data/big-mac-full-index.csv'
data = pd.read_csv(url, index_col=1)


# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div(style={'backgroundColor': 'yellow'},children=[
    
    html.H1("Bigmac index", style={'text-align': 'center'}),

    dcc.Dropdown(id="country",
                 options=list(data['name'].unique()),
                 multi=False,
                 value='Australia',
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container', style={'textAlign' : 'center'},children=[]),
    html.Br(),
    
    html.Div(
        dcc.Graph(id='GDP_bigmac_index', figure={},style={'backgroundColor': 'red'}), style={'width': '50%', 'display': 'inline-block'}),
        html.Div(
            dcc.Graph(id='price_by_con', figure={},style={'backgroundColor': 'red'}),style={'width': '50%', 'display': 'inline-block'}
        )
        

])


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='GDP_bigmac_index', component_property='figure'),
     Output(component_id='price_by_con', component_property='figure')],
    [Input(component_id='country', component_property='value')]
)
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "{} bigmac index".format(option_slctd)

    data_filtered = data.dropna()
    data_fig = data_filtered[data_filtered['name'] == option_slctd]

    fig = make_subplots(specs=[[{'secondary_y':True}]])
    fig1 = px.line(data_fig, x='date', y=['USD_adjusted','USD_raw'])
    fig1['data'][1]['line']['color']='rgb(1,200,10)'
    # fig1.update_traces(marker_line_color=['rgb(1,200,10)','rgb(1,10,200)'])
    fig2 = px.bar(data_fig, x='date' , y='GDP_dollar')
    fig2.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5,opacity=0.6)
    fig1.update_traces(yaxis = "y2")
    fig.add_traces(fig1.data + fig2.data)
    fig.layout.xaxis.title = "date"
    fig.layout.yaxis.title = "GDP dollar"
    fig.layout.yaxis2.title = "bigmac index"
    fig.update_layout({'paper_bgcolor':'rgb(200,0,0)'})
    fig.update_layout(font_color='white')
    fig.layout.title = "{} bigmac index".format(option_slctd)
    

    fig_bycon = px.line(data,x='date',y='dollar_price', color='name')
    fig_bycon.layout.title = "Bigmac price by country"
    fig_bycon.layout.xaxis.title = "date"
    fig_bycon.layout.yaxis.title = "Bigmac price USD"
    fig_bycon.update_layout({'paper_bgcolor':'rgb(200,0,0)'})
    fig_bycon.update_layout(font_color='white')


    return container, fig, fig_bycon


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)