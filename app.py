import streamlit as st
import numpy as np
import plotly.express as px

st.title("Фрактал Мандельброта 🌌")

# интерактивные параметры
max_iter = st.slider("Количество итераций", 50, 500, 150)
zoom = st.slider("Zoom", 1, 10, 1)
x_center = st.slider("Смещение X", -2.0, 1.0, -0.5, step=0.01)
y_center = st.slider("Смещение Y", -1.5, 1.5, 0.0, step=0.01)

# размер изображения
width = 400
height = 400

# диапазон координат
x_width = 3.5 / zoom
y_height = 3.0 / zoom

x = np.linspace(x_center - x_width/2, x_center + x_width/2, width)
y = np.linspace(y_center - y_height/2, y_center + y_height/2, height)

X, Y = np.meshgrid(x, y)
C = X + 1j * Y
Z = np.zeros_like(C)
mandelbrot = np.zeros(C.shape)

# вычисление фрактала
for i in range(max_iter):
    mask = np.abs(Z) <= 2
    Z[mask] = Z[mask]**2 + C[mask]
    mandelbrot[mask] = i

# отображение
fig = px.imshow(
    mandelbrot,
    color_continuous_scale="turbo",
    origin="lower"
)

fig.update_layout(
    xaxis_showticklabels=False,
    yaxis_showticklabels=False
)

st.plotly_chart(fig, use_container_width=True)
