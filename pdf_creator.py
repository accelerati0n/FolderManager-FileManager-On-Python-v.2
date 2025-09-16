import os
from reportlab.pdfgen import canvas
from file_creator import FileCreator

class PdfCreator(FileCreator):
    """Crea un archivo .pdf en la carpeta PDF."""

    def __init__(self):
        super().__init__("PDF")

    def create_file(self, filename):
        file_path = os.path.join(self.folder, f"{filename}.pdf")
        c = canvas.Canvas(file_path)
        c.drawString(100, 750, "Este es un archivo PDF creado con reportlab.")
        c.save()
