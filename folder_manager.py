import os

class FolderManager:
    """
    Clase base encargada de crear la carpeta principal 'Documents'
    en el Escritorio del usuario y sus subcarpetas:
    Word, Text, PDF y Excel.
    """

    def __init__(self):
        # Detecta el escritorio del usuario
        home = os.path.expanduser("~")
        desktop = os.path.join(home, "Desktop")

        # Carpeta base en el escritorio
        self.base_folder = os.path.join(desktop, "Documents")

        # Subcarpetas por tipo de archivo
        self.subfolders = {
            "Word": os.path.join(self.base_folder, "Word"),
            "Text": os.path.join(self.base_folder, "Text"),
            "PDF": os.path.join(self.base_folder, "PDF"),
            "Excel": os.path.join(self.base_folder, "Excel"),
        }
        self.create_folders()

    def create_folders(self):
        """Crea la carpeta principal y las subcarpetas necesarias en el Escritorio."""
        for folder in self.subfolders.values():
            os.makedirs(folder, exist_ok=True)
