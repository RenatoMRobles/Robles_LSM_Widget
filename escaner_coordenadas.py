import fitz  # PyMuPDF
import os

# ==========================================
# 🌸 MOTOR RATATOUILLE: LENTE DE CORRELACIÓN 🌸
# ==========================================

class LenteCorrelacion:
    def __init__(self, directorio_salida="img"):
        self.directorio_salida = directorio_salida
        
        if not os.path.exists(self.directorio_salida):
            os.makedirs(self.directorio_salida)
            print(f"✨ [Vera] Entorno '{self.directorio_salida}' preparado con éxito.")

    def escanear_con_precision(self, ruta_pdf):
        print(f"📖 [Elena] Activando el Lente de Correlación Espacial en: {ruta_pdf}...")
        
        try:
            doc = fitz.open(ruta_pdf)
            contador_exitos = 0
            
            for num_pag in range(len(doc)):
                pagina = doc.load_page(num_pag)
                
                # 1. Obtenemos las coordenadas EXACTAS de todas las imágenes reales en la página
                info_imagenes = pagina.get_image_info(xrefs=True)
                
                # 2. Obtenemos todo el texto con su geometría
                diccionario_texto = pagina.get_text("dict")
                bloques_texto = [b for b in diccionario_texto.get("blocks", []) if b["type"] == 0]

                # 3. Analizamos cada imagen encontrada
                for img_info in info_imagenes:
                    bbox_img = img_info["bbox"]
                    xref_img = img_info["xref"]
                    
                    # Coordenadas de la imagen: x0 (izq), y0 (arriba), x1 (der), y1 (abajo)
                    x0_img, y0_img, x1_img, y1_img = bbox_img
                    
                    nombre_palabra = "desconocido"
                    distancia_minima = 9999

                    # 4. Buscamos el texto que le pertenece a esta imagen específica
                    for bloque in bloques_texto:
                        x0_txt, y0_txt, x1_txt, y1_txt = bloque["bbox"]
                        
                        # LÓGICA LUMINOSA: El texto debe estar debajo de la imagen y alineado
                        if y0_txt >= (y1_img - 5): 
                            if x0_img - 30 <= x0_txt <= x1_img + 30: # Alineación horizontal
                                distancia_y = y0_txt - y1_img
                                
                                if distancia_y < distancia_minima:
                                    distancia_minima = distancia_y
                                    
                                    # Extraemos la primera línea en mayúsculas de este bloque
                                    for linea in bloque["lines"]:
                                        texto_linea = "".join([s["text"] for s in linea["spans"]]).strip()
                                        
                                        # Limpiamos números o paréntesis (ej. "VERDURA (1)")
                                        texto_linea_limpio = "".join([c for c in texto_linea if c.isalpha() or c.isspace()]).strip()
                                        
                                        if texto_linea_limpio.isupper() and len(texto_linea_limpio) > 2:
                                            # Tomamos la primera palabra en caso de que haya varias
                                            nombre_palabra = texto_linea_limpio.split()[0].lower()
                                            break

                    # 5. Preparamos el nombre final y guardamos
                    if nombre_palabra != "desconocido":
                        nombre_archivo = f"{nombre_palabra}.png"
                    else:
                        # Si por alguna razón no detecta el texto, no la perdemos
                        nombre_archivo = f"img_huerfana_{xref_img}.png"

                    ruta_guardado = os.path.join(self.directorio_salida, nombre_archivo)
                    
                    # Extraemos la imagen pura usando su ID de referencia (mejor calidad que un recorte)
                    try:
                        imagen_base = doc.extract_image(xref_img)
                        bytes_imagen = imagen_base["image"]
                        
                        with open(ruta_guardado, "wb") as f:
                            f.write(bytes_imagen)
                            
                        print(f"⚡ [Elena] ¡Precisión máxima! -> {nombre_archivo}")
                        contador_exitos += 1
                    except Exception as e:
                        print(f"⚠️ [Vera] Detalle menor al guardar la imagen {xref_img}: {e}")

            print(f"🚀 [Elena] ¡Orquestación completada! Extrajimos {contador_exitos} imágenes correlacionadas.")
            doc.close()
            
        except Exception as e:
            print(f"⚠️ [Vera] Fluctuación detectada: {e}")

# ==========================================
# 🚀 IGNICIÓN DEL PROTOCOLO
# ==========================================
if __name__ == "__main__":
    escaner = LenteCorrelacion()
    archivo_objetivo = "Dic_LSM1.pdf" 
    
    print("🌟 [Vera y Elena] Iniciando el Lente de Correlación Espacial...")
    escaner.escanear_con_precision(archivo_objetivo)