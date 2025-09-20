import shutil
from pathlib import Path

class FileOrganizer:
    """
    Organiza documentos desde Escritorio, Descargas y Documentos.
    Los mueve a subcarpetas dentro de 'Documents' en el Escritorio.
    Devuelve estadísticas de archivos movidos.
    """

    def __init__(self):
        self.desktop = Path.home() / "Desktop"
        self.documents = Path.home() / "Documents"
        self.downloads = Path.home() / "Downloads"

        # Carpeta principal en el Escritorio
        self.main_folder = self.desktop / "Documents"
        self.subfolders = {
            "Word": [".docx"],
            "Text": [".txt"],
            "PDF": [".pdf"],
            "Excel": [".xlsx"]
        }

        # Crear carpeta principal y subcarpetas
        self.main_folder.mkdir(parents=True, exist_ok=True)
        for folder in self.subfolders:
            (self.main_folder / folder).mkdir(parents=True, exist_ok=True)

    def organize_files(self):
        """
        Organiza los archivos encontrados en las carpetas del usuario.
        Retorna estadísticas en forma de diccionario:
        {"Word": 3, "Text": 7, "PDF": 5, "Excel": 2}
        """
        stats = {folder: 0 for folder in self.subfolders}

        # Buscar archivos en Escritorio, Documentos y Descargas
        search_folders = [self.desktop, self.documents, self.downloads]

        for folder in search_folders:
            if folder.exists():
                for file in folder.iterdir():
                    if file.is_file():
                        for subfolder, extensions in self.subfolders.items():
                            if file.suffix.lower() in extensions:
                                destination = self.main_folder / subfolder / file.name
                                try:
                                    shutil.move(str(file), str(destination))
                                    stats[subfolder] += 1
                                except Exception as e:
                                    print(f"❌ Error moviendo {file.name}: {e}")

        return stats
