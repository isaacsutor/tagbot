from dash import dash_table, html
import pandas as pd

class TableComponent:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def get_component(self):
        table = html.Div(
            dash_table.DataTable(
                columns=[{"name": i, "id": i} for i in self.df.columns],
                data=self.df.to_dict("records"),
                row_selectable="single",
                row_deletable=True,
                editable=True,
                filter_action="native",
                sort_action="native",
                style_table={"overflowX": "auto"},
            ),
        )
        return table