import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.title("Моё портфолио Python")

freq = st.slider("Частота", 1, 10, 3)

x = np.linspace(0, 10, 400)
y = np.sin(freq * x)

fig = go.Figure()
fig.add_scatter(x=x, y=y)

st.plotly_chart(fig, use_container_width=True)
