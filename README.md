# Sistema Inteligente de Rutas (SIR)

![SIR Logo](assets/sir_logo.png)

## Autores

* Cear Torrecilla
* Andres Gonzales

## Tabla de Contenidos

1. [Descripción del Proyecto](#descripción-del-proyecto)
2. [Objetivos](#objetivos)
3. [Alcance](#alcance)
4. [Tecnologías](#tecnologías)
5. [Plan por Fases](#plan-por-fases)
6. [Arquitectura](#arquitectura)
7. [Flujo del Sistema](#flujo-del-sistema)
8. [Estructura de Carpetas](#estructura-de-carpetas)
9. [Versionado del Proyecto](#versionado-del-proyecto)
10. [Entregables](#entregables)
11. [Reglas del Proyecto](#reglas-del-proyecto)
12. [Conclusión](#conclusión)

## 1. Descripción del Proyecto

El Sistema Inteligente de Rutas (SIR) es una aplicación web diseñada para facilitar la planificación de viajes al permitir a los usuarios ingresar un punto de origen y un destino. La aplicación visualizará la ruta óptima en un mapa interactivo, utilizando una API externa para el cálculo de rutas y la estimación del tiempo de viaje. En futuras fases, se incorporarán alertas simples para mejorar la experiencia del usuario.

## 2. Objetivos

*   **Visualización de Rutas:** Mostrar de manera clara y precisa rutas entre dos puntos en un mapa.
*   **Estimación de Tiempo:** Proporcionar tiempos de viaje estimados para las rutas generadas.
*   **Interfaz Intuitiva:** Desarrollar una interfaz de usuario sencilla y fácil de usar.
*   **Escalabilidad Futura:** Sentar las bases para la inclusión de funcionalidades adicionales como alertas.

## 3. Alcance

### Incluye

*   Desarrollo de una interfaz web para la entrada de origen y destino.
*   Integración con una API de mapas para la visualización de rutas.
*   Cálculo y muestra del tiempo estimado de viaje.
*   Estructura de proyecto limpia y modular para futuras expansiones.

### No Incluye

*   Funcionalidades de machine learning complejas.
*   Sistemas de autenticación de usuarios avanzados en la fase inicial.
*   Manejo de múltiples paradas o rutas complejas en la fase MVP.
*   Desarrollo de una API de ruteo propia.

## 4. Tecnologías

Para el desarrollo de SIR, se prevé el uso de las siguientes tecnologías:

*   **Frontend:** HTML, CSS, JavaScript (con un framework moderno como React o Vue.js para futuras fases).
*   **Backend:** Python (con un framework como Django o Flask para futuras fases).
*   **Base de Datos:** (A definir en fases posteriores, posiblemente PostgreSQL o MySQL).
*   **API de Mapas:** Una API externa como Google Maps API, OpenStreetMap, o Mapbox.

## 5. Plan por Fases

El proyecto se desarrollará en las siguientes fases:

*   **Fase 1: Configuración Inicial (Setup):** Establecimiento del entorno de desarrollo, estructura del proyecto y documentación base.
*   **Fase 2: Producto Mínimo Viable (MVP):** Implementación de las funcionalidades principales (entrada de puntos, visualización de ruta, tiempo estimado).
*   **Fase 3: Gestión de Datos:** Integración de base de datos y funcionalidades de almacenamiento si son necesarias.
*   **Fase 4: Mejoras y Alertas:** Adición de funcionalidades avanzadas como alertas simples y optimizaciones.

Para más detalles, consulte `docs/fases.md`.

## 6. Arquitectura

La arquitectura del sistema se basará en un enfoque cliente-servidor, con un frontend que interactúa con un backend, el cual a su vez consume una API externa de mapas. A continuación, se presenta un diagrama de arquitectura simplificado:

```text
[Diagrama de Arquitectura del Sistema]
```

Para una descripción más detallada, consulte `docs/arquitectura.md`.

## 7. Flujo del Sistema

El flujo principal del sistema para la obtención de una ruta es el siguiente:

```text
[Diagrama de Flujo del Sistema]
```

Para una descripción más detallada, consulte `diagrams/flujo.txt`.

## 8. Estructura de Carpetas

La estructura del proyecto es la siguiente:

```
ruta-inteligente/
│
├── README.md               # Documento principal del proyecto
├── requirements.txt        # Dependencias del proyecto (Python)
├── .gitignore              # Archivos y carpetas a ignorar por Git
│
├── docs/                   # Documentación detallada del proyecto
│   ├── fases.md            # Descripción de las fases del proyecto
│   └── arquitectura.md     # Detalles de la arquitectura del sistema
│
├── diagrams/               # Diagramas del proyecto en formato de texto
│   ├── flujo.txt           # Diagrama de flujo del sistema
│   └── arquitectura.txt    # Diagrama de arquitectura del sistema
│
├── assets/                 # Recursos estáticos como imágenes y logos
│   └── sir_logo.png        # Logo del proyecto
│
└── src/                    # Código fuente de la aplicación (vacío inicialmente)
```

## 9. Versionado del Proyecto

Se utilizará un esquema de versionado semántico (Major.Minor.Patch). Las versiones iniciales se centrarán en la estabilidad y la implementación de las funcionalidades básicas.

## 10. Entregables

Los entregables de este proyecto incluyen:

*   Repositorio de GitHub con la estructura completa.
*   Documentación detallada (README, fases, arquitectura).
*   Diagramas de arquitectura y flujo.
*   Código fuente (en fases posteriores).

## 11. Reglas del Proyecto

*   Todo el código y la documentación deben estar en español.
*   Se priorizará la claridad y simplicidad para facilitar el aprendizaje.
*   Las contribuciones deben seguir las guías de estilo definidas.
*   No se incluirá código complejo o funcionalidades fuera del alcance definido para cada fase.

## 12. Conclusión

SIR es un proyecto educativo ambicioso que busca proporcionar una base sólida para el desarrollo de aplicaciones web. Con una planificación cuidadosa y un enfoque en la claridad, esperamos que este proyecto sirva como una excelente herramienta de aprendizaje y un punto de partida para futuras innovaciones.
