import os
from openpyxl import Workbook
from file_creator import FileCreator

class ExcelCreator(FileCreator):
    """Crea un archivo .xlsx en la carpeta Excel."""

    def __init__(self):
        super().__init__("Excel")

    def create_file(self, filename):
        wb = Workbook()
        ws = wb.active
        ws.title = "Hoja1"
        ws["A1"] = "Archivo Excel de prueba creado con openpyxl."
        file_path = os.path.join(self.folder, f"{filename}.xlsx")
        wb.save(file_path)
