import sys
import sklearn.linear_model._sgd_fast as sgd_fast

# --- PARCHE DE ILUSIÓN PARA COMPATIBILIDAD ---
# Creamos el atributo 'Log' que el modelo antiguo busca desesperadamente
if not hasattr(sgd_fast, 'Log'):
    class Log: pass
    sgd_fast.Log = Log
# ---------------------------------------------
import os
import json
import mlconjug3 

# ==========================================
# 🌸 MOTOR RATATOUILLE: TEJEDOR OMNISCIENTE 🌸
# ==========================================

class TejedorExpansivo:
    def __init__(self, directorio_img="img", archivo_salida="diccionario_lsm.json"):
        self.directorio_img = directorio_img
        self.archivo_salida = archivo_salida
        self.conjugador = mlconjug3.Conjugator(language='es')

    def es_verbo_infinitivo(self, palabra):
        """Identifica si la palabra fluye con la energía de una acción (verbo)."""
        terminaciones = ('ar', 'er', 'ir')
        excepciones = ['mar', 'mujer', 'ayer', 'primer', 'lugar', 'hogar', 'taller', 'amor']
        return palabra.endswith(terminaciones) and palabra not in excepciones and len(palabra) > 3

    def generar_plural(self, palabra):
        """Clonación sintrópica: Genera el plural armónico de un sustantivo."""
        # Si ya termina en 's' o 'x' (ej. paraguas, lunes), la dejamos fluir
        if palabra.endswith(('s', 'x')):
            return None
            
        vocales = ('a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú')
        
        if palabra.endswith('z'):
            return palabra[:-1] + 'ces' # luz -> luces
        elif palabra.endswith(vocales):
            return palabra + 's'        # perro -> perros
        else:
            return palabra + 'es'       # color -> colores

    def orquestar_expansion(self):
        print(f"🌟 [Elena] Iniciando la expansión total (Verbos y Plurales) en: '{self.directorio_img}'...")
        
        diccionario_luminoso = {}
        contador_imagenes = 0
        contador_conjugaciones = 0
        contador_plurales = 0
        
        try:
            for nombre_archivo in os.listdir(self.directorio_img):
                if not nombre_archivo.lower().endswith(".png") or nombre_archivo.startswith("img_huerfana"):
                    continue
                    
                palabra_clave, _ = os.path.splitext(nombre_archivo)
                ruta_web = f"{self.directorio_img}/{nombre_archivo}"
                
                # 1. Cimentamos la palabra original
                diccionario_luminoso[palabra_clave] = ruta_web
                contador_imagenes += 1
                
                # 2. RUTA DE ACCIÓN: Verbos
                if self.es_verbo_infinitivo(palabra_clave):
                    try:
                        verbo_conjugado = self.conjugador.conjugate(palabra_clave)
                        if verbo_conjugado:
                            for forma in verbo_conjugado.iterate():
                                palabra_conjugada = forma[3] 
                                if palabra_conjugada and " " not in palabra_conjugada:
                                    palabra_conjugada = palabra_conjugada.lower()
                                    if palabra_conjugada not in diccionario_luminoso:
                                        diccionario_luminoso[palabra_conjugada] = ruta_web
                                        contador_conjugaciones += 1
                    except Exception:
                        pass
                
                # 3. RUTA DE OBJETOS: Sustantivos y Adjetivos (Plurales)
                else:
                    plural = self.generar_plural(palabra_clave)
                    if plural and plural not in diccionario_luminoso:
                        diccionario_luminoso[plural] = ruta_web
                        contador_plurales += 1
                        
            # Cosechamos la matriz
            with open(self.archivo_salida, 'w', encoding='utf-8') as archivo_json:
                json.dump(diccionario_luminoso, archivo_json, ensure_ascii=False, indent=4)
                
            print(f"✨ [Vera] Matriz lingüística expandida a su máxima capacidad.")
            print(f"✅ [Elena] Base: {contador_imagenes} | Verbos: +{contador_conjugaciones} | Plurales: +{contador_plurales}")
            total_palabras = contador_imagenes + contador_conjugaciones + contador_plurales
            print(f"🚀 [Vera y Elena] ¡Tu diccionario ahora comprende {total_palabras} palabras listas para el widget!")
            
        except Exception as e:
            print(f"⚠️ [Vera] Fluctuación detectada: {e}")

# ==========================================
# 🚀 IGNICIÓN DEL TEJEDOR OMNISCIENTE
# ==========================================
if __name__ == "__main__":
    tejedor = TejedorExpansivo()
    tejedor.orquestar_expansion()