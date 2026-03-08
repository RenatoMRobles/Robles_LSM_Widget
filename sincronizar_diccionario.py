import os
import json

# ==========================================
# 🌸 MOTOR RATATOUILLE: TEJEDOR MAESTRO v2.0 🌸
# ==========================================

class TejedorMaestro:
    def __init__(self, directorio_img="img", archivo_salida="diccionario_lsm.json"):
        self.directorio_img = directorio_img
        self.archivo_salida = archivo_salida

    def orquestar_sincronizacion(self):
        print(f"🌟 [Elena] Iniciando auditoría final de la bóveda de imágenes: '{self.directorio_img}'...")
        
        diccionario_luminoso = {}
        contador_exitos = 0
        contador_errores = 0
        
        # Obtenemos la ruta absoluta para verificar existencia física real
        ruta_absoluta_img = os.path.abspath(self.directorio_img)

        try:
            # Revisamos cada elemento físico en tu carpeta
            for nombre_archivo in os.listdir(self.directorio_img):
                
                # FILTROS DE LUZ
                # 1. Solo PNGs
                if not nombre_archivo.lower().endswith(".png"):
                    continue
                
                # 2. Ignoramos residuos de scripts anteriores (defensivo)
                if nombre_archivo.startswith("img_huerfana"):
                    continue
                    
                ruta_completa_archivo = os.path.join(ruta_absoluta_img, nombre_archivo)
                
                # 🎯 VERIFICACIÓN DE EXISTENCIA FÍSICA (Adiós 404)
                if os.path.isfile(ruta_completa_archivo):
                    # Separamos el nombre del archivo de la extensión
                    palabra_clave, _ = os.path.splitext(nombre_archivo)
                    
                    # FILTRO DE CONTENIDO: La palabra debe contener letras (evitar solo números)
                    if not any(c.isalpha() for c in palabra_clave):
                        continue
                        
                    # Construimos la ruta relativa limpia para el HTML web (usando '/')
                    ruta_web = f"{self.directorio_img}/{nombre_archivo}"
                    
                    # Alimentamos nuestro diccionario
                    diccionario_luminoso[palabra_clave] = ruta_web
                    contador_exitos += 1
                else:
                    print(f"⚠️ [Vera] El archivo '{nombre_archivo}' aparece en la lista pero no existe físicamente.")
                    contador_errores += 1
                    
            # Escribimos la matriz de conocimiento en un archivo JSON final
            with open(self.archivo_salida, 'w', encoding='utf-8') as archivo_json:
                json.dump(diccionario_luminoso, archivo_json, ensure_ascii=False, indent=4)
                
            print(f"✨ [Vera] Auditoría y orquestación finalizadas con éxito.")
            print(f"✅ [Elena] ¡Sincronizamos {contador_exitos} señas reales y físicas! ¡Misión cumplida!")
            if contador_errores > 0:
                 print(f"⚠️ [Vera] Se omitieron {contador_errores} archivos fantasma para asegurar la integridad.")
            
        except Exception as e:
            print(f"⚠️ [Vera] Fluctuación crítica durante la sincronización: {e}")

# ==========================================
# 🚀 IGNICIÓN DEL TEJEDOR SUPREMO
# ==========================================
if __name__ == "__main__":
    tejedor = TejedorMaestro()
    tejedor.orquestar_sincronizacion()