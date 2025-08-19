# Python - Script para insertar de forma automática la firma digital en archivos PDF


## Como Funciona
### 1 - Configuración:

    input_folder: Carpeta con los PDFs originales.

    output_folder: Carpeta donde se guardarán los PDFs firmados.

    signature_image: Ruta de la imagen de tu firma (transparente para mejor resultado).

    position: Coordenadas (x, y) donde se colocará la firma (en puntos, desde la esquina inferior izquierda).

### 2 - Proceso:

    El script crea un PDF temporal con la imagen de la firma usando reportlab.

    Luego, fusiona ese PDF temporal con cada página del PDF original (opcional: solo la primera página).

    Guarda el resultado en la carpeta de salida.

### Personalización
    Ajustar posición/tamaño de la firma:
    Cambia los valores en c.drawImage():

    c.drawImage(signature_image, x=300, y=100, width=120, height=60)  # Ejemplo para esquina superior derecha

### Alternativas
    Usar PyMuPDF (fitz): Más rápido y con soporte para transparencias:

    import fitz  # pip install pymupdf
    doc = fitz.open("documento.pdf")
    for page in doc:
        page.insert_image(fitz.Rect(50, 50, 150, 100), filename="firma.png")  # Rect(x0, y0, x1, y1)
    doc.save("documento_firmado.pdf")

### Notas importantes
    La imagen de la firma debe tener fondo transparente (PNG) para evitar bloques blancos.

    Prueba el script con un PDF de muestra antes de procesar el lote completo.