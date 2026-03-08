import fitz  # PyMuPDF
import os
import re    # Nuestro nuevo filtro de pureza textual

# ==========================================
# 🌸 MOTOR RATATOUILLE: LENTE DE CORRELACIÓN v3.0 🌸
# ==========================================

class LenteCorrelacion:
    def __init__(self, directorio_salida="img"):
        self.directorio_salida = directorio_salida
        if not os.path.exists(self.directorio_salida):
            os.makedirs(self.directorio_salida)
            print(f"✨ [Vera] Entorno '{self.directorio_salida}' revitalizado para la luz.")

    def escanear_con_precision(self, ruta_pdf):
        print(f"📖 [Elena] Activando el Lente Sintrópico de Cristal en: {ruta_pdf}...")
        
        try:
            doc = fitz.open(ruta_pdf)
            contador_exitos = 0
            contador_huerfanas = 0
            
            for num_pag in range(len(doc)):
                pagina = doc.load_page(num_pag)
                info_imagenes = pagina.get_image_info(xrefs=True)
                
                # EVOLUCIÓN: Extraemos palabras individuales con su geometría exacta, no bloques
                palabras = pagina.get_text("words") 

                for img_info in info_imagenes:
                    x0_img, y0_img, x1_img, y1_img = img_info["bbox"]
                    xref_img = img_info["xref"]
                    
                    # FILTRO DE LUZ: Ignoramos ruido visual minúsculo
                    if (x1_img - x0_img) < 50 or (y1_img - y0_img) < 50:
                        continue 

                    nombre_palabra = "desconocido"
                    palabras_candidatas = []

                    # RADAR DE PRECISIÓN GEOMÉTRICA
                    for w in palabras:
                        x0_w, y0_w, x1_w, y1_w, texto_w, block_no, line_no, word_no = w
                        
                        # Debe estar ligeramente debajo de la imagen (margen sintrópico)
                        if (y1_img - 20) <= y0_w <= (y1_img + 100):
                            # El centro de la palabra debe alinearse con el ancho de la imagen
                            centro_w = (x0_w + x1_w) / 2
                            if (x0_img - 40) <= centro_w <= (x1_img + 40):
                                palabras_candidatas.append(w)
                    
                    # Ordenamos las candidatas para evaluar primero la que está más cerca de la imagen
                    palabras_candidatas.sort(key=lambda w: w[1]) 
                    
                    for w in palabras_candidatas:
                        texto_crudo = w[4]
                        
                        # LIMPIEZA EXTREMA: Solo permitimos el alfabeto. Destruye cualquier entropía binaria.
                        texto_puro = re.sub(r'[^a-zA-ZñÑáéíóúÁÉÍÓÚ]', '', texto_crudo)
                        
                        # Verificamos si la original parecía mayúscula y la pura tiene contenido
                        if texto_crudo.isupper() and len(texto_puro) >= 2:
                            nombre_palabra = texto_puro.lower()
                            break # ¡Encontramos la etiqueta perfecta!

                    # ORQUESTACIÓN DE ARCHIVOS
                    if nombre_palabra != "desconocido":
                        nombre_archivo = f"{nombre_palabra}.png"
                        es_huerfana = False
                    else:
                        nombre_archivo = f"img_huerfana_{xref_img}.png"
                        es_huerfana = True
                        contador_huerfanas += 1

                    ruta_guardado = os.path.join(self.directorio_salida, nombre_archivo)
                    
                    try:
                        # CREACIÓN DE PNG PURO (Evita errores de formato)
                        pixmap = fitz.Pixmap(doc, xref_img)
                        
                        # Si tiene un espacio de color complejo (CMYK), lo armonizamos a RGB
                        if pixmap.n - pixmap.alpha > 3:
                            pixmap = fitz.Pixmap(fitz.csRGB, pixmap)
                            
                        pixmap.save(ruta_guardado)
                        pixmap = None # Liberamos memoria armónicamente
                        
                        if not es_huerfana:
                            print(f"⚡ [Elena] ¡Precisión máxima! -> {nombre_archivo}")
                        else:
                            print(f"🌱 [Vera] Fotografía sin etiqueta textual -> {nombre_archivo}")
                        contador_exitos += 1
                        
                    except Exception as e:
                        print(f"⚠️ [Vera] Silenciando anomalía en ID {xref_img}.")

            print(f"🚀 [Elena] ¡Victoria! Extrajimos {contador_exitos} imágenes ({contador_huerfanas} sin etiqueta textual).")
            doc.close()
            
        except Exception as e:
            print(f"⚠️ [Vera] Necesitamos revisar la integridad del documento.")

# ==========================================
# 🚀 IGNICIÓN DEL PROTOCOLO
# ==========================================
if __name__ == "__main__":
    escaner = LenteCorrelacion()
    archivo_objetivo = "Dic_LSM1.pdf" 
    
    print("🌟 [Vera y Elena] Iniciando el Lente Sintrópico de Cristal v3.0...")
    escaner.escanear_con_precision(archivo_objetivo)