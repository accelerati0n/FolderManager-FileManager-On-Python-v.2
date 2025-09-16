import os
from file_creator import FileCreator

class TxtCreator(FileCreator):
    """Crea un archivo .txt en la carpeta Text."""

    def __init__(self):
        super().__init__("Text")

    def create_file(self, filename):
        file_path = os.path.join(self.folder, f"{filename}.txt")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("Este es un archivo de texto creado con Python nativo.")
