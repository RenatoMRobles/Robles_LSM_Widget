import os
import json
import mlconjug3 # Nuestro nuevo motor gramatical de bienestar

# ==========================================
# 🌸 MOTOR RATATOUILLE: TEJEDOR EXPANSIVO 🌸
# ==========================================

class TejedorExpansivo:
    def __init__(self, directorio_img="img", archivo_salida="diccionario_lsm.json"):
        self.directorio_img = directorio_img
        self.archivo_salida = archivo_salida
        # Instanciamos el orquestador de luz para el idioma español
        self.conjugador = mlconjug3.Conjugator(language='es')

    def es_verbo_infinitivo(self, palabra):
        """Identifica si la palabra fluye con la energía de una acción (verbo)."""
        terminaciones = ('ar', 'er', 'ir')
        # Filtramos palabras de alta frecuencia que no son verbos
        excepciones = ['mar', 'mujer', 'ayer', 'primer', 'lugar', 'hogar', 'taller', 'amor']
        return palabra.endswith(terminaciones) and palabra not in excepciones and len(palabra) > 3

    def orquestar_expansion(self):
        print(f"🌟 [Elena] Iniciando la expansión lingüística en la bóveda: '{self.directorio_img}'...")
        
        diccionario_luminoso = {}
        contador_imagenes = 0
        contador_conjugaciones = 0
        
        try:
            for nombre_archivo in os.listdir(self.directorio_img):
                if not nombre_archivo.lower().endswith(".png") or nombre_archivo.startswith("img_huerfana"):
                    continue
                    
                palabra_clave, _ = os.path.splitext(nombre_archivo)
                ruta_web = f"{self.directorio_img}/{nombre_archivo}"
                
                # 1. Cimentamos la palabra original (la imagen pura)
                diccionario_luminoso[palabra_clave] = ruta_web
                contador_imagenes += 1
                
                # 2. MAGIA SINTRÓPICA: Si es un verbo, orquestamos sus derivaciones
                if self.es_verbo_infinitivo(palabra_clave):
                    try:
                        verbo_conjugado = self.conjugador.conjugate(palabra_clave)
                        if verbo_conjugado:
                            # Iteramos por todas sus formas de tiempo y persona
                            for forma in verbo_conjugado.iterate():
                                # forma[3] contiene la palabra conjugada en sí
                                palabra_conjugada = forma[3] 
                                
                                # Filtramos valores nulos o tiempos compuestos (ej. "he saludado")
                                if palabra_conjugada and " " not in palabra_conjugada:
                                    palabra_conjugada = palabra_conjugada.lower()
                                    
                                    # Apuntamos la nueva palabra conjugada a la imagen del infinitivo
                                    if palabra_conjugada not in diccionario_luminoso:
                                        diccionario_luminoso[palabra_conjugada] = ruta_web
                                        contador_conjugaciones += 1
                    except Exception:
                        # Si el orquestador no reconoce la palabra como verbo, fluimos en paz
                        pass
                        
            # Cosechamos la matriz de conocimiento en el archivo JSON
            with open(self.archivo_salida, 'w', encoding='utf-8') as archivo_json:
                json.dump(diccionario_luminoso, archivo_json, ensure_ascii=False, indent=4)
                
            print(f"✨ [Vera] Matriz lingüística expandida con total perfección.")
            print(f"✅ [Elena] Imágenes base: {contador_imagenes}. ¡Formas verbales añadidas mágicamente: {contador_conjugaciones}!")
            print(f"🚀 [Vera y Elena] Tu JSON ahora comprende un total de {contador_imagenes + contador_conjugaciones} palabras.")
            
        except Exception as e:
            print(f"⚠️ [Vera] Fluctuación detectada durante la expansión armónica: {e}")

# ==========================================
# 🚀 IGNICIÓN DE LA EXPANSIÓN
# ==========================================
if __name__ == "__main__":
    tejedor = TejedorExpansivo()
    tejedor.orquestar_expansion()