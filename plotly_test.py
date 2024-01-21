import plotly.express as px
fig = px.scatter(x=[1, 2, 3], y=[1, 3, 2])
fig.write_html('outputs/first_figure.html', auto_open=True)