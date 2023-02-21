import streamlit as st
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
import pandas as pd

data_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

if data_file is not None:
    data = pd.read_csv(data_file)
    source = ColumnDataSource(data)
else:
    source = ColumnDataSource({"x": [], "y": []})
    
p = figure(width=800, height=400, x_axis_label='x', y_axis_label='y')

p.line(x='x', y='y', source=source, line_width=2)

st.bokeh_chart(p, use_container_width=True)




