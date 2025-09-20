import tkinter as tk
from tkinter import messagebox
import time
from doc_creator import DocCreator
from txt_creator import TxtCreator
from pdf_creator import PdfCreator
from excel_creator import ExcelCreator
from file_organizer import FileOrganizer
from image_organizer import ImageOrganizer
from report_generator import ReportGenerator


class FileOrganizerGUI:
    """
    Interfaz gráfica con Tkinter.
    Crea archivos de prueba, organiza documentos e imágenes,
    y genera reportes en Excel con estadísticas.
    """

    def __init__(self, root):
        self.root = root
        self.root.title("Organizador de Archivos")
        self.root.geometry("450x300")
        self.root.resizable(False, False)

        # Etiqueta principal
        label = tk.Label(
            root,
            text="📂 Organizador de Archivos",
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

    # --- Métodos principales ---
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
        start_time = time.time()

        moved_files = organizer.organize_files()
        total_files = sum(moved_files.values())
        elapsed_time = time.time() - start_time

        # Estimación de tiempo ahorrado (5 seg por archivo)
        manual_seconds = total_files * 5
        minutes, seconds = divmod(manual_seconds, 60)

        # Generar reporte en Excel
        report = ReportGenerator()
        filename = report.generate_report(moved_files, total_files, manual_seconds)

        messagebox.showinfo(
            "Éxito",
            f"✅ Documentos organizados correctamente.\n\n"
            f"Se movieron {total_files} archivos.\n"
            f"⏳ Te ahorraste aprox. {minutes} min {seconds} seg.\n\n"
            f"📊 Reporte generado en:\n{filename}"
        )

    def organize_images(self):
        organizer = ImageOrganizer()
        start_time = time.time()

        moved_files = organizer.organize_images()
        total_files = sum(moved_files.values())
        elapsed_time = time.time() - start_time

        manual_seconds = total_files * 5
        minutes, seconds = divmod(manual_seconds, 60)

        # Generar reporte en Excel
        report = ReportGenerator()
        filename = report.generate_report(moved_files, total_files, manual_seconds)

        messagebox.showinfo(
            "Éxito",
            f"✅ Imágenes organizadas correctamente.\n\n"
            f"Se movieron {total_files} archivos.\n"
            f"⏳ Te ahorraste aprox. {minutes} min {seconds} seg.\n\n"
            f"📊 Reporte generado en:\n{filename}"
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = FileOrganizerGUI(root)
    root.mainloop()
