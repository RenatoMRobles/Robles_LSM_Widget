<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Laboratorio Alpha | Motor Ratatouille LSM v2.0</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #1a1a20; color: #fff;
            padding: 50px; text-align: center;
        }

        .laboratorio-container {
            max-width: 600px; margin: 0 auto; background: #2a2a35;
            padding: 30px; border-radius: 15px; border: 1px solid #ffca28;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }

        h1 { color: #ffca28; margin-top: 0; }
        
        textarea {
            width: 100%; height: 100px; background: #15151a; color: #fff;
            border: 1px solid #444; border-radius: 8px; padding: 10px;
            font-size: 1.1em; margin-bottom: 20px; box-sizing: border-box;
            resize: none; outline: none;
        }
        textarea:focus { border-color: #ffca28; }

        button {
            background: #ffca28; color: #000; font-weight: bold; border: none;
            padding: 12px 25px; border-radius: 8px; cursor: pointer; font-size: 1em;
            transition: all 0.3s ease; box-shadow: 0 5px 15px rgba(255, 202, 40, 0.3);
        }
        button:hover { background: #fff; transform: translateY(-2px); }

        #alerta-seguridad {
            background: #ff5252; color: white; padding: 10px; border-radius: 8px;
            margin-bottom: 20px; display: none; font-weight: bold;
        }

        /* 📺 EL WIDGET TIPO TELEVISIÓN */
        #lsm-widget {
            position: fixed; bottom: 30px; left: 30px;
            width: 220px; background: #000; border: 2px solid #ffca28; 
            border-radius: 12px; box-shadow: 0 15px 35px rgba(0,0,0,0.8);
            display: none; flex-direction: column; overflow: hidden; z-index: 999999;
        }

        .lsm-header {
            width: 100%; background: #222; padding: 8px 0;
            font-size: 0.75em; color: #ffca28; text-transform: uppercase; font-weight: bold;
            letter-spacing: 1px; border-bottom: 1px solid #444;
            display: flex; justify-content: space-between; align-items: center;
        }
        .lsm-header span { margin-left: 15px; }
        
        .lsm-cerrar {
            background: none; border: none; color: #aaa; cursor: pointer;
            margin-right: 10px; font-size: 1.2em; padding: 0;
        }
        .lsm-cerrar:hover { color: #ff5252; }

        #lsm-pantalla {
            width: 100%; height: 160px; object-fit: contain;
            background-color: #f5f5f7; 
            transition: opacity 0.1s ease;
        }

        .lsm-texto-actual {
            background: #111; color: #00e676; font-size: 1.2em; font-weight: bold;
            padding: 5px 0; border-top: 1px solid #333; text-transform: uppercase;
            letter-spacing: 2px; height: 25px; display: flex; justify-content: center; align-items: center;
        }

        .lsm-controles {
            width: 100%; display: flex; justify-content: space-between;
            padding: 10px 15px; background: #222; border-top: 1px solid #444;
            box-sizing: border-box; align-items: center;
        }
        
        .lsm-speed-label { font-size: 0.7em; color: #aaa; margin-right: 5px; }
        .lsm-speed { width: 80px; accent-color: #ffca28; }
    </style>
</head>
<body>

    <div class="laboratorio-container">
        <h1>🎙️ Motor Ratatouille LSM v2.0</h1>
        
        <div id="alerta-seguridad">
            ⚠️ ESTÁS USANDO FILE:// - Enciende tu Live Server en VS Code para que el cerebro JSON funcione.
        </div>

        <p>El Auto-Tejedor Lexical está conectado. ¡Prueba a escribir!</p>
        
        <textarea id="textoPrueba" placeholder="Escribe 'gracias' o deletrea..."></textarea>
        <button onclick="iniciarTraduccion()">Activar Intérprete LSM 👐</button>
    </div>

    <div id="lsm-widget">
        <div class="lsm-header">
            <span>Intérprete LSM</span>
            <button class="lsm-cerrar" onclick="detenerLSM()">✖</button>
        </div>
        <img id="lsm-pantalla" src="" alt="Seña">
        <div class="lsm-texto-actual" id="lsm-subtitulo">...</div>
        <div class="lsm-controles">
            <span class="lsm-speed-label">Velocidad</span>
            <input type="range" class="lsm-speed" id="velocidadLSM" min="200" max="2000" value="1000" dir="rtl">
        </div>
    </div>

    <script>
        // 🛡️ Verificar que estamos en un Servidor Local
        if (window.location.protocol === "file:") {
            document.getElementById('alerta-seguridad').style.display = 'block';
        }

        // 🧠 1. EL CEREBRO DINÁMICO (Carga por Fetch)
        let diccionarioLSM = {};

        fetch('diccionario_lsm.json')
            .then(response => {
                if (!response.ok) throw new Error("No se encontró el JSON.");
                return response.json();
            })
            .then(data => {
                diccionarioLSM = data;
                console.log("✨ Cerebro LSM cargado con éxito:", Object.keys(diccionarioLSM).length, "señas.");
            })
            .catch(error => {
                console.error("⚠️ El Guardián CORS bloqueó la carga. Enciende Live Server:", error);
            });

        // Variables de control
        let intervalo;
        let secuenciaReproduccion = [];
        let indexActual = 0;

        function iniciarTraduccion() {
            detenerLSM(); 
            const textoBruto = document.getElementById('textoPrueba').value.toLowerCase().trim();
            if(textoBruto === "") return;

            const textoLimpio = textoBruto.normalize("NFD").replace(/[\u0300-\u036f]/g, "").replace(/[^a-zñ ]/g, '');
            const palabras = textoLimpio.split(/\s+/);
            secuenciaReproduccion = [];

            // 🧠 2. ALGORITMO DE CASCADA (Mapeo directo del JSON)
            palabras.forEach(palabra => {
                if(diccionarioLSM[palabra]) {
                    // Si tienes 'gracias' en tu JSON, agarrará 'img/gracias.png'
                    secuenciaReproduccion.push({ tipo: 'palabra', valor: palabra, src: diccionarioLSM[palabra] });
                } else {
                    // Si no, deletrea
                    let letras = palabra.split('');
                    letras.forEach(letra => {
                        let rutaLetra = diccionarioLSM[letra] ? diccionarioLSM[letra] : `img/${letra}.png`;
                        secuenciaReproduccion.push({ tipo: 'letra', valor: letra, src: rutaLetra });
                    });
                }
                // Añadimos un pequeño espacio visual entre palabras
                secuenciaReproduccion.push({ tipo: 'espacio', valor: ' ', src: 'img/espacio.png' });
            });

            indexActual = 0;
            document.getElementById('lsm-widget').style.display = 'flex';
            reproducirSiguiente();
        }

        function reproducirSiguiente() {
            if (indexActual >= secuenciaReproduccion.length) {
                detenerLSM();
                return;
            }

            let velocidad = document.getElementById('velocidadLSM').value;
            let item = secuenciaReproduccion[indexActual];
            let pantalla = document.getElementById('lsm-pantalla');
            let subtitulo = document.getElementById('lsm-subtitulo');

            pantalla.style.opacity = 0.5;

            setTimeout(() => {
                if (item.tipo === 'espacio') {
                    pantalla.src = item.src; 
                    subtitulo.textContent = "...";
                } else {
                    pantalla.src = item.src;
                    subtitulo.textContent = item.valor;
                }
                pantalla.style.opacity = 1;
            }, 50);

            let tiempoEspera = item.tipo === 'palabra' ? velocidad * 2 : velocidad;
            indexActual++;
            intervalo = setTimeout(reproducirSiguiente, tiempoEspera);
        }

        function detenerLSM() {
            clearTimeout(intervalo);
            document.getElementById('lsm-widget').style.display = 'none';
        }
    </script>
</body>
</html>