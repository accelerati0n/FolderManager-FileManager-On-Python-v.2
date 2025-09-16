from doc_creator import DocCreator
from txt_creator import TxtCreator
from pdf_creator import PdfCreator
from excel_creator import ExcelCreator

if __name__ == "__main__":
    # Instanciamos las subclases
    creators = [
        DocCreator(),
        TxtCreator(),
        PdfCreator(),
        ExcelCreator(),
    ]

    # Creamos un archivo de prueba en cada carpeta
    for creator in creators:
        creator.create_file("test_file")

    # Mensaje final
    print("✅ Todos los archivos fueron creados correctamente en sus carpetas correspondientes.")
