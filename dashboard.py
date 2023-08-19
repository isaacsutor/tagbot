import sqlite3

import dash
import dash_bootstrap_components as dbc
import pandas as pd
from dash import dash_table, dcc, html
from dash.dependencies import Input, Output
from components import header, table, photo_gallery
# Initialize the Dash app
# app = dash.Dash(__name__)

# Connect to the SQLite3 database
conn = sqlite3.connect("testing_database.db")
query = "SELECT * FROM pictures"
df = pd.read_sql_query(query, conn)
conn.close()

dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"  # pylint: disable=line-too-long
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc_css])

tab1_content = dbc.Card(
    dbc.CardBody(
        [
            html.P("This is tab 1!", className="card-text"),
            dbc.Button("Click here", color="success"),
        ]
    ),
    className="mt-3",
)

tab2_content = dbc.Card(
    dbc.CardBody(
        [
            html.P("This is tab 2!", className="card-text"),
            dbc.Button("Don't click here", color="danger"),
        ]
    ),
    className="mt-3",
)


tabs = dbc.Tabs(
    [
        dbc.Tab(tab1_content, label="Tab 1"),
        dbc.Tab(tab2_content, label="Tab 2"),
        dbc.Tab(
            "This tab's content is never seen", label="Tab 3", disabled=True
        ),
    ]
)

with_theme = html.Div(
    [
        html.H5("DataTable with Bootstrap theme"),
        table.TableComponent(df).get_component(),
    ],
    className="dbc dbc-row-selectable",
)

without_theme = html.Div([
    html.H5("No theme", className="mt-4"),
    table.TableComponent(df).get_component()
])

photos = ["https://images.squarespace-cdn.com/content/v1/56f4c7679f72666afb4935fc/1567767924742-G7S94DDALIZT8MYRXGIW/CMON+Hate+Miniature+Painting+Chronicles+of+Hate+Adrian+Smith+%289%29.JPG",
          "https://creativetwilight.com/wp-content/uploads/2019/02/Miniature-Painting-Guide.jpg",
          "https://www.wargamer.com/wp-content/sites/wargamer/2021/05/best-paints-for-miniatures-citadel-technical-texture-paints-valhallan-blizzard-ogor-model.jpg"]

gallery = photo_gallery.PhotoGalleryComponent(photos).get_component()

app.layout = dbc.Container([
    header.HeaderComponent("Theme Explorer Sample App").get_component(),
    tabs,
    gallery,
    with_theme, without_theme
])

if __name__ == "__main__":
    app.run_server(debug=True)
