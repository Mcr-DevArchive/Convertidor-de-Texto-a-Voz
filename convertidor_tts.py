import requests
import os

# ==========================================================
# METADATOS DEL AUTOR
# Autor: Mcr-DevArchive
# GitHub: https://github.com/Mcr-DevArchive
# Versión: 1.0
# ==========================================================

# CONFIGURACIÓN DEL SERVIDOR (DOCKER)
API_URL = "http://localhost:5050/v1/audio/speech"
API_KEY = "sk-1234"

# VOCES PREDETERMINADAS (https://tts.travisvn.com/)
VOZ_PREGUNTA = "es-ES-AlvaroNeural"   # Voz masculina (España)
VOZ_RESPUESTA = "es-ES-XimenaNeural"  # Voz femenina (España)

def mostrar_cabecera():
    """Muestra los créditos del autor y del motor de audio."""
    print("\n" + "="*60)
    print("        CONVERTIDOR DE TEXTO A VOZ (VOZ DUAL)")
    print(f"        Autor: Mcr-DevArchive | Versión: 1.0")
    print(f"        GitHub: https://github.com/Mcr-DevArchive")
    print("="*60)
    print("Motor de audio (Créditos): https://github.com/travisvn/openai-edge-tts")
    print("-" * 60)

def obtener_rutas():
    """Solicita y valida las rutas de entrada y salida."""
    while True:
        entrada = input("📄 Ruta o nombre del archivo .txt (ej: preguntas.txt): ").strip()
        if not entrada:
            print("⚠️ Error: No has introducido ninguna ruta.")
            continue
        if not os.path.exists(entrada):
            print(f"❌ Error: El archivo '{entrada}' no existe.")
            continue
        break

    while True:
        salida = input("🔊 Nombre del archivo MP3 final (ej: examen_redes): ").strip()
        if not salida:
            print("⚠️ Error: El nombre de salida es obligatorio.")
            continue
        if not salida.lower().endswith(".mp3"):
            salida += ".mp3"
        break

    return entrada, salida

def generar_audio_dual():
    mostrar_cabecera()
    
    # Paso 1: Configuración de archivos
    archivo_texto, archivo_audio_final = obtener_rutas()

    # Paso 2: Lectura de datos
    try:
        with open(archivo_texto, "r", encoding="utf-8") as f:
            lineas = [l.strip() for l in f.readlines() if l.strip()]
    except Exception as e:
        print(f"🔥 Error al leer el archivo: {e}")
        return

    print(f"\n🚀 Procesando {len(lineas)} líneas...")
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    if os.path.exists(archivo_audio_final):
        os.remove(archivo_audio_final)

    # Paso 3: Conversión línea a línea
    with open(archivo_audio_final, "wb") as archivo_salida:
        for i, linea in enumerate(lineas):
            # Lógica de cambio de voz dinámica
            if linea.lower().startswith("pregunta"):
                voz_actual = VOZ_PREGUNTA
                etiqueta = "[ÁLVARO]"
            else:
                voz_actual = VOZ_RESPUESTA
                etiqueta = "[XIMENA]"

            print(f"[{i+1}/{len(lineas)}] {etiqueta}: {linea[:45]}...")
            
            payload = {
                "model": "tts-1",
                "input": linea + " . ", # Pausa natural al final
                "voice": voz_actual
            }

            try:
                response = requests.post(API_URL, json=payload, headers=headers)
                if response.status_code == 200:
                    archivo_salida.write(response.content)
                else:
                    print(f"⚠️ Error en línea {i+1} (Status {response.status_code})")
                    if response.status_code == 401:
                        print("❌ API Key no válida en el contenedor Docker.")
                        return
            except Exception as e:
                print(f"🔥 Fallo de conexión: {e}")
                break

    print(f"\n✅ PROCESO COMPLETADO")
    print(f"📂 Audio guardado en: {os.path.abspath(archivo_audio_final)}\n")

if __name__ == "__main__":
    generar_audio_dual()