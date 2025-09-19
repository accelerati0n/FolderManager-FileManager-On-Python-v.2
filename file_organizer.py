import os
import shutil
from folder_manager import FolderManager

class FileOrganizer(FolderManager):
    """
    Clase que organiza archivos ya existentes en Escritorio, Documentos y Descargas.
    Si encuentra archivos con extensiones conocidas, los mueve a las carpetas correspondientes.
    """

    def __init__(self):
        super().__init__()
        # Directorios típicos en sistemas operativos
        home = os.path.expanduser("~")
        self.search_paths = [
            os.path.join(home, "Desktop"),
            os.path.join(home, "Documents"),
            os.path.join(home, "Downloads"),
        ]
        # Extensiones soportadas y su destino
        self.extension_map = {
            ".docx": self.subfolders["Word"],
            ".txt": self.subfolders["Text"],
            ".pdf": self.subfolders["PDF"],
            ".xlsx": self.subfolders["Excel"],
        }

    def organize_files(self):
        """Busca archivos en las rutas definidas y los mueve a las carpetas correspondientes en Escritorio/Documents."""
        moved_files = 0
        for path in self.search_paths:
            if not os.path.exists(path):
                continue
            for root, _, files in os.walk(path):
                for file in files:
                    ext = os.path.splitext(file)[1].lower()
                    if ext in self.extension_map:
                        src = os.path.join(root, file)
                        dst = os.path.join(self.extension_map[ext], file)
                        try:
                            shutil.move(src, dst)
                            moved_files += 1
                        except Exception as e:
                            print(f"⚠️ No se pudo mover {file}: {e}")
        print(f"✅ Se organizaron {moved_files} archivos en {self.base_folder}.")
