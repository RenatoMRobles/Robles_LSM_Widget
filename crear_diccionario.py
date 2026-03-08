import os
import json

# ==========================================
# 🌸 MOTOR RATATOUILLE: TEJEDOR JSON 🌸
# ==========================================

class TejedorSintropico:
    def __init__(self, directorio_img="img", archivo_salida="diccionario_lsm.json"):
        self.directorio_img = directorio_img
        self.archivo_salida = archivo_salida

    def orquestar_diccionario(self):
        print(f"🌟 [Elena] Iniciando el escaneo de la bóveda de imágenes: '{self.directorio_img}'...")
        
        diccionario_luminoso = {}
        contador_palabras = 0
        
        try:
            # Revisamos cada elemento físico en tu carpeta
            for nombre_archivo in os.listdir(self.directorio_img):
                
                # Solo invitamos a los archivos PNG puros y descartamos las huérfanas
                if nombre_archivo.endswith(".png") and not nombre_archivo.startswith("img_huerfana"):
                    
                    # Separamos "abuela" de ".png"
                    palabra_clave = os.path.splitext(nombre_archivo)[0]
                    
                    # Construimos la ruta relativa para el HTML (ej. "img/abuela.png")
                    ruta_relativa = f"{self.directorio_img}/{nombre_archivo}"
                    
                    # Alimentamos nuestro diccionario
                    diccionario_luminoso[palabra_clave] = ruta_relativa
                    contador_palabras += 1
                    
            # Escribimos la matriz de conocimiento en un archivo JSON
            with open(self.archivo_salida, 'w', encoding='utf-8') as archivo_json:
                json.dump(diccionario_luminoso, archivo_json, ensure_ascii=False, indent=4)
                
            print(f"✨ [Vera] Orquestación perfecta. Se ha tejido el mapa con {contador_palabras} señas vitales.")
            print(f"🚀 [Elena] ¡El archivo '{self.archivo_salida}' está listo para tu frontend!")
            
        except Exception as e:
            print(f"⚠️ [Vera] Fluctuación detectada durante el tejido: {e}")

# ==========================================
# 🚀 IGNICIÓN DEL PROTOCOLO
# ==========================================
if __name__ == "__main__":
    tejedor = TejedorSintropico()
    tejedor.orquestar_diccionario()