# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_mantine_components as dmc

# Incorporate data
df = px.data.gapminder()

# Initialize the app - incorporate a Dash Mantine theme
external_stylesheets = [dmc.theme.DEFAULT_COLORS]
app = Dash(__name__, external_stylesheets=external_stylesheets)

# App layout
app.layout = dmc.Container([
    dmc.Title("My First App with Data, Graph, and Controls", color="blue", size="h3"),
    dmc.RadioGroup(
            [dmc.Radio(i, value=i) for i in  ["pop", "lifeExp", "gdpPercap"]],
            id="metric-controls",
            value="lifeExp",
            size="sm"
        ),
    dmc.Grid([
        dmc.Col([
            dash_table.DataTable(data=df.to_dict("records"), page_size=10, style_table={"overflowX": "auto"})
        ], span=6),
        dmc.Col([
            dcc.Graph(figure={}, id="my-graph")
        ], span=6),
    ]),

], fluid=True)

# Add controls to build the interaction
@callback(
    Output(component_id="my-graph", component_property="figure"),
    Input(component_id="metric-controls", component_property="value")
)
def update_graph(col_chosen):
    fig = px.histogram(df, x="continent", y=col_chosen, histfunc="avg")
    return fig

# Run the App
if __name__ == "__main__":
    app.run_server(debug=True)


