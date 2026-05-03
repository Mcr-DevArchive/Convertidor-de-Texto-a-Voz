# 🎙️ Convertidor de Texto a Voz (TTS) - Voz Dual

**Convertidor de Texto a Voz** es una herramienta profesional de automatización diseñada para transformar documentos de texto extensos en audio MP3 de alta fidelidad. A diferencia de las soluciones de IA actuales que generan resúmenes o formatos de "podcast" (como NotebookLM), este script ofrece una **lectura estricta, fiel y estructurada**, ideal para el estudio de certificaciones técnicas y documentos profesionales.

---

## 👤 Información del Autor
*   **Desarrollador:** [Mcr-DevArchive](https://github.com/Mcr-DevArchive)
*   **Repositorio:** [Convertidor-de-Texto-a-Voz](https://github.com/Mcr-DevArchive/Convertidor-de-Texto-a-Voz)
*   **Versión:** 1.0

---

## ⚖️ Créditos y Honestidad Intelectual
Este proyecto utiliza como motor de síntesis de voz el contenedor desarrollado por **TravisVN**, que emula la API de OpenAI utilizando las voces neuronales de Microsoft Edge.
*   **Motor de Audio (Créditos Totales):** [openai-edge-tts de TravisVN](https://github.com/travisvn/openai-edge-tts)
*   **Contribución de Mcr-DevArchive:** Desarrollo del script de orquestación interactivo en Python, lógica de alternancia de voces (Dual-Voice) y validación de flujos de trabajo para archivos de gran volumen.

---

## 🌟 Características Principales
*   **Doble Locución Dinámica:** Alterna entre voz masculina (**Álvaro**) para encabezados/preguntas y femenina (**Ximena**) para el cuerpo del texto/respuestas.
*   **Interfaz Interactiva:** El script solicita al usuario la ruta del archivo y el nombre de salida, validando la existencia de los datos.
*   **Optimizado para Certificaciones:** Perfecto para procesar archivos tipo Test-King (AWS, Cisco, Azure, etc.) y escucharlos mientras se repasan.
*   **Zero Tokens (Low-Cost):** Funciona localmente vía Docker, evitando los costes por caracteres de servicios como ElevenLabs.
*   **Voces Humanas:** Calidad neuronal de Microsoft Edge, eliminando el tono robótico de los TTS antiguos.
---

## 🛠️ Guía de Instalación y Uso

### 1. Requisitos Previos
*   **Docker Desktop:** [Descargar e instalar](https://www.docker.com/products/docker-desktop/).
*   **Python 3.x:** Con la librería `requests` instalada:
    ```bash
    pip install requests
    ```

### 2. Levantar el Servidor de Audio (Motor)
Ejecuta el siguiente comando en tu terminal para arrancar el servidor local:
    ```bash
docker run -d -p 5050:5050 --name edge-tts-server -e API_KEY=sk-1234 travisvn/openai-edge-tts
    ```
### 3. Ejecutar el Convertidor

*   Lanza el script y sigue las instrucciones en pantalla:

    ```bash
    convertidor_tts.py
    ```

### 📝 Formato de Texto Soportado
Para que la Voz Dual funcione correctamente, el script identifica la palabra clave "Pregunta" al inicio de la línea para cambiar de locutor.
Ejemplo de archivo.txt:

```bash
Pregunta 1. ¿Qué protocolo se utiliza para la transferencia de archivos segura?
A. FTP
B. SFTP
C. HTTP
La respuesta correcta es la B.
```
### 🎨 Personalización de Voces
Puedes cambiar los locutores accediendo al catálogo completo en https://tts.travisvn.com/ y modificando las variables en el código convertidor_tts.py.

```bash
VOZ_PREGUNTA  
VOZ_RESPUESTA
```
## ⏱️ Control de Pausas
El motor de Microsoft Edge es altamente sensible a la puntuación. Puedes controlar el ritmo y los silencios del audio directamente desde tu archivo `.txt` usando los siguientes trucos:

1.  **Pausa corta (Breve):** Usa una coma ( `,` ). Ideal para separar opciones.
2.  **Pausa media (Estándar):** Usa un punto ( `.` ). Útil al final de una frase.
3.  **Pausa larga (Énfasis):** Usa tres puntos o más ( `...` ). Perfecto para dejar tiempo de reflexión tras una pregunta antes de escuchar la respuesta.

> **Tip:** Si necesitas un silencio aún mayor, puedes añadir una línea en blanco que contenga solo puntos suspensivos entre el bloque de la pregunta y la respuesta.
