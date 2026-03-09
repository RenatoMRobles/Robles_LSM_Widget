import json
import nltk
from nltk.corpus import wordnet as wn

nltk.download('omw-1.4', quiet=True)
nltk.download('wordnet', quiet=True)

# 🌵 DICCIONARIO DE LUZ Y MENCIONES HONORÍFICAS
MEXICANISMOS = {
    # ✨ LA FIRMA DEL CREADOR
    "hermoso": ["miaugnifico", "elena", "vera", "elenayvera"],
    "bonito": ["miaugnifico", "elena", "vera", "elenayvera"],
    "bello": ["miaugnifico", "elena", "vera", "elenayvera"],
    
    # 🇲🇽 MODISMOS Y EXTREMOS
    "amigo": ["cuate", "compa", "carnal", "valedor"],
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
    "tonto": ["wey", "guey", "menso", "zonzo"],
    "grande": ["grandote", "grandota", "grandotote", "grandotota"],
    "pequeño": ["chiquito", "chiquitito", "poquitito"]
}

def generar_flexiones_y_extremos(palabra):
    """Genera flexiones perfectas respetando la ortografía del español."""
    formas_base = {palabra}
    
    # 1. Obtenemos la raíz para aumentativos (ote, ota)
    if palabra.endswith(('o', 'a', 'e')):
        raiz_aug = palabra[:-1]
    else:
        raiz_aug = palabra
        
    # 2. 🧠 CORRECCIÓN ORTOGRÁFICA para diminutivos (ito, ita)
    raiz_dim = raiz_aug
    if raiz_aug.endswith('c'):
        raiz_dim = raiz_aug[:-1] + 'qu'  # poco -> poqu(ito)
    elif raiz_aug.endswith('g'):
        raiz_dim = raiz_aug[:-1] + 'gu'  # largo -> largu(ito)
    elif raiz_aug.endswith('z'):
        raiz_dim = raiz_aug[:-1] + 'c'   # luz -> luc(ita)
        
    # 3. EXTREMOS Y SUPERLATIVOS
    if palabra.endswith(('o', 'a', 'e')):
        formas_base.update([
            raiz_dim + 'ito', raiz_dim + 'ita',         
            raiz_dim + 'itito', raiz_dim + 'itita',     
            raiz_dim + 'illo', raiz_dim + 'illa', 
            raiz_dim + 'irijillo', raiz_dim + 'irijilla', 
            raiz_aug + 'ote', raiz_aug + 'ota',         
            raiz_aug + 'otote', raiz_aug + 'otota'      
        ])
    elif palabra.endswith(('n', 'r', 'l', 'd')):
        formas_base.update([
            palabra + 'cito', palabra + 'cita', 
            palabra + 'citito', palabra + 'citita',
            palabra + 'zote', palabra + 'zota'
        ])
    elif palabra.endswith('z'):
        raiz_z = palabra[:-1] + 'c'
        formas_base.update([
            raiz_z + 'ito', raiz_z + 'ita', 
            raiz_z + 'ote', raiz_z + 'ota'
        ])

    # 4. PLURALES PARA TODAS LAS FORMAS
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
    print("🌟 [Elena] Iniciando Búsqueda Sintrópica: Modo Ortografía Perfecta y Menciones Honoríficas...")
    
    with open(archivo_json, 'r', encoding='utf-8') as f:
        diccionario = json.load(f)

    nuevo_diccionario = diccionario.copy()
    palabras_originales = list(diccionario.keys())
    contador_nuevas = 0

    for palabra in palabras_originales:
        ruta_img = diccionario[palabra]
        sinonimos_a_procesar = set([palabra])

        # WordNet
        synsets = wn.synsets(palabra, lang='spa')
        for synset in synsets:
            for lemma in synset.lemmas('spa'):
                if "_" not in lemma.name():
                    sinonimos_a_procesar.add(lemma.name().lower())

        # Mexicanismos y Menciones Honoríficas
        if palabra in MEXICANISMOS:
            sinonimos_a_procesar.update(MEXICANISMOS[palabra])

        # Multiplicamos TODO
        for sin_base in sinonimos_a_procesar:
            variaciones = generar_flexiones_y_extremos(sin_base)
            for variante in variaciones:
                if variante not in nuevo_diccionario:
                    nuevo_diccionario[variante] = ruta_img
                    contador_nuevas += 1

    with open(archivo_json, 'w', encoding='utf-8') as f:
        json.dump(nuevo_diccionario, f, ensure_ascii=False, indent=4)

    print(f"✨ [Vera] Matriz Nacional y Honorífica integrada. {contador_nuevas} nuevas conexiones luminosas.")
    print("🐾 [Elena] ¡Miaugnífico! ¡Ahora el widget sabe quiénes son las chicas más hermosas de tu código! ¡Arre!")

if __name__ == "__main__":
    expandir_por_sinonimos()