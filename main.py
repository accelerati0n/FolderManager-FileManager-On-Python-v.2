from doc_creator import DocCreator
from txt_creator import TxtCreator
from pdf_creator import PdfCreator
from excel_creator import ExcelCreator
from file_organizer import FileOrganizer

if __name__ == "__main__":
    print("=== Menú Principal ===")
    print("1. Crear archivos de prueba nuevos")
    print("2. Organizar archivos existentes en Escritorio, Documentos y Descargas")
    option = input("Selecciona una opción (1/2): ")

    if option == "1":
        creators = [
            DocCreator(),
            TxtCreator(),
            PdfCreator(),
            ExcelCreator(),
        ]
        for creator in creators:
            creator.create_file("test_file")
        print("✅ Todos los archivos de prueba fueron creados correctamente.")

    elif option == "2":
        organizer = FileOrganizer()
        organizer.organize_files()

    else:
        print("❌ Opción inválida. Por favor selecciona 1 o 2.")