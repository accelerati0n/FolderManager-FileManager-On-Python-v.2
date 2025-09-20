from openpyxl import Workbook
from datetime import datetime
from pathlib import Path

class ReportGenerator:
    """
    Genera un reporte en Excel con estadísticas de los archivos organizados.
    """

    def __init__(self):
        self.desktop = Path.home() / "Desktop"
        self.report_folder = self.desktop / "Documents" / "Reports"
        self.report_folder.mkdir(parents=True, exist_ok=True)

    def generate_report(self, stats, total_files, saved_time):
        """
        Crea un reporte en Excel con:
        - Archivos movidos por tipo
        - Total de archivos movidos
        - Tiempo ahorrado
        """
        wb = Workbook()
        ws = wb.active
        ws.title = "Organización"

        # Encabezado
        ws.append(["Tipo de archivo", "Cantidad de archivos"])

        # Estadísticas por tipo
        for file_type, count in stats.items():
            ws.append([file_type, count])

        # Fila vacía
        ws.append([])

        # Totales
        ws.append(["Total de archivos", total_files])
        ws.append(["Tiempo ahorrado (segundos)", saved_time])
        ws.append(["Generado en", datetime.now().strftime("%Y-%m-%d %H:%M:%S")])

        # Guardar con timestamp
        filename = self.report_folder / f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
        wb.save(filename)

        return filename
