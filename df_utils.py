# Define a function to center the headers
def styled_df(df):
    return df.style.set_properties(**{"text-align": "center"}).set_table_styles(
        [
            {"selector": "thead th", "props": [("text-align", "center")]},
            {
                "selector": "tbody tr:nth-child(even)",
                "props": [("background-color", "#f2f2f2")],
            },
            {"selector": "th, td", "props": [("border-right", "1px solid black")]},
            {
                "selector": "th:last-child, td:last-child",
                "props": [("border-right", "none")],
            },
        ]
    )
