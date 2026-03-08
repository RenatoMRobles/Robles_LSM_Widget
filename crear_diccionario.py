import os
import json

def generar_diccionario():
    # Ruta a tu carpeta de imágenes
    carpeta_img = 'img'
    
    # Diccionario que vamos a llenar mágicamente
    diccionario_lsm = {}
    
    print("🔍 Escaneando la bóveda de imágenes...")
    
    # Extensiones válidas para nuestro widget
    extensiones_validas = ('.png', '.jpg', '.jpeg', '.gif', '.webp')
    
    # Revisamos cada archivo en la carpeta
    for archivo in os.listdir(carpeta_img):
        if archivo.lower().endswith(extensiones_validas):
            # Obtenemos el nombre de la palabra sin la extensión
            palabra = os.path.splitext(archivo)[0].lower()
            
            # Guardamos la ruta exacta
            ruta_relativa = f"img/{archivo}"
            diccionario_lsm[palabra] = ruta_relativa
            
    # Exportamos el cerebro a un archivo JSON
    ruta_json = 'diccionario_lsm.json'
    with open(ruta_json, 'w', encoding='utf-8') as f:
        json.dump(diccionario_lsm, f, indent=4, ensure_ascii=False)
        
    print(f"✨ ¡Miau-gnífico! Diccionario creado con {len(diccionario_lsm)} señas.")
    print(f"📁 Archivo guardado en: {ruta_json}")

if __name__ == '__main__':
    generar_diccionario()