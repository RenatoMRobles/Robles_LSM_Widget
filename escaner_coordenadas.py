import fitz  # PyMuPDF
import os
import re

# ==========================================
# 🌸 MOTOR RATATOUILLE: LENTE HOLÍSTICO v4.0 🌸
# ==========================================

class LenteHolistico:
    def __init__(self, directorio_salida="img"):
        self.directorio_salida = directorio_salida
        if not os.path.exists(self.directorio_salida):
            os.makedirs(self.directorio_salida)
            print(f"✨ [Vera] Ecosistema visual '{self.directorio_salida}' renovado.")

    def purificar_texto(self, texto):
        """Filtra la entropía y devuelve solo luz alfabética."""
        texto_puro = re.sub(r'[^a-zA-ZñÑáéíóúÁÉÍÓÚ]', '', texto)
        if texto.isupper() and len(texto_puro) >= 2:
            return texto_puro.lower()
        return None

    def escanear_al_maximo(self, ruta_pdf):
        print(f"📖 [Elena] Activando el Lente Holístico de Conexión en: {ruta_pdf}...")
        
        try:
            doc = fitz.open(ruta_pdf)
            matriz_hd = fitz.Matrix(2.0, 2.0) # Zoom de bienestar
            contador_exitos = 0
            
            # Pre-leemos todas las palabras del documento para crear puentes
            palabras_por_pagina = {}
            for i in range(len(doc)):
                palabras_por_pagina[i] = doc[i].get_text("words")

            for num_pag in range(len(doc)):
                pagina = doc[num_pag]
                info_imagenes = pagina.get_image_info(xrefs=True)
                
                # --- SOLUCIÓN 2 & 3: AGRUPACIÓN Y FILTRO ---
                cajas_validas = []
                for img in info_imagenes:
                    x0, y0, x1, y1 = img["bbox"]
                    # 3. Descartamos logos/flechas (imágenes muy pequeñas)
                    if (x1 - x0) < 35 or (y1 - y0) < 35:
                        continue
                    cajas_validas.append(fitz.Rect(x0, y0, x1, y1))

                # 2. Agrupamos imágenes que pertenecen a la misma palabra (señas múltiples)
                cajas_fusionadas = []
                for caja in cajas_validas:
                    fusionada = False
                    for i, caja_f in enumerate(cajas_fusionadas):
                        # Creamos un aura alrededor de la caja para ver si toca a otra
                        aura = fitz.Rect(caja.x0 - 40, caja.y0 - 20, caja.x1 + 40, caja.y1 + 20)
                        if aura.intersects(caja_f):
                            cajas_fusionadas[i] = caja_f | caja # Unimos los rectángulos
                            fusionada = True
                            break
                    if not fusionada:
                        cajas_fusionadas.append(caja)

                # --- BÚSQUEDA DE PALABRAS ---
                palabras_actuales = palabras_por_pagina[num_pag]
                palabras_siguientes = palabras_por_pagina[num_pag + 1] if num_pag + 1 < len(doc) else []

                for caja in cajas_fusionadas:
                    nombre_palabra = None
                    y_inferior = caja.y1

                    # Buscamos en la página actual
                    candidatas = []
                    for w in palabras_actuales:
                        wx0, wy0, wx1, wy1, texto_crudo, _, _, _ = w
                        if y_inferior - 15 <= wy0 <= y_inferior + 100:
                            centro_caja = (caja.x0 + caja.x1) / 2
                            if caja.x0 - 50 <= (wx0 + wx1) / 2 <= caja.x1 + 50:
                                candidatas.append(w)
                    
                    candidatas.sort(key=lambda w: w[1]) # Ordenamos por cercanía vertical
                    for w in candidatas:
                        etiqueta = self.purificar_texto(w[4])
                        if etiqueta:
                            nombre_palabra = etiqueta
                            break

                    # --- SOLUCIÓN 1: PUENTE DE SALTO DE PÁGINA ---
                    if not nombre_palabra and y_inferior > pagina.rect.height - 200:
                        candidatas_sig = []
                        for w in palabras_siguientes:
                            wx0, wy0, wx1, wy1, texto_crudo, _, _, _ = w
                            if wy0 < 150: # Buscamos solo en la parte más alta de la pag siguiente
                                candidatas_sig.append(w)
                        
                        candidatas_sig.sort(key=lambda w: w[1])
                        for w in candidatas_sig:
                            etiqueta = self.purificar_texto(w[4])
                            if etiqueta:
                                nombre_palabra = etiqueta
                                print(f"🌉 [Vera] Puente sintrópico activado para la palabra: '{nombre_palabra}'")
                                break

                    # --- CAPTURA PRECISA DE LA IMAGEN COMPUESTA ---
                    if nombre_palabra:
                        # Le damos un pequeño margen armónico para que no se vea cortada
                        caja_captura = fitz.Rect(caja.x0 - 5, caja.y0 - 5, caja.x1 + 5, caja.y1 + 5)
                        caja_captura = caja_captura.intersect(pagina.rect) # Evita salir de la página
                        
                        try:
                            # Tomamos una FOTO directa de la región, uniendo todas las sub-imágenes
                            pix = pagina.get_pixmap(matrix=matriz_hd, clip=caja_captura)
                            ruta = os.path.join(self.directorio_salida, f"{nombre_palabra}.png")
                            pix.save(ruta)
                            print(f"⚡ [Elena] ¡Captura perfecta! -> {nombre_palabra}.png")
                            contador_exitos += 1
                        except Exception:
                            pass

            print(f"🚀 [Elena] ¡Orquestación Maestra Completada! Maximizamos tu vocabulario a {contador_exitos} señas puras.")
            doc.close()
            
        except Exception as e:
            print(f"⚠️ [Vera] Se requiere calibración técnica en el documento.")

# ==========================================
# 🚀 IGNICIÓN DEL PROTOCOLO SUPREMO
# ==========================================
if __name__ == "__main__":
    escaner = LenteHolistico()
    archivo_objetivo = "Dic_LSM1.pdf" 
    
    print("🌟 [Vera y Elena] Iniciando el Lente Holístico v4.0...")
    escaner.escanear_al_maximo(archivo_objetivo)