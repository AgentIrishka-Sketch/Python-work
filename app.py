import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.title("Интерактивная спиральная галактика 🌌")

# Параметры
num_particles = st.slider("Количество звезд", 100, 2000, 500)
arms = st.slider("Количество спиральных ветвей", 1, 5, 2)
rotation = st.slider("Сила вращения", 0.1, 2.0, 1.0)
spread = st.slider("Разброс звезд", 0.01, 0.5, 0.2)

# Генерация частиц
theta = np.random.rand(num_particles) * 2 * np.pi
r = np.random.rand(num_particles)**0.5  # плотность ближе к центру
branch_angle = (theta % (2*np.pi/arms))  # угол для ветви

# смещение ветви
r += branch_angle * spread
x = r * np.cos(theta) * rotation
y = r * np.sin(theta) * rotation

# цвет в зависимости от радиуса
color = np.sqrt(x**2 + y**2)

# график
fig = go.Figure()

fig.add_scatter(
    x=x, y=y,
    mode="markers",
    marker=dict(
        size=4,
        color=color,
        colorscale="turbo",
        showscale=False,
        opacity=0.8
    )
)

fig.update_layout(
    xaxis=dict(showgrid=False, visible=False),
    yaxis=dict(showgrid=False, visible=False),
    height=600,
    margin=dict(l=0,r=0,t=40,b=0)
)

st.plotly_chart(fig, use_container_width=True)
