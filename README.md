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
5. [Metodología de Desarrollo](#metodología-de-desarrollo)
6. [Plan por Fases](#plan-por-fases)
7. [Arquitectura](#arquitectura)
8. [Flujo del Sistema](#flujo-del-sistema)
9. [Estructura de Carpetas](#estructura-de-carpetas)
10. [Versionado del Proyecto](#versionado-del-proyecto)
11. [Conclusión](#conclusión)

## 1. Descripción del Proyecto

El Sistema Inteligente de Rutas (SIR) es una aplicación web en desarrollo diseñada para simplificar la planificación de viajes. Permite a los usuarios ingresar un punto de origen y un destino, visualizando la ruta óptima en un mapa interactivo. Para el cálculo de rutas y la estimación del tiempo de viaje, SIR se integra con una API externa. En futuras etapas, se incorporarán alertas sencillas para mejorar la experiencia del usuario.

## 2. Objetivos

*   **Visualización Clara de Rutas:** Mostrar de forma precisa y comprensible las rutas entre dos puntos en un mapa.
*   **Estimación Fiable de Tiempo:** Proporcionar estimaciones de tiempo de viaje realistas para las rutas generadas.
*   **Interfaz Amigable:** Desarrollar una interfaz de usuario intuitiva y fácil de usar para todos los usuarios.
*   **Preparación para el Futuro:** Establecer una base sólida que permita la fácil integración de funcionalidades adicionales, como alertas y mejoras continuas.

## 3. Alcance

### Incluye

*   Desarrollo de una interfaz web para la entrada de puntos de origen y destino.
*   Integración con una API de mapas externa para la visualización de rutas y cálculo de tiempos.
*   Presentación del tiempo estimado de viaje.
*   Una estructura de proyecto modular y bien organizada, pensada para futuras expansiones.

### No Incluye (en esta fase inicial)

*   Funcionalidades avanzadas de machine learning.
*   Sistemas de autenticación de usuarios complejos.
*   Manejo de múltiples paradas o rutas con optimización avanzada.
*   Desarrollo de una API de ruteo propia.

## 4. Tecnologías

Para el desarrollo de SIR, se consideran las siguientes tecnologías clave:

*   **Frontend:** HTML, CSS, JavaScript. Se explorará el uso de frameworks modernos como [React](https://react.dev/) o [Vue.js](https://vuejs.org/) en fases posteriores para una interfaz más dinámica.
*   **Backend:** Python. Se evaluarán frameworks como [Django](https://www.djangoproject.com/) o [Flask](https://flask.palletsprojects.com/) para construir una API robusta y escalable.
*   **Base de Datos:** La elección se definirá en fases avanzadas, con opciones como [PostgreSQL](https://www.postgresql.org/) o [MySQL](https://www.mysql.com/).
*   **API de Mapas:** Se integrará una API externa de mapas, como [Google Maps Platform](https://developers.google.com/maps), [OpenStreetMap](https://www.openstreetmap.org/) (a través de servicios como OSRM) o [Mapbox](https://www.mapbox.com/), para la funcionalidad de ruteo y visualización.

## 5. Metodología de Desarrollo

El proyecto SIR se está desarrollando utilizando la metodología **Design Thinking**. Este enfoque centrado en el usuario nos permite comprender profundamente las necesidades de los estudiantes, idear soluciones innovadoras y prototipar rápidamente para validar conceptos. Las fases de Design Thinking que aplicaremos incluyen:

*   **Empatizar:** Entender las necesidades y desafíos de los usuarios.
*   **Definir:** Clarificar el problema central a resolver.
*   **Idear:** Generar una amplia gama de soluciones creativas.
*   **Prototipar:** Crear versiones preliminares de las soluciones.
*   **Testear:** Validar los prototipos con usuarios reales para obtener retroalimentación.

Actualmente, el proyecto se encuentra **en desarrollo**.

## 6. Plan por Fases

El desarrollo del proyecto SIR se estructura en las siguientes fases:

*   **Fase 1: Configuración Inicial (Setup):** Establecimiento del entorno de desarrollo, definición de la estructura del proyecto y creación de la documentación base.
*   **Fase 2: Producto Mínimo Viable (MVP):** Implementación de las funcionalidades esenciales: entrada de origen/destino, visualización de ruta en mapa y estimación de tiempo de viaje.
*   **Fase 3: Gestión de Datos:** Integración de una base de datos y desarrollo de funcionalidades de almacenamiento, si son necesarias para el proyecto.
*   **Fase 4: Mejoras y Alertas:** Adición de funcionalidades avanzadas como alertas simples, optimizaciones de rendimiento y mejoras en la experiencia de usuario.

Para una descripción más detallada de cada fase, consulte `docs/fases.md`.

## 7. Arquitectura

La arquitectura del sistema se basa en un enfoque cliente-servidor, donde el frontend interactúa con un backend que, a su vez, consume una API externa de mapas. A continuación, se presenta un diagrama de arquitectura simplificado:

```text
[Diagrama de Arquitectura del Sistema]
```

Para una explicación más profunda de la arquitectura, consulte `docs/arquitectura.md`.

## 8. Flujo del Sistema

El flujo principal para obtener una ruta en el sistema es el siguiente:

```text
[Diagrama de Flujo del Sistema]
```

Para una descripción detallada del flujo, consulte `diagrams/flujo.txt`.

## 9. Estructura de Carpetas

La organización de los archivos y directorios del proyecto es la siguiente:

```
ruta-inteligente/
│
├── README.md               # Documento principal del proyecto, con información general.
├── requirements.txt        # Lista de dependencias de Python para el proyecto.
├── .gitignore              # Archivo que especifica qué elementos ignorar en el control de versiones Git.
│
├── docs/                   # Documentación detallada del proyecto.
│   ├── fases.md            # Descripción de las fases de desarrollo del proyecto.
│   └── arquitectura.md     # Detalles sobre la arquitectura del sistema.
│
├── diagrams/               # Diagramas del proyecto en formato de texto ASCII.
│   ├── flujo.txt           # Diagrama que ilustra el flujo principal del sistema.
│   └── arquitectura.txt    # Diagrama que representa la estructura arquitectónica del sistema.
│
├── assets/                 # Recursos estáticos como imágenes y el logo del proyecto.
│   └── sir_logo.png        # Logo oficial del proyecto SIR.
│
└── src/                    # Directorio que contendrá el código fuente de la aplicación (vacío inicialmente).
```

## 10. Versionado del Proyecto

Se adoptará un esquema de versionado semántico (Major.Minor.Patch) para gestionar las versiones del proyecto. Las primeras versiones se enfocarán en la estabilidad y la implementación de las funcionalidades básicas, evolucionando a medida que se añadan nuevas características.

## 11. Conclusión

SIR es un proyecto educativo con el objetivo de proporcionar una base sólida para el desarrollo de aplicaciones web. A través de una planificación cuidadosa, un enfoque en la claridad y la aplicación de la metodología Design Thinking, esperamos que este proyecto sirva como una herramienta de aprendizaje valiosa y un punto de partida para futuras innovaciones y desarrollos.
