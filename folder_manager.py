import os

class FolderManager:
    """
    Clase base encargada de crear la carpeta principal 'Documents' y
    sus subcarpetas: Word, Text, PDF y Excel.
    """

    def __init__(self, base_folder="Documents"):
        self.base_folder = base_folder
        self.subfolders = {
            "Word": os.path.join(self.base_folder, "Word"),
            "Text": os.path.join(self.base_folder, "Text"),
            "PDF": os.path.join(self.base_folder, "PDF"),
            "Excel": os.path.join(self.base_folder, "Excel"),
        }
        self.create_folders()

    def create_folders(self):
        """Crea la carpeta principal y las subcarpetas necesarias."""
        for folder in self.subfolders.values():
            os.makedirs(folder, exist_ok=True)
