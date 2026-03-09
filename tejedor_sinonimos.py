import json
import nltk
from nltk.corpus import wordnet as wn

nltk.download('omw-1.4', quiet=True)
nltk.download('wordnet', quiet=True)

# 🌵 DICCIONARIO DE LUZ MEXICANO (Sinónimos manuales para no saturar)
MEXICANISMOS = {
    "amigo": ["cuate", "compa", "carnal", "valedor"],
    "bonito": ["chido", "padre", "padrisimo"],
    "bueno": ["chido", "perron"],
    "niño": ["chamaco", "morro", "escuincle", "huerco"],
    "trabajo": ["chamba"],
    "dinero": ["lana", "feria", "varo"],
    "fiesta": ["pachanga", "peda"],
    "enojado": ["encabronado", "enchilado"],
    "cerveza": ["chela", "cheve"],
    "auto": ["carro", "nave"],
    "si": ["simon", "camara"],
    "verdad": ["neta"],
    "mentira": ["choro"],
    "tonto": ["wey", "guey", "menso", "zonzo"]
}

def generar_flexiones_y_extremos(palabra):
    """Genera género, número, diminutivos, extremos y superlativos."""
    formas_base = {palabra}
    
    # 🧸 EXTREMOS Y SUPERLATIVOS
    if palabra.endswith(('o', 'a')):
        raiz = palabra[:-1]
        formas_base.update([
            raiz + 'ito', raiz + 'ita',         # chiquito
            raiz + 'itito', raiz + 'itita',     # chiquitito (Extremo)
            raiz + 'illo', raiz + 'illa', 
            raiz + 'irijillo', raiz + 'irijilla', 
            raiz + 'ote', raiz + 'ota',         # grandote (Superlativo)
            raiz + 'otote', raiz + 'otota'      # grandotote (Superlativo Extremo)
        ])
    elif palabra.endswith(('e', 'n', 'r', 'l', 'd')):
        formas_base.update([palabra + 'cito', palabra + 'cita', palabra + 'zote', palabra + 'zota'])
    elif palabra.endswith('z'):
        raiz = palabra[:-1] + 'c'
        formas_base.update([raiz + 'ito', raiz + 'ita', raiz + 'ote', raiz + 'ota'])

    # 🧬 PLURALES PARA TODAS LAS FORMAS
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
    print("🌟 [Elena] Iniciando Búsqueda Sintrópica: Modo Mexicano y Superlativo...")
    
    with open(archivo_json, 'r', encoding='utf-8') as f:
        diccionario = json.load(f)

    nuevo_diccionario = diccionario.copy()
    palabras_originales = list(diccionario.keys())
    contador_nuevas = 0

    for palabra in palabras_originales:
        ruta_img = diccionario[palabra]
        sinonimos_a_procesar = set([palabra])

        # Agregamos sinónimos de WordNet
        synsets = wn.synsets(palabra, lang='spa')
        for synset in synsets:
            for lemma in synset.lemmas('spa'):
                if "_" not in lemma.name():
                    sinonimos_a_procesar.add(lemma.name().lower())

        # 🌵 Agregamos Mexicanismos si la palabra base coincide
        if palabra in MEXICANISMOS:
            sinonimos_a_procesar.update(MEXICANISMOS[palabra])

        # ✨ Multiplicamos TODO por los superlativos y diminutivos
        for sin_base in sinonimos_a_procesar:
            variaciones = generar_flexiones_y_extremos(sin_base)
            for variante in variaciones:
                if variante not in nuevo_diccionario:
                    nuevo_diccionario[variante] = ruta_img
                    contador_nuevas += 1

    with open(archivo_json, 'w', encoding='utf-8') as f:
        json.dump(nuevo_diccionario, f, ensure_ascii=False, indent=4)

    print(f"✨ [Vera] Matriz Nacional integrada. {contador_nuevas} nuevas conexiones luminosas.")
    print("🌮 [Elena] ¡Ajuuuua! ¡Tu JSON ya sabe qué es la neta del planeta! ¡Arre!")

if __name__ == "__main__":
    expandir_por_sinonimos()