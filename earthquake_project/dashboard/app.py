from sqlalchemy import create_engine
import pandas as pd
import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
from kafka_consumer import KafkaConsumerRealtime

engine = create_engine("postgresql://postgres:admin123@localhost:5432/postgres")
df = pd.read_sql("SELECT * from earthquake_data", engine)

years = sorted(df['year'].dropna().unique())
countries = sorted(df['country'].dropna().unique())

kafkaClient = KafkaConsumerRealtime(run_hours=2, max_records=5)
kafkaClient.start()

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Earthquake Dashboard"

app.layout = dbc.Container([
    html.H2("Earthquake Analytics Dashboard", className='text-center mt-4 mb-4'),
    dbc.Row([
        dbc.Col([
            html.Label("Data Mode"),
            dcc.RadioItems(
                id="data-mode",
                options=[{"label": x, "value": x} for x in ["Historic", "Realtime"]],
                value="Historic",
                inline=True,
                labelStyle={"margin-right": "10px"}
            )
        ], width=4),

        dbc.Col([
            html.Label("Plot Type"),
            dcc.RadioItems(
                id="plot-type",
                options=[{"label": x, "value": x} for x in ["Map", "Time Series", "Histogram"]],
                value="Map",
                inline=True,
                labelStyle={"margin-right": "10px"}
            )
        ], width=8)
    ]),

    html.Hr(),
    dbc.Row([
        dbc.Col([
            # html.Label("Region"),
            # dcc.Dropdown(
            #     id="country-filter",
            #     options=[{"label": x, "value": x} for x in countries],
            #     value='None',
            #     placeholder="Select Region"
            # ),

            html.Br(),
            html.Label("Year(Only For Historic)"),
            dcc.Dropdown(
                id="year-filter",
                options=[{"label": x, "value": x} for x in years],
                value='None',
                placeholder="Select Year"
            ),

            html.Br(),
            html.Label("Magnitude Range"),
            dcc.RangeSlider(
                id="range-filter",
                min=0, max=10, step=0.1,
                marks={i: str(i) for i in range(0, 11)},
                value=[0, 10]
            )
        ], width=4),

        dbc.Col([
            dcc.Graph(id="map-plot", style={"height": "600px"}),
            dcc.Interval(id='interval-refresh', interval=2 * 1000, n_intervals=0, disabled=True)
        ], width=8)
    ]),

    html.Hr(),
    dbc.Row([
        dbc.Col([
            html.H5("Aggregate Stats"),
            html.Div(id="stats-output", className="mt-2")
        ])
    ])
], fluid=True)


def fetch_realtime_data(limit=5):
    data_list = kafkaClient.get_data()
    if not data_list:
        return pd.DataFrame()
    df_realtime = pd.DataFrame(data_list)
    print(f'Realtime DataFrame:\n{df_realtime}')
    return df_realtime


@app.callback(
    Output('map-plot', 'figure'),
    Output('stats-output', 'children'),
    Output('interval-refresh', 'disabled'),
    Input('data-mode', 'value'),
    Input('plot-type', 'value'),
    # Input('country-filter', 'value'),
    Input('year-filter', 'value'),
    Input('range-filter', 'value'),
    Input('interval-refresh', 'n_intervals'),
)
def update_graph(mode, plot, year, mag_range, n_intervals):
    if mode == 'Historic':
        interval_disabled = True
        dff = df.copy()
        if year and year != 'None':
            dff = dff[dff['year'] == year]
        # if country and country != 'None':
        #     dff = dff[dff['country'] == country]
    else:
        interval_disabled = False
        dff = fetch_realtime_data()

    if mag_range and 'magnitude' in dff.columns:
        dff = dff[(dff['magnitude'] >= mag_range[0]) & (dff['magnitude'] <= mag_range[1])]

    if dff.empty:
        return px.scatter_geo(lat=[], lon=[]), "No data available", interval_disabled

    stats = (
        f"Total Earthquakes: {len(dff)} | "
        f"Min Magnitude: {dff['magnitude'].min():.2f} | "
        f"Max Magnitude: {dff['magnitude'].max():.2f} | "
        f"Standard Deviation: {dff['magnitude'].std():.2f}"
    )

    if plot == 'Map':
        if mode == 'Historic':
            fig = px.scatter_geo(
                dff,
                lat='latitude',
                lon='longitude',
                color='magnitude',
                color_continuous_scale="Blues",
                hover_name='place',
                hover_data=['id', 'time', 'place'],
                projection='natural earth'
            )
            fig.update_traces(marker=dict(size=10))
        else:
            fig = px.scatter_geo(
                dff,
                lat='latitude',
                lon='longitude',
                color='magnitude',
                color_continuous_scale="Blues",
                hover_data=['id', 'date'],
                projection='natural earth'
            )
            fig.update_traces(marker=dict(size=10))
    elif plot == 'Histogram':
        fig = px.histogram(dff, x='magnitude', nbins=30, title="Magnitude Distribution")
        fig.update_traces(marker_line_width=1.5, marker_line_color="black")
    elif plot == 'Time Series':
        if mode == 'Historic':
            dff['date'] = pd.to_datetime(dff['time']).dt.date
        else:
            dff['date'] = pd.to_datetime(dff['date']).dt.date if 'date' in dff.columns else pd.to_datetime('now')
        trend = dff.groupby("date")['magnitude'].count().reset_index()
        fig = px.line(trend, x='date', y='magnitude', title='Earthquakes Over Time')
    else:
        fig = px.scatter_geo()

    return fig, stats, interval_disabled


if __name__ == "__main__":
    app.run(debug=True)