import os
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO

# Configuración
input_folder = "pdfs_originales"  # Carpeta con los PDFs a modificar
output_folder = "pdfs_firmados"   # Carpeta para guardar los PDFs firmados
signature_image = "/home/jorge/proyectos/firmapdfconpython/signature_image/Logo.png"  # Ruta de la imagen de la firma
position = (50, 50)               # Posición (x, y) de la firma en la página (en puntos)

# Crear carpeta de salida si no existe
os.makedirs(output_folder, exist_ok=True)

def add_signature_to_pdf(input_pdf_path, output_pdf_path):
    # Crear un PDF temporal con la firma usando ReportLab
    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=letter)
    c.drawImage(signature_image, position[0], position[1], width=100, height=50)  # Ajusta ancho/alto
    c.save()

    # Mover el cursor al inicio del buffer
    packet.seek(0)
    signature_pdf = PdfReader(packet)

    # Leer el PDF original
    original_pdf = PdfReader(open(input_pdf_path, "rb"))
    writer = PdfWriter()

    # Fusionar cada página del PDF original con la firma
    for page_num in range(len(original_pdf.pages)):
        page = original_pdf.pages[page_num]
        if page_num == 0:  # Solo firmar la primera página (ajusta si necesitas más)
            page.merge_page(signature_pdf.pages[0])
        writer.add_page(page)

    # Guardar el PDF firmado
    with open(output_pdf_path, "wb") as output_file:
        writer.write(output_file)

# Procesar todos los PDFs en la carpeta de entrada
for filename in os.listdir(input_folder):
    if filename.endswith(".pdf"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        add_signature_to_pdf(input_path, output_path)
        print(f"PDF firmado guardado en: {output_path}")

print("¡Proceso completado!")