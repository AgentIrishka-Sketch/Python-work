import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.title("Интерактивная симуляция частиц ✨")

# параметры
num_particles = st.slider("Количество частиц", 10, 500, 100)
speed = st.slider("Скорость движения", 0.01, 0.2, 0.05)

# начальные позиции
x = np.random.rand(num_particles)
y = np.random.rand(num_particles)

# случайное движение
angle = np.random.rand(num_particles) * 2 * np.pi
x = x + np.cos(angle) * speed
y = y + np.sin(angle) * speed

# ограничение границ
x = np.clip(x, 0, 1)
y = np.clip(y, 0, 1)

# график
fig = go.Figure()

fig.add_scatter(
    x=x,
    y=y,
    mode="markers",
    marker=dict(
        size=8,
        color=np.sqrt(x*y),
        colorscale="plasma",
        showscale=True
    )
)

fig.update_layout(
    title="Движение частиц",
    xaxis=dict(range=[0,1]),
    yaxis=dict(range=[0,1]),
    height=600
)

st.plotly_chart(fig, use_container_width=True)
