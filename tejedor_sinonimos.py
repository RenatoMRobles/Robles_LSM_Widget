import json
import nltk
from nltk.corpus import wordnet as wn

# Aseguramos que el cerebro multilingüe esté activo
nltk.download('omw-1.4', quiet=True)
nltk.download('wordnet', quiet=True)

def generar_flexiones_y_diminutivos(palabra):
    """Genera las variaciones de género, número y diminutivos de pura luz."""
    formas_base = {palabra}
    
    # 🧸 FASE 1: INYECCIÓN DE TERNURA (Diminutivos desde la palabra raíz)
    if palabra.endswith(('o', 'a')):
        raiz = palabra[:-1]
        formas_base.update([
            raiz + 'ito', raiz + 'ita', 
            raiz + 'illo', raiz + 'illa', 
            raiz + 'irijillo', raiz + 'irijilla' # ¡El toque Flanders!
        ])
    elif palabra.endswith(('e', 'n', 'r', 'l', 'd')):
        formas_base.update([palabra + 'cito', palabra + 'cita'])
    elif palabra.endswith('z'):
        raiz = palabra[:-1] + 'c'
        formas_base.update([raiz + 'ito', raiz + 'ita'])

    # 🧬 FASE 2: EXPANSIÓN CUÁNTICA (Plurales y cambios de género para TODAS las formas)
    flexiones_totales = set(formas_base)
    for forma in formas_base:
        if forma.endswith('o'):
            flexiones_totales.update([forma[:-1] + 'a', forma + 's', forma[:-1] + 'as'])
        elif forma.endswith(('a', 'e', 'é', 'í', 'ó', 'ú')):
            flexiones_totales.add(forma + 's')
        elif forma.endswith('z'):
            flexiones_totales.add(forma[:-1] + 'ces')
        elif forma.endswith(('l', 'r', 'n', 'd', 'j')):
            flexiones_totales.add(forma + 'es')
            
    return flexiones_totales

def expandir_por_sinonimos(archivo_json="diccionario_lsm.json"):
    print("🌟 [Elena] Iniciando la Búsqueda de Alias Sintrópicos con Módulo de Ternura...")
    
    with open(archivo_json, 'r', encoding='utf-8') as f:
        diccionario = json.load(f)

    nuevo_diccionario = diccionario.copy()
    palabras_originales = list(diccionario.keys())
    contador_nuevas = 0

    for palabra in palabras_originales:
        ruta_img = diccionario[palabra]
        
        # Expandimos los sinónimos de WordNet
        synsets = wn.synsets(palabra, lang='spa')
        for synset in synsets:
            for lemma in synset.lemmas('spa'):
                sinonimo_base = lemma.name().lower()
                
                # Evitamos entropía de guiones bajos
                if "_" not in sinonimo_base:
                    
                    # ✨ LA MAGIA: Multiplicamos por género, número y diminutivos
                    variaciones = generar_flexiones_y_diminutivos(sinonimo_base)
                    
                    for variante in variaciones:
                        if variante not in nuevo_diccionario:
                            nuevo_diccionario[variante] = ruta_img
                            contador_nuevas += 1

    with open(archivo_json, 'w', encoding='utf-8') as f:
        json.dump(nuevo_diccionario, f, ensure_ascii=False, indent=4)

    print(f"✨ [Vera] Expansión empática completada. Se añadieron {contador_nuevas} nuevas conexiones de luz.")
    print("🥸 [Elena] ¡Tu JSON ya habla con diminutivos! ¡Listirijillo, jefe!")

if __name__ == "__main__":
    expandir_por_sinonimos()