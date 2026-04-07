<!-- README.md — SIR: Sistema Inteligente de Rutas -->

<div align="center">

<br>

<img src="assets/sir_logo.png" width="250" alt="SIR Logo">

# Sistema Inteligente de Rutas

<p style="font-size:16px; max-width:600px; margin: 0 auto;">
Planificación de rutas urbanas basada en modelos estadísticos de machine learning,<br>
datos de tráfico en tiempo real y alertas climáticas adaptativas.
</p>

<br>

[![Estado](https://img.shields.io/badge/Estado-En%20Desarrollo-orange?style=for-the-badge)](https://github.com/seculqr1-bit/ruta-inteligente)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-5-092E20?style=for-the-badge&logo=django&logoColor=white)](https://djangoproject.com)
[![Licencia MIT](https://img.shields.io/badge/Licencia-MIT-22c55e?style=for-the-badge)](LICENSE)
[![Open Source](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-ec4899?style=for-the-badge)](https://github.com/seculqr1-bit/ruta-inteligente)

<br>

[Descripción](#-descripción) · [Características](#-características-clave) · [Stack](#-stack-tecnológico) · [Modelo ML](#-modelo-estadístico-predictivo) ·  · [Autores](#-autores)

<br>

</div>

---

##  Descripción

SIR es una herramienta de **código abierto** que ayuda a las personas a tomar mejores decisiones de movilidad **antes de salir de casa**. En lugar de depender de mapas genéricos, SIR entrena un modelo estadístico predictivo con datos históricos de tráfico, condiciones climáticas y reportes  para recomendar la ruta que, con mayor probabilidad estadística, resultará más eficiente para el usuario en ese momento específico.

El sistema corre localmente en el navegador del usuario mediante un servidor **Django**, incluye registro de ubicaciones frecuentes (hogar, trabajo, etc.), visualización del mapa en tiempo real y un sistema de alertas graduadas basado en **rangos intercuartílicos (IQR)**.



---

##  Modelo estadístico predictivo

Aclarar que SIR no es un agente de IA generativa, sino un **modelo de probabilidad supervisado(por humanoos)**. Para cada par origen–destino, el sistema calcula la probabilidad de eficiencia de cada ruta disponible dado un conjunto de variables de contexto

### Sistema de alertas IQR

Las condiciones de tráfico se clasifican usando los cuartiles Q1, Q2 y Q3 calculados sobre datos históricos del mismo tramo horario:

| Nivel | Rango | Significado | Acción sugerida |
| :---: | :---- | :---------- | :-------------- |
|  **Normal** | < Q2 | Condiciones esperadas | Sin alerta activa |
|  **Moderado** | Q2 – Q3 | Tráfico por encima del promedio | Pre-alerta, salida anticipada |
|  **Crítico** | > Q3 | Congestión significativa | Alerta activa, ruta alternativa |

---

##  Stack tecnológico

| Componente | Tecnología | Justificación |
| :--------- | :--------- | :------------ |
| **Backend** | [Django 5](https://www.djangoproject.com/) + [DRF](https://www.django-rest-framework.org/) | ORM declarativo para base de datos relacional sin configuración manual. Ahorra tiempo y reduce deuda técnica. |
| **Modelo ML** | [scikit-learn](https://scikit-learn.org/) + [pandas](https://pandas.pydata.org/) + [NumPy](https://numpy.org/) | Pipeline estándar de Python para modelos estadísticos supervisados y manejo de datos. |
| **Mapas** | [Folium](https://python-visualization.github.io/folium/) / [Google Maps API](https://developers.google.com/maps) | Visualización de mapas interactivos embebida directamente en la interfaz web Django. |
| **Base de datos** | SQLite (dev) → [PostgreSQL](https://www.postgresql.org/) (prod) | Gestionado 100% por el ORM de Django. Sin escritura manual de SQL para las entidades base. |
| **Frontend** | Django Templates + [Tailwind CSS](https://tailwindcss.com/) | Sin framework JS adicional para mantener el proyecto accesible y simple de contribuir. |
| **Clima** | [OpenWeatherMap API](https://openweathermap.org/api) | API gratuita con tier para desarrollo. Pronóstico horario por coordenadas. |

---

## 📄 Licencia

Distribuido bajo la licencia **MIT**. Ver [`LICENSE`](LICENSE) para más información.

---

<div align="center">

<br>

Desarrollado con ❤️ para mejorar la movilidad urbana.

<br>

**César Torrecilla** &nbsp;·&nbsp; **Andrés González**


</div>                                                   
