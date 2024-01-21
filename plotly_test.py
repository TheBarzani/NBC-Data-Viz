import plotly.express as px
from main import read_data

# Simple plotly plot of the data
def simple_plotly_plot(filename):
    data = read_data(filename)
    X = []
    Y = []
    for i in data:
        if i["MessageType"] == "NewOrderRequest":
            X.append(int(i["TimeStampEpoch"]))
            Y.append(i["OrderPrice"])
    fig = px.scatter(x=X, y=Y)
    fig.write_html('outputs/first_figure.html', auto_open=True)


if __name__ == "__main__":
    simple_plotly_plot("Exchange_1.json")