import pandas as pd
import plotly.figure_factory as pff

data = pd.read_csv("Mobilebrand.csv")
avgrt = data["Avgrating"].tolist()
graph = pff.create_distplot([avgrt],["a"], show_hist = False)

graph.show()