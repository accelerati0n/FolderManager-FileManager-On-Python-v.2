from folder_manager import FolderManager

class FileCreator(FolderManager):
    """
    Clase abstracta que hereda de FolderManager.
    Define el método create_file que será implementado (polimorfismo)
    por cada subclase.
    """

    def __init__(self, folder_type):
        super().__init__()
        self.folder = self.subfolders[folder_type]

    def create_file(self, filename):
        raise NotImplementedError("Este método debe ser implementado por la subclase.")
