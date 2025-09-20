import os
import shutil
from folder_manager import FolderManager

class ImageOrganizer(FolderManager):
    """
    Clase que organiza imágenes (.jpg, .jpeg, .png, .gif, .bmp)
    desde Escritorio, Documentos y Descargas hacia una carpeta 'Images'
    dentro de Documents en el Escritorio.
    """

    def __init__(self):
        super().__init__()
        # Crear la subcarpeta "Images" en Documents
        self.image_folder = os.path.join(self.base_folder, "Images")
        os.makedirs(self.image_folder, exist_ok=True)

        # Directorios donde buscar
        home = os.path.expanduser("~")
        self.search_paths = [
            os.path.join(home, "Desktop"),
            os.path.join(home, "Documents"),
            os.path.join(home, "Downloads"),
        ]

        # Extensiones soportadas
        self.supported_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]

    def organize_images(self):
        """Busca imágenes en las rutas definidas y las mueve a la carpeta 'Images'."""
        moved_files = 0
        for path in self.search_paths:
            if not os.path.exists(path):
                continue
            for root, _, files in os.walk(path):
                for file in files:
                    ext = os.path.splitext(file)[1].lower()
                    if ext in self.supported_extensions:
                        src = os.path.join(root, file)
                        dst = os.path.join(self.image_folder, file)
                        try:
                            shutil.move(src, dst)
                            moved_files += 1
                        except Exception as e:
                            print(f"⚠️ No se pudo mover {file}: {e}")
        print(f"✅ Se organizaron {moved_files} imágenes en {self.image_folder}.")
