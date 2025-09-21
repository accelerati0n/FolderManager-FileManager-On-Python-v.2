🛠️ Funcionalidades principales
📁 Creación de carpetas y archivos

El sistema genera una carpeta principal en el Escritorio llamada Documents y dentro de ella las subcarpetas:

- Word → archivos .docx con python-docx
- Text → archivos .txt con Python nativo
- PDF → archivos .pdf con reportlab
- Excel → archivos .xlsx con openpyxl

Cada tipo de archivo es creado por una subclase que implementa el método create_file, mostrando el uso práctico de herencia y polimorfismo.

📂 Organización automática

El programa puede:
- Ordenar documentos (.docx, .txt, .pdf, .xlsx).
- Ordenar imágenes (.jpg, .png, .gif, etc.).
- Mover los archivos encontrados en Escritorio, Documentos y Descargas hacia las carpetas correspondientes en Documents.

📊 Reportes automáticos

Cada vez que se organiza, el programa genera un Excel de reporte en Documents/Reports con:

- Número de archivos movidos por tipo.
- Total de archivos organizados.
- Tiempo ahorrado (estimando 5 segundos por archivo si se hiciera manualmente).
- Fecha y hora de la ejecución.

🖥️ Interfaz gráfica (GUI)

El sistema cuenta con una interfaz gráfica simple en Tkinter, que permite:

- Crear archivos de prueba.
- Organizar documentos.
- Organizar imágenes.
- Generar reportes automáticos.

Salir del programa.

🚀 Ejecución
1. Instalar dependencias
pip install python-docx reportlab openpyxl

2. Ejecutar el programa principal
python gui.py


Los archivos de prueba se crearán automáticamente en la estructura de carpetas.
Al organizar archivos, se generará un Excel con estadísticas del proceso.

👨‍💻 Integrantes

- Miguel Angel Diaz (aka Accelerati0n)
- William Vargas (aka wmvargas-cell)

📋 Revisión

El código fue revisado por el profesor de POO:
Juan Miguel Vargas Cortez (aka juanvarco95)

💥💣 Bombazo para la clase:

https://acortar.link/file_manager
