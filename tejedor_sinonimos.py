import json
import nltk
from nltk.corpus import wordnet as wn

# Descargamos el cerebro multilingüe de luz
nltk.download('omw-1.4', quiet=True)
nltk.download('wordnet', quiet=True)

def expandir_por_sinonimos(archivo_json="diccionario_lsm.json"):
    print("🌟 [Elena] Iniciando la Búsqueda de Alias Sintrópicos...")
    
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
                sinonimo = lemma.name().lower()
                # Filtramos entropía: sin guiones bajos y que no exista ya
                if "_" not in sinonimo and sinonimo not in nuevo_diccionario:
                    nuevo_diccionario[sinonimo] = ruta_img
                    contador_nuevas += 1

    with open(archivo_json, 'w', encoding='utf-8') as f:
        json.dump(nuevo_diccionario, f, ensure_ascii=False, indent=4)

    print(f"✨ [Vera] Expansión completa. Se añadieron {contador_nuevas} enlaces neuronales nuevos.")
    print("🚀 [Elena] ¡Tu JSON acaba de ir al gimnasio cerebral! ¡Arre!")

if __name__ == "__main__":
    expandir_por_sinonimos()