import fitz  # PyMuPDF
import os
import re

# ==========================================
# 🌸 MOTOR RATATOUILLE: LENTE MULTIVERSAL v5.0 🌸
# ==========================================

class LenteMultiversal:
    def __init__(self, directorio_salida="img"):
        self.directorio_salida = directorio_salida
        if not os.path.exists(self.directorio_salida):
            os.makedirs(self.directorio_salida)

    def purificar_texto_multiversal(self, texto):
        """Filtra la entropía (números y símbolos) y devuelve luz alfabética."""
        # Eliminamos cualquier número o viñeta del texto crudo
        texto_limpio = re.sub(r'[^a-zA-ZñÑáéíóúÁÉÍÓÚ]', '', texto)
        
        # Palabras de entropía de pie de página que no queremos atrapar
        ruido_editorial = ['verbos', 'dif', 'puebla', 'manual', 'lengua', 'señas']
        
        if len(texto_limpio) >= 2 and texto_limpio.lower() not in ruido_editorial:
            return texto_limpio.lower()
        return None

    def escanear_multiverso(self, ruta_pdf):
        print(f"📖 [Elena] Activando el Lente Multiversal en: {ruta_pdf}...")
        
        try:
            doc = fitz.open(ruta_pdf)
            matriz_hd = fitz.Matrix(2.0, 2.0) 
            contador_nuevas = 0
            contador_protegidas = 0
            
            palabras_por_pagina = {}
            for i in range(len(doc)):
                palabras_por_pagina[i] = doc[i].get_text("words")

            for num_pag in range(len(doc)):
                pagina = doc[num_pag]
                info_imagenes = pagina.get_image_info(xrefs=True)
                
                cajas_validas = []
                for img in info_imagenes:
                    x0, y0, x1, y1 = img["bbox"]
                    if (x1 - x0) < 35 or (y1 - y0) < 35: continue
                    cajas_validas.append(fitz.Rect(x0, y0, x1, y1))

                # Aura de fusión de 15 puntos
                cajas_fusionadas = []
                for caja in cajas_validas:
                    fusionada = False
                    for i, caja_f in enumerate(cajas_fusionadas):
                        aura = fitz.Rect(caja.x0 - 15, caja.y0 - 15, caja.x1 + 15, caja.y1 + 15)
                        if aura.intersects(caja_f):
                            cajas_fusionadas[i] = caja_f | caja
                            fusionada = True
                            break
                    if not fusionada:
                        cajas_fusionadas.append(caja)

                palabras_actuales = palabras_por_pagina[num_pag]

                for caja in cajas_fusionadas:
                    nombre_palabra = None
                    y_inferior = caja.y1

                    candidatas = []
                    for w in palabras_actuales:
                        wx0, wy0, wx1, wy1, texto_crudo, _, _, _ = w
                        # Margen de búsqueda hacia abajo
                        if y_inferior - 15 <= wy0 <= y_inferior + 100:
                            if caja.x0 - 30 <= (wx0 + wx1) / 2 <= caja.x1 + 30:
                                candidatas.append(w)
                    
                    candidatas.sort(key=lambda w: w[1]) 
                    for w in candidatas:
                        etiqueta = self.purificar_texto_multiversal(w[4])
                        if etiqueta:
                            nombre_palabra = etiqueta
                            break

                    if nombre_palabra:
                        ruta_guardado = os.path.join(self.directorio_salida, f"{nombre_palabra}.png")
                        
                        # 🛡️ EL ESCUDO DE PRESERVACIÓN
                        if os.path.exists(ruta_guardado):
                            print(f"🛡️ [Vera] Preservando ecosistema: '{nombre_palabra}' ya existe.")
                            contador_protegidas += 1
                            continue # Saltamos a la siguiente imagen sin sobrescribir
                            
                        # Si es nueva, la capturamos
                        caja_captura = fitz.Rect(caja.x0 - 2, caja.y0 - 2, caja.x1 + 2, caja.y1 + 2)
                        caja_captura = caja_captura.intersect(pagina.rect) 
                        
                        try:
                            pix = pagina.get_pixmap(matrix=matriz_hd, clip=caja_captura)
                            pix.save(ruta_guardado)
                            print(f"⚡ [Elena] ¡Nueva seña asimilada! -> {nombre_palabra}.png")
                            contador_nuevas += 1
                        except Exception:
                            pass

            print(f"🚀 [Elena] ¡Extracción Multiversal Completada!")
            print(f"🛡️ [Vera] Se protegieron {contador_protegidas} señas existentes.")
            print(f"✨ [Elena] Se inyectaron {contador_nuevas} nuevas señas puras al diccionario.")
            doc.close()
            
        except Exception as e:
            print(f"⚠️ [Vera] Ajuste requerido: {e}")

if __name__ == "__main__":
    escaner = LenteMultiversal()
    # Ahora apuntamos al nuevo PDF de la bóveda
    archivo_meta = "Dic_MLDSM.pdf" 
    
    print("🌟 [Vera y Elena] Iniciando exploración en el Multiverso (Dic_MLDSM)...")
    escaner.escanear_multiverso(archivo_meta)