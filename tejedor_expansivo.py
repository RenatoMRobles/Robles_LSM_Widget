import os
import json
import mlconjug3
import sys
import unicodedata # Nuevo: Filtro de luz para acentos

# --- PARCHE DE ILUSIÓN PARA COMPATIBILIDAD ---
import sklearn.linear_model._sgd_fast as sgd_fast
if not hasattr(sgd_fast, 'Log'):
    class Log: pass
    sgd_fast.Log = Log
# ---------------------------------------------

# ==========================================
# 🌸 MOTOR RATATOUILLE: TEJEDOR OMNISCIENTE v3.0 🌸
# ==========================================

class TejedorExpansivo:
    def __init__(self, directorio_img="img", archivo_salida="diccionario_lsm.json"):
        self.directorio_img = directorio_img
        self.archivo_salida = archivo_salida
        self.conjugador = mlconjug3.Conjugator(language='es')

    def quitar_acentos(self, texto):
        """Purifica la palabra separando las tildes de su esencia alfabética."""
        # Normaliza el texto separando los caracteres de sus marcas diacríticas (acentos)
        texto_normalizado = unicodedata.normalize('NFD', texto)
        # Filtra solo los caracteres base, ignorando las marcas
        texto_sin_acentos = ''.join(c for c in texto_normalizado if unicodedata.category(c) != 'Mn')
        return texto_sin_acentos.lower()

    def es_verbo_infinitivo(self, palabra):
        terminaciones = ('ar', 'er', 'ir')
        excepciones = ['mar', 'mujer', 'ayer', 'primer', 'lugar', 'hogar', 'taller', 'amor']
        return palabra.endswith(terminaciones) and palabra not in excepciones and len(palabra) > 3

    def generar_plural(self, palabra):
        if palabra.endswith(('s', 'x')):
            return None
        vocales = ('a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú')
        if palabra.endswith('z'):
            return palabra[:-1] + 'ces'
        elif palabra.endswith(vocales):
            return palabra + 's'
        else:
            return palabra + 'es'

    def orquestar_expansion(self):
        print(f"🌟 [Elena] Iniciando la expansión estandarizada en: '{self.directorio_img}'...")
        
        diccionario_luminoso = {}
        
        try:
            for nombre_archivo in os.listdir(self.directorio_img):
                if not nombre_archivo.lower().endswith(".png") or nombre_archivo.startswith("img_huerfana"):
                    continue
                    
                palabra_base_cruda, _ = os.path.splitext(nombre_archivo)
                ruta_web = f"{self.directorio_img}/{nombre_archivo}"
                
                # 1. Cimentamos la palabra original (ya sin acentos)
                palabra_base = self.quitar_acentos(palabra_base_cruda)
                diccionario_luminoso[palabra_base] = ruta_web
                
                # 2. RUTA DE ACCIÓN: Verbos
                if self.es_verbo_infinitivo(palabra_base_cruda):
                    try:
                        verbo_conjugado = self.conjugador.conjugate(palabra_base_cruda)
                        if verbo_conjugado:
                            for forma in verbo_conjugado.iterate():
                                palabra_conj = forma[3] 
                                if palabra_conj and " " not in palabra_conj:
                                    # Aplicamos el filtro de luz a la conjugación
                                    palabra_conj_limpia = self.quitar_acentos(palabra_conj)
                                    if palabra_conj_limpia not in diccionario_luminoso:
                                        diccionario_luminoso[palabra_conj_limpia] = ruta_web
                    except Exception:
                        pass
                
                # 3. RUTA DE OBJETOS: Sustantivos y Adjetivos (Plurales)
                else:
                    plural = self.generar_plural(palabra_base_cruda)
                    if plural:
                        # Aplicamos el filtro de luz al plural
                        plural_limpio = self.quitar_acentos(plural)
                        if plural_limpio not in diccionario_luminoso:
                            diccionario_luminoso[plural_limpio] = ruta_web
                        
            with open(self.archivo_salida, 'w', encoding='utf-8') as archivo_json:
                json.dump(diccionario_luminoso, archivo_json, ensure_ascii=False, indent=4)
                
            print(f"✨ [Vera] Matriz lingüística purificada. Todas las llaves están libres de fricción ortográfica.")
            print(f"🚀 [Elena] ¡Orquestación completada con total éxito, jefe!")
            
        except Exception as e:
            print(f"⚠️ [Vera] Fluctuación detectada: {e}")

if __name__ == "__main__":
    tejedor = TejedorExpansivo()
    tejedor.orquestar_expansion()