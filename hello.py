import streamlit as st
import altair as alt
from vega_datasets import data
# データサンプルを取得
def get_data(): 
    source = data.stocks() 
    source = source[source.date.gt("2004-01-01")] 
    return source
source = get_data()
st.write(source.head())
st.write(source.describe())


chart = alt.Chart(source).mark_line().encode( x="date:T", y="price", color="symbol"
)
st.altair_chart(chart, use_container_width=True)