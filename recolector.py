import os
import time
import requests
from bs4 import BeautifulSoup

# ==========================================
# 🌸 MOTOR RATATOUILLE: RECOLECTOR LSM 🌸
# ==========================================

class RecolectorLuminoso:
    def __init__(self, url_base, directorio_img="img"):
        self.url_base = url_base
        self.directorio_img = directorio_img
        
        # Nos aseguramos de que el nido de imágenes exista
        if not os.path.exists(self.directorio_img):
            os.makedirs(self.directorio_img)
            print(f"✨ [Vera] Carpeta '{self.directorio_img}' creada en perfecta armonía.")

    def descargar_imagen(self, url_imagen, nombre_palabra):
        """Descarga la imagen/GIF y la guarda con el nombre correcto."""
        try:
            # Determinamos si es gif o png según la URL
            extension = ".gif" if ".gif" in url_imagen.lower() else ".png"
            ruta_archivo = os.path.join(self.directorio_img, f"{nombre_palabra}{extension}")
            
            respuesta = requests.get(url_imagen, stream=True)
            if respuesta.status_code == 200:
                with open(ruta_archivo, 'wb') as archivo:
                    for bloque in respuesta.iter_content(1024):
                        archivo.write(bloque)
                print(f"⚡ [Elena] ¡Éxito! '{nombre_palabra}' guardada como {ruta_archivo}")
            else:
                print(f"⚠️ [Vera] El servidor no respondió favorablemente para '{nombre_palabra}'.")
                
        except Exception as e:
            print(f"⚠️ [Vera] Hubo un tropiezo en el flujo de datos: {e}")

    def buscar_palabra(self, palabra):
        """Busca la palabra en el diccionario web y extrae su imagen."""
        # NOTA PARA RENATO: Esta URL y los selectores HTML dependen del sitio específico
        url_busqueda = f"{self.url_base}/buscar?q={palabra}"
        
        try:
            print(f"🔍 [Elena] Explorando la red buscando: {palabra}...")
            respuesta = requests.get(url_busqueda)
            soup = BeautifulSoup(respuesta.text, 'html.parser')
            
            # 🎯 AQUÍ ES DONDE CALIBRAMOS EL RADAR
            # Ejemplo: Buscamos una etiqueta <img> dentro de un div con clase 'resultado-lsm'
            elemento_imagen = soup.find('img', class_='imagen-lsm-resultado') 
            
            if elemento_imagen and 'src' in elemento_imagen.attrs:
                url_img_encontrada = elemento_imagen['src']
                
                # A veces las rutas son relativas, las hacemos absolutas
                if not url_img_encontrada.startswith('http'):
                    url_img_encontrada = f"{self.url_base}{url_img_encontrada}"
                    
                self.descargar_imagen(url_img_encontrada, palabra)
            else:
                print(f"🌱 [Vera] No encontramos representación visual para '{palabra}' en esta página.")
                
            # Un pequeño respiro sintrópico para no saturar al servidor amigo (Buenas prácticas)
            time.sleep(1.5) 

        except Exception as e:
            print(f"⚠️ [Elena] ¡Fallo en la matrix! {e}")

# ==========================================
# 🚀 EJECUCIÓN DEL PROTOCOLO
# ==========================================
if __name__ == "__main__":
    # URL imaginaria de ejemplo
    sitio_objetivo = "https://diccionario-lsm-ejemplo.com" 
    recolector = RecolectorLuminoso(sitio_objetivo)
    
    # Lista de palabras de bienestar para iniciar nuestra prueba
    palabras_a_buscar = ["abuela", "gracias", "familia", "aprender"]
    
    print("🌟 [Vera e Elena] Iniciando recolección para el Motor Ratatouille...")
    for palabra in palabras_a_buscar:
        recolector.buscar_palabra(palabra)