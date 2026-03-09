import json
import nltk
from nltk.corpus import wordnet as wn

# Descargamos el cerebro multilingüe (si ya lo tienes, pasará rapidísimo)
nltk.download('omw-1.4', quiet=True)
nltk.download('wordnet', quiet=True)

def generar_flexiones(palabra):
    """Genera las variaciones de género y número para una raíz sintrópica."""
    flexiones = {palabra} # Usamos un conjunto (set) para evitar duplicados
    
    # Regla 1: Si termina en 'o' (adjetivos/sustantivos típicamente masculinos)
    if palabra.endswith('o'):
        flexiones.add(palabra[:-1] + 'a')   # Femenino (bello -> bella)
        flexiones.add(palabra + 's')        # Masculino plural (bello -> bellos)
        flexiones.add(palabra[:-1] + 'as')  # Femenino plural (bello -> bellas)
        
    # Regla 2: Si termina en vocal que no sea 'o'
    elif palabra.endswith(('a', 'e', 'é', 'í', 'ó', 'ú')):
        flexiones.add(palabra + 's')        # (amable -> amables, bella -> bellas)
        
    # Regla 3: Si termina en 'z'
    elif palabra.endswith('z'):
        flexiones.add(palabra[:-1] + 'ces') # (feliz -> felices)
        
    # Regla 4: Si termina en consonante normal
    elif palabra.endswith(('l', 'r', 'n', 'd', 'j')):
        flexiones.add(palabra + 'es')       # (espectacular -> espectaculares)
            
    return flexiones

def expandir_por_sinonimos(archivo_json="diccionario_lsm.json"):
    print("🌟 [Elena] Iniciando la Búsqueda de Alias Sintrópicos con Expansión Morfológica...")
    
    with open(archivo_json, 'r', encoding='utf-8') as f:
        diccionario = json.load(f)

    nuevo_diccionario = diccionario.copy()
    palabras_originales = list(diccionario.keys())
    contador_nuevas = 0

    for palabra in palabras_originales:
        ruta_img = diccionario[palabra]
        
        # Buscamos la palabra en WordNet (Español)
        synsets = wn.synsets(palabra, lang='spa')
        for synset in synsets:
            for lemma in synset.lemmas('spa'):
                sinonimo_base = lemma.name().lower()
                
                # Filtramos entropía: sin guiones bajos
                if "_" not in sinonimo_base:
                    
                    # ✨ LA MAGIA: Generamos todas las versiones de la palabra
                    variaciones = generar_flexiones(sinonimo_base)
                    
                    for variante in variaciones:
                        if variante not in nuevo_diccionario:
                            nuevo_diccionario[variante] = ruta_img
                            contador_nuevas += 1

    with open(archivo_json, 'w', encoding='utf-8') as f:
        json.dump(nuevo_diccionario, f, ensure_ascii=False, indent=4)

    print(f"✨ [Vera] Matriz léxica enriquecida. Se añadieron {contador_nuevas} flexiones y sinónimos a la bóveda.")
    print("🥋 [Elena] ¡Dar cera, pulir código! ¡Tu JSON ya es cinturón negro! ¡Arre!")

if __name__ == "__main__":
    expandir_por_sinonimos()