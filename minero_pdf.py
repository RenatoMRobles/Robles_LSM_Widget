import fitz  # PyMuPDF
import os

# ==========================================
# 🌸 MOTOR RATATOUILLE: MINERO LUMINOSO PDF 🌸
# ==========================================

class MineroSintropico:
    def __init__(self, directorio_salida="img_pdf"):
        self.directorio_salida = directorio_salida
        
        # Preparamos el nido para las nuevas imágenes
        if not os.path.exists(self.directorio_salida):
            os.makedirs(self.directorio_salida)
            print(f"✨ [Vera] Carpeta '{self.directorio_salida}' forjada con éxito.")

    def extraer_imagenes_de_pdf(self, ruta_pdf):
        """Abre el PDF y extrae cada imagen incrustada en sus páginas."""
        print(f"📖 [Elena] Abriendo el cofre de conocimiento: {ruta_pdf}...")
        
        try:
            # Abrimos el documento con delicadeza
            documento = fitz.open(ruta_pdf)
            contador_imagenes = 0
            
            # Recorremos cada página del documento
            for numero_pagina in range(len(documento)):
                pagina = documento.load_page(numero_pagina)
                lista_imagenes = pagina.get_images(full=True)
                
                # Si hay imágenes en esta página, las extraemos
                for indice_imagen, img in enumerate(lista_imagenes):
                    xref = img[0] # El ID de referencia de la imagen
                    imagen_base = documento.extract_image(xref)
                    bytes_imagen = imagen_base["image"]
                    extension = imagen_base["ext"] # Suele ser png o jpeg
                    
                    # Generamos un nombre temporal (luego Renato les dará su nombre real)
                    nombre_archivo = f"img_pag{numero_pagina + 1}_{indice_imagen + 1}.{extension}"
                    ruta_completa = os.path.join(self.directorio_salida, nombre_archivo)
                    
                    # Guardamos la imagen en el mundo físico
                    with open(ruta_completa, "wb") as archivo_salida:
                        archivo_salida.write(bytes_imagen)
                        
                    contador_imagenes += 1
            
            print(f"🚀 [Elena] ¡Misión cumplida! Se extrajeron {contador_imagenes} imágenes luminosas.")
            documento.close()
            
        except Exception as e:
            print(f"⚠️ [Vera] Hubo una interrupción armónica en la lectura: {e}")

# ==========================================
# 🚀 EJECUCIÓN DEL PROTOCOLO DE EXTRACCIÓN
# ==========================================
if __name__ == "__main__":
    minero = MineroSintropico()
    
    # NOTA PARA RENATO: Coloca aquí el nombre exacto de uno de tus PDFs
    # Asegúrate de que el PDF esté en la misma carpeta que este script
    archivo_objetivo = "Dic_LSM.pdf" 
    
    print("🌟 [Vera y Elena] Iniciando el protocolo de minería local...")
    minero.extraer_imagenes_de_pdf(archivo_objetivo)