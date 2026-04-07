# Arquitectura del Sistema SIR

La arquitectura del Sistema Inteligente de Rutas (SIR) se concibe como una aplicación web moderna, siguiendo un patrón cliente-servidor. Se compone principalmente de tres capas lógicas que interactúan entre sí para ofrecer la funcionalidad deseada.

## Frontend (Cliente)

El Frontend es la parte de la aplicación con la que el usuario interactúa directamente a través de su navegador web. Es responsable de:

*   **Interfaz de Usuario (UI):** Presentar los elementos visuales (formularios, mapas, botones) y la lógica de interacción.
*   **Recopilación de Entradas:** Capturar el origen y el destino que el usuario introduce.
*   **Visualización:** Mostrar la ruta calculada y el tiempo estimado en el mapa.
*   **Comunicación con el Backend:** Enviar solicitudes al Backend para obtener datos y recibir respuestas para actualizar la UI.

Se construirá utilizando tecnologías web estándar como HTML, CSS y JavaScript. En fases posteriores, se podría integrar un framework como React o Vue.js para una gestión más eficiente del estado y la interfaz.

## Backend (Servidor)

El Backend actúa como el cerebro de la aplicación, gestionando la lógica de negocio y la comunicación con servicios externos. Sus responsabilidades incluyen:

*   **Recepción de Solicitudes:** Procesar las peticiones enviadas desde el Frontend (por ejemplo, una solicitud de cálculo de ruta).
*   **Lógica de Negocio:** Coordinar las operaciones necesarias para cumplir con la solicitud, como llamar a la API externa de mapas.
*   **Comunicación con API Externa:** Realizar llamadas a la API de mapas para obtener la información de rutas y tiempos.
*   **Preparación de Respuestas:** Formatear los datos recibidos de la API externa y enviarlos de vuelta al Frontend.

Se desarrollará utilizando Python, con la posible adopción de un framework como Django o Flask en el futuro para estructurar la aplicación de manera robusta y escalable.

## API Externa de Mapas

La API Externa de Mapas es un servicio de terceros que proporciona la funcionalidad central de ruteo y visualización geográfica. Esta API es fundamental para:

*   **Cálculo de Rutas:** Determinar la trayectoria óptima entre dos puntos geográficos.
*   **Estimación de Tiempo:** Proporcionar el tiempo de viaje estimado para la ruta calculada.
*   **Datos Geográficos:** Ofrecer la información necesaria para renderizar el mapa y los marcadores en el Frontend.

El Backend se comunicará con esta API para solicitar la información de rutas y luego la procesará antes de enviarla al Frontend. Ejemplos de estas APIs incluyen Google Maps Platform, OpenStreetMap (a través de servicios como OSRM) o Mapbox.
