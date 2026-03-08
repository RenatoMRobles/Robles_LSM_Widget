import fitz  # PyMuPDF
import os

# ==========================================
# 🌸 MOTOR RATATOUILLE: LENTE DE CORRELACIÓN v2.1 🌸
# ==========================================

class LenteCorrelacion:
    def __init__(self, directorio_salida="img"):
        self.directorio_salida = directorio_salida
        
        if not os.path.exists(self.directorio_salida):
            os.makedirs(self.directorio_salida)
            print(f"✨ [Vera] Entorno '{self.directorio_salida}' preparado para la luz.")

    def escanear_con_precision(self, ruta_pdf):
        print(f"📖 [Elena] Activando el Lente Sintrópico Refinado en: {ruta_pdf}...")
        
        try:
            doc = fitz.open(ruta_pdf)
            contador_exitos = 0
            contador_huerfanas = 0
            
            for num_pag in range(len(doc)):
                pagina = doc.load_page(num_pag)
                info_imagenes = pagina.get_image_info(xrefs=True)
                diccionario_texto = pagina.get_text("dict")
                bloques_texto = [b for b in diccionario_texto.get("blocks", []) if b["type"] == 0]

                for img_info in info_imagenes:
                    bbox_img = img_info["bbox"]
                    xref_img = img_info["xref"]
                    x0_img, y0_img, x1_img, y1_img = bbox_img
                    
                    # 1. FILTRO DE LUZ: Ignoramos imágenes demasiado pequeñas (logos, viñetas)
                    ancho = x1_img - x0_img
                    alto = y1_img - y0_img
                    if ancho < 50 or alto < 50:
                        continue 

                    nombre_palabra = "desconocido"
                    distancia_minima = 9999

                    # 2. RADAR EXPANDIDO: Buscamos el texto debajo con mayor tolerancia
                    for bloque in bloques_texto:
                        x0_txt, y0_txt, x1_txt, y1_txt = bloque["bbox"]
                        
                        # El texto debe estar un poco debajo de la imagen, pero no lejísimos (máximo 80 ptos)
                        if (y1_img - 15) <= y0_txt <= (y1_img + 80): 
                            # Tolerancia horizontal más amplia
                            if (x0_img - 50) <= x0_txt <= (x1_img + 50): 
                                distancia_y = abs(y0_txt - y1_img)
                                
                                if distancia_y < distancia_minima:
                                    distancia_minima = distancia_y
                                    
                                    for linea in bloque["lines"]:
                                        texto_linea = "".join([s["text"] for s in linea["spans"]]).strip()
                                        texto_linea_limpio = "".join([c for c in texto_linea if c.isalpha() or c.isspace()]).strip()
                                        
                                        if texto_linea_limpio.isupper() and len(texto_linea_limpio) >= 2:
                                            nombre_palabra = texto_linea_limpio.split()[0].lower()
                                            break

                    # 3. GUARDADO SEGURO (Sin entropía en consola)
                    if nombre_palabra != "desconocido":
                        nombre_archivo = f"{nombre_palabra}.png"
                        es_huerfana = False
                    else:
                        nombre_archivo = f"img_huerfana_{xref_img}.png"
                        es_huerfana = True
                        contador_huerfanas += 1

                    ruta_guardado = os.path.join(self.directorio_salida, nombre_archivo)
                    
                    try:
                        imagen_base = doc.extract_image(xref_img)
                        bytes_imagen = imagen_base["image"]
                        
                        with open(ruta_guardado, "wb") as f:
                            f.write(bytes_imagen)
                            
                        if not es_huerfana:
                            print(f"⚡ [Elena] ¡Precisión máxima! -> {nombre_archivo}")
                        else:
                            print(f"🌱 [Vera] Imagen gráfica sin texto guardada como -> {nombre_archivo}")
                            
                        contador_exitos += 1
                        
                    except Exception:
                        # Silenciamos el error binario, solo avisamos con elegancia
                        print(f"⚠️ [Vera] Fluctuación bloqueada en la imagen con ID {xref_img}. Omitida por seguridad.")

            print(f"🚀 [Elena] ¡Orquestación completada! Extrajimos {contador_exitos} imágenes ({contador_huerfanas} son elementos gráficos sin texto).")
            doc.close()
            
        except Exception as e:
            print(f"⚠️ [Vera] Detalle en el flujo principal: Verifique el documento.")

# ==========================================
# 🚀 IGNICIÓN DEL PROTOCOLO
# ==========================================
if __name__ == "__main__":
    escaner = LenteCorrelacion()
    archivo_objetivo = "Dic_LSM1.pdf" 
    
    print("🌟 [Vera y Elena] Iniciando el Lente de Correlación Espacial v2.1...")
    escaner.escanear_con_precision(archivo_objetivo)