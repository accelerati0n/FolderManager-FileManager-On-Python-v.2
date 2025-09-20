import tkinter as tk
from tkinter import messagebox
from doc_creator import DocCreator
from txt_creator import TxtCreator
from pdf_creator import PdfCreator
from excel_creator import ExcelCreator
from file_organizer import FileOrganizer
from image_organizer import ImageOrganizer

class FileOrganizerGUI:
    """
    Interfaz gráfica para el organizador de archivos usando Tkinter.
    Permite crear archivos de prueba, organizar documentos e imágenes.
    """

    def __init__(self, root):
        self.root = root
        self.root.title("Organizador de Archivos")
        self.root.geometry("400x250")
        self.root.resizable(False, False)

        # Etiqueta principal
        label = tk.Label(
            root, 
            text="Organizador de Archivos", 
            font=("Arial", 16, "bold"),
            pady=10
        )
        label.pack()

        # Botón para crear archivos de prueba
        btn_create = tk.Button(
            root, 
            text="📄 Crear archivos de prueba", 
            font=("Arial", 12), 
            width=30,
            command=self.create_test_files
        )
        btn_create.pack(pady=5)

        # Botón para organizar documentos
        btn_docs = tk.Button(
            root, 
            text="📂 Organizar documentos", 
            font=("Arial", 12), 
            width=30,
            command=self.organize_documents
        )
        btn_docs.pack(pady=5)

        # Botón para organizar imágenes
        btn_images = tk.Button(
            root, 
            text="🖼️ Organizar imágenes", 
            font=("Arial", 12), 
            width=30,
            command=self.organize_images
        )
        btn_images.pack(pady=5)

        # Botón de salir
        btn_exit = tk.Button(
            root, 
            text="❌ Salir", 
            font=("Arial", 12), 
            width=30,
            command=root.quit
        )
        btn_exit.pack(pady=10)

    # Métodos que conectan con tus clases
    def create_test_files(self):
        creators = [
            DocCreator(),
            TxtCreator(),
            PdfCreator(),
            ExcelCreator(),
        ]
        for creator in creators:
            creator.create_file("test_file")
        messagebox.showinfo("Éxito", "✅ Archivos de prueba creados correctamente.")

    def organize_documents(self):
        organizer = FileOrganizer()
        organizer.organize_files()
        messagebox.showinfo("Éxito", "✅ Documentos organizados correctamente.")

    def organize_images(self):
        img_organizer = ImageOrganizer()
        img_organizer.organize_images()
        messagebox.showinfo("Éxito", "✅ Imágenes organizadas correctamente.")


if __name__ == "__main__":
    root = tk.Tk()
    app = FileOrganizerGUI(root)
    root.mainloop()
